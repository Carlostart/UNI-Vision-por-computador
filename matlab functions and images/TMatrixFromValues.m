function A = TMatrixFromValues(xi)
    
    x = xi(1); y = xi(2); z = xi(3);
    yaw = xi(4); pitch = xi(5); roll = xi(6);

    cy = cos(degtorad(yaw));
    sy = sin(degtorad(yaw));

    cp = cos(degtorad(pitch));
    sp = sin(degtorad(pitch));

    cr = cos(degtorad(roll));
    sr = sin(degtorad(roll));

    A = [cy*cp, cy*sp*sr-sy*cr, cy*sp*cr+sy*sr, x; ...
         sy*cp, sy*sp*sr+cy*cr, sy*sp*cr-cy*sr, y; ...
         -sp, cp*sr, cp*cr, z;
         0 0 0 1];
end