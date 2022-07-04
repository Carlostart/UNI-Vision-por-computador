function MC = momentos_centrales(I)
    MC=[0 0 0 0 0 0 0 0 0 0]; 
    I=double(I);
    [r c]=size(I); 
    m=zeros(r,c); 
    % geometric moments 
    for i=0:1 
        for j=0:1 
            for x=1:r 
                for y=1:c 
                    m(i+1,j+1)=m(i+1,j+1)+(x^i*y^j*I(x,y)); 
                end
            end
        end
    end
    xb=m(2,1)/m(1,1); 
    yb=m(1,2)/m(1,1);
    % central moments 
    u=[ 0 0 0 0;0 0 0 0;0 0 0 0;0 0 0 0]; 
    for i=0:3 
        for j=0:3 
            for x=1:r 
                for y=1:c 
                    u(i+1,j+1)=u(i+1,j+1)+(x-xb)^i*(y-yb)^j*I(x,y); 
                end
            end
        end
    end
    MC = [u(1,1) u(2,1) u(1,2) u(2,2) u(3,1) u(1,3) u(3,2) u(2,3) u(4,1) u(1,4)];