function [phi_i] = CinematiqueInverse(P, param)
% Calcul les positions angulaires nécessaire pour atteindre la position
% désirée de l'effecteur
% Prend en paramètre le vecteur position P=[x, y, z] et les paramètres du
% robot param=[Longueur_bicep, longueur_avantBras, rayon_base, rayon_effecteur].
% Retourne un vecteur phi_i=[phi_1, phi_2, phi_3] contenant les positions angulaires des
% moteurs du bras.

% Position désiré de l'effecteur
x = P(1);
y = P(2);
z = P(3);

% Angle phi résultants
phi_1 = 0;
phi_2 = 0;
phi_3 = 0;

% Calcul de phi 1
[phi_1, singularite] = calcul(P, param);

if(singularite == 0)
    % Calcul phi 2
    [phi_2, singularite] = calcul([x*cos(120*pi/180) + y*sin(120*pi/180), ...
                         y*cos(120*pi/180) - x*sin(120*pi/180), ...
                         z]...
                         ,param);
end

if(singularite == 0)
    % Calcul phi 3
    [phi_3,singularite] = calcul([x*cos(120*pi/180) - y*sin(120*pi/180), ...
                        y*cos(120*pi/180) + x*sin(120*pi/180), ...
                        z]...
                        ,param);
end

if(singularite == 0) % Position angulaire trouvée
    phi_i = [phi_1, phi_2, phi_3];
else % Il y a eu un problème pour au moins une section du bras
    phi_i = [0, 0, 0]; % Position par défaut
end

end

%% Fonction interne
function [phi, singularite] = calcul(P, param)
% Calcul la position angulaire d'une section pour atteindre la position
% désirée de l'effecteur.
% Prend en paramètre un vecteur de position P et les paramètres du robot.

% Position désirée de l'effecteur
x = P(1);
y = P(2);
z = P(3);

% Dimensions des bras en mètre
l_bicep = param(1);
l_avantBras = param(2);

% Dimensions du rayon de la base et de l'effecteur en mètre
base = param(3)/(2*sqrt(3));
effecteur = param(4)/(2*sqrt(3));

phi = 0;

y = y - effecteur;

ni = (x^2 + y^2 + z^2 + l_bicep^2 - l_avantBras^2 + base^2)/(2*z);
mi = (-base - y)/z;

% Espace 3D atteingnable par l'effecteur si li >= 0
li = -(ni + mi*-base)^2 + l_bicep*(mi^2*l_bicep + l_bicep);

if(li < 0) % Position impossible
    singularite = 1;
else 
    yi = (-base - ni*mi - sqrt(li))/(mi^2 + 1);
    zi = ni + mi*yi;
    phi = 180 * atan(-zi/(-base - yi))/pi;
    
    if(yi > -base) % On choisi l'autre solution
        phi = phi + 180;
    end
    
    singularite = 0;
end
end
