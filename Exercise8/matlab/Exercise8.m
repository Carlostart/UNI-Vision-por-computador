close all
clear variables

% 1: Homogeneous transformations
% 2: Camera-to-world transformation
% 3: World-to-camera transformation
execute = 3;

% -------------------------------------------------------------------------
% 1: Homogeneous transformations
%
if execute == 1 
    
    % Initial translations
    tx = 0; ty = 0; tz = 0;

    % Initial reference frame
    T = [1 0 0 tx
         0 1 0 ty
         0 0 1 tz
         0 0 0  1]; 
     showTransformation(T);

     % Move the camera 0.5 meters forward
     tx = 0; ty = 0; tz = 0.5;
     T = [1 0 0 tx
          0 1 0 ty
          0 0 1 tz
          0 0 0 1]; 
     showTransformation(T);

     % Rotate the camera 35degrees to look to the left (yaw rotation)
     tx = 0; ty = 0; tz = 0;
     yaw = deg2rad(35);
     T = [1 0         0        tx
          0 cos(yaw) -sin(yaw) ty
          0 sin(yaw)  cos(yaw) tz
          0 0         0        1];
     showTransformation(T);

     % Move the camera 0.5 meters upwards and rotate it downwards
     tx = 0; ty = -0.5; tz = 0;
     pitch = deg2rad(45);
     T = [cos(pitch) 0 sin(pitch) tx
          0          1 0          ty
         -sin(pitch) 0 cos(pitch) tz
          0          0 0          1];
     showTransformation(T);
     
% -------------------------------------------------------------------------
% 2: Camera-to-world transformation
%     
elseif execute == 2 || execute == 3
    
    % Read the rgb and depth images images
    rgb = 'person_rgb.png';
    depth = 'person_depth.png';
    im_rgb = imread(rgb);
    im_depth = imread(depth);    
 
    % Show them
    figure
    imshow(im_rgb)
    figure
    imshow(im_depth)
    
    % Camera intrinsic parameters
    f = 525;
    x0 = 319.5;
    y0 = 239.5;
    
    % Initialization of useful vectors
    [rows,cols] = size(im_depth);
    points_x = zeros(rows,cols);
    points_y = zeros(rows,cols);
    points_z = zeros(rows,cols);
    
    % Depth scale and max depth considered
    scale = 0.0002;
    max_depth = 5; 
    
    % Obtain the 3D coordinates of each pixel
    for y=1:rows
        for x=1:cols
            points_z(y,x) = double(im_depth(y,x))*scale;
            if points_z(y,x) > max_depth % check max depth
                points_z(y,x) = 0;
            end
            if points_z(y,x) ~= 0
                points_x(y,x) = -1*x*scale;
                points_y(y,x) = -1*y*scale;    
            end
        end
    end
    
    downsample = 2; % increment this downsampling depending on your 
                    % pc's computational power
                        
    if execute == 2
        plot3DScene(points_x,points_y,points_z,im_rgb,downsample);
    end
end

% -------------------------------------------------------------------------
% 3: World-to-camera transformation
%
if execute == 3
    
    % Modify this transformation
    transform = [-0.3; -0.3; -0.3; 0; -10; 0]; % -z, -x, -y, z, yaw, pitch, roll
    T = TMatrixFromValues(transform);
    
    % Useful variables
    proj_x = zeros(rows,cols);
    proj_y = zeros(rows,cols);
    z_t = zeros(rows,cols);
    
    % Coompute the coordinates (pixels) of each 3D point
    for x=1:cols
        for y=1:rows
            
            % Apply the transformation T to the point
            % The coordinates are reorder because of the Matlab coordinates
            % system: x towards (our z), y left (our x), z upwards (our y)
            p = [points_z(y,x); points_x(y,x); points_y(y,x); 1];
            z_t(y,x) = T(1,:)*p;
            x_t = T(2,:)*p;
            y_t = T(3,:)*p;
            
            % Now, use the K matrix to retrieve proj_x (x') and proj_y
            % (y'). These are the coordinates (x',y') of the 3D point in
            % the image!
            proj_x(y,x) = -1*(x_t*f+z_t(y,x)*x0);
            proj_y(y,x) = -1*(y_t*f+z_t(y,x)*y0);
        end
    end
    
    renderNewImage(proj_x, proj_y, z_t, im_rgb);
end