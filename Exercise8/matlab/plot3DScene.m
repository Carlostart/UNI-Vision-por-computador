function plot3DScene(X,Y,Z,image_RGB,downsample)

rows_down = size(image_RGB,1)/downsample;
cols_down = size(image_RGB,2)/downsample;

%Downsample
x_down = X(1:downsample:end, 1:downsample:end);
y_down = Y(1:downsample:end, 1:downsample:end);
z_down = Z(1:downsample:end, 1:downsample:end);
r_down = image_RGB(1:downsample:end, 1:downsample:end, 1);
g_down = image_RGB(1:downsample:end, 1:downsample:end, 2);
b_down = image_RGB(1:downsample:end, 1:downsample:end, 3);

%Draw 3D point cloud
x_vec = reshape(x_down,rows_down*cols_down,1);
y_vec = reshape(y_down,rows_down*cols_down,1);
z_vec = reshape(z_down,rows_down*cols_down,1);
c = zeros(rows_down*cols_down,3);
c(:,1) = double(reshape(r_down,rows_down*cols_down,1))/255;
c(:,2) = double(reshape(g_down,rows_down*cols_down,1))/255;
c(:,3) = double(reshape(b_down,rows_down*cols_down,1))/255;

scatter3(z_vec,x_vec,y_vec,5*downsample,c,'filled');
axis equal;

end


