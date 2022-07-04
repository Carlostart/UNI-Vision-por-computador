%Draw original and transformed reference frames from an homogeneous
%transformation (do View->camera toolbar and then first rotation + Y to see
%it properly)

function showTransformation(T)

%Translation
%xi = [0.3; 0.5; 0; 0; 0; 0];
%T = TMatrixFromValues(xi); 

origin = [T(1,4) T(2,4) T(3,4)];
axis_x_cam = T*[1; 0; 0; 1];
axis_y_cam = T*[0; 1; 0; 1];
axis_z_cam = T*[0; 0; 1; 1];

%show
figure; hold on;

%Plot original reference frame (blue)
plot3([0 1], [0 0], [0 0],'b');
plot3([0 0], [0 1], [0 0],'b');
plot3([0 0], [0 0], [0 1],'b');
points_x = [0 1 0 0];
points_y = [0 0 0 1];
points_z = [0 0 1 0];
scatter3(points_x, points_y, points_z,'b');
axis equal;
axis([-2 2 -2 2 -2 2]);
grid on;
xlabel('x'); ylabel('y'); zlabel('z');
%view([-128.4 -45]);
view(3) %y up

%Plot transformed reference frame (red)
plot3([origin(1) axis_x_cam(1)], [origin(2) axis_x_cam(2)], [origin(3) axis_x_cam(3)],'r');
plot3([origin(1) axis_y_cam(1)], [origin(2) axis_y_cam(2)], [origin(3) axis_y_cam(3)],'r');
plot3([origin(1) axis_z_cam(1)], [origin(2) axis_z_cam(2)], [origin(3) axis_z_cam(3)],'r');
points_x = [origin(1) axis_x_cam(1) axis_y_cam(1) axis_z_cam(1)];
points_y = [origin(2) axis_x_cam(2) axis_y_cam(2) axis_z_cam(2)];
points_z = [origin(3) axis_x_cam(3) axis_y_cam(3) axis_z_cam(3)];
scatter3(points_x, points_y, points_z,'r');
axis equal;
axis([-2 2 -2 2 -2 2]);
grid on;

end
