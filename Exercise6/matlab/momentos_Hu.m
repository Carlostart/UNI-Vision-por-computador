function HM=momentos_Hu(I)
% Calcula los momentos de Hu invariantes de una imagen (I) en niveles de gris
% Si se desea obtener la descripción de momentos de un único objeto de la
% imagen, el resto hay que ponerlos a cero.
%
% Entrada: Imagen I en niveles de gris
% Salida:  Vector HM (7x1) de momentos de Hu (invariantes)
% 
% Fecha: 2009-2012 Javier Gonzalez
 
    I=double(I)/255;
 
    % Momentos centrales                             
    % [mu00,mu10,mu01,mu11,mu20,mu02,mu21,mu12,mu30,mu03] = momentos_centrales(I);
    mom = momentos_centrales(I);
 
    %Momentos normalizados
    u002 = mom(1)*mom(1);
    u0025 = mom(1)^2.5;
    %u0015 = mu00^1.5
    n02 = mom(6)/u002;
    n20 = mom(5)/u002;
    n11 = mom(4)/u002;
    n12 = mom(8)/u0025;
    n21 = mom(7)/u0025;
    n03 = mom(10)/u0025;
    n30 = mom(9)/u0025;
 
    %Momentos invariantes de Hu
    f1 = n20+n02; 
    f2 = (n20-n02)^2 + 4*n11^2;
    f3 = (n30-3*n12)^2+(3*n21-n03)^2;
    f4 = (n30+n12)^2+(n21+n03)^2;
    f5 = (n30-3*n12)*(n30+n12)*((n30+n12)^2 - 3*(n21+n03)^2) + (3*n21-n03)*(n21+n03)*(3*(n30+n12)^2 - (n21+n03)^2);
    f6 = (n20-n02)*((n30+n12)^2 - (n21+n03)^2) + 4*n11*(n30+n12)*(n21+n03);
    f7 = (3*n21-n03)*(n30+n12)*((n30+n12)^2 - 3*(n21+n03)^2) - (n30-3*n12)*(n21+n03)*(3*(n30+n12)^2 - (n21+n03)^2);
    
    HM = [f1 f2 f3 f4 f5 f6 f7];

return;