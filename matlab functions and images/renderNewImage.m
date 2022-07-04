function renderNewImage(x_proj, y_proj, depth_transformed, image_RGB)

%Compute 3D coordinates
[rows,cols] = size(depth_transformed);
new_image = zeros(rows,cols,3);
new_depth = 10*ones(rows,cols);

for u=1:cols,
    for v=1:rows,
        if (depth_transformed(v,u) > 0)
            for k=0:1,
                for l=0:1,
                    y_now = floor(y_proj(v,u))+l;
                    x_now = floor(x_proj(v,u))+k;

                    if ((y_now < 1)||(y_now > rows)||(x_now < 1)||(x_now > cols))
                        continue;
                    end

                    if (new_depth(y_now,x_now) > depth_transformed(v,u));
                        new_image(y_now,x_now,:) = image_RGB(v,u,:);
                        new_depth(y_now,x_now) = depth_transformed(v,u);
                    end
                end
            end
        end
    end
end

imshow(uint8(new_image));

end

