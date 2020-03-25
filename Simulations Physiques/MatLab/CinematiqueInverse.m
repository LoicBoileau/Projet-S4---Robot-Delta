function [t] = CinematiqueInverse(P, param)
x = P(1);
y = P(2);
z = P(3);

t1 = 0;
t2 = 0;
t3 = 0;

[t1, s] = calcul(P, param);
if(s == 0)
    [t2, s] = calcul([x*cos(120*pi/180) + y*sin(120*pi/180), y*cos(120*pi/180)-x*sin(120*pi/180), z],param);
end

if(s==0)
    [t3,s] = calcul([x*cos(120*pi/180) - y*sin(120*pi/180), y*cos(120*pi/180)+x*sin(120*pi/180), z],param);
end

if(s==0) 
    t = eval([t1,t2,t3]);
else
    t = [0,0,0];
end
end


function [theta, s] = calcul(P, param)

x = P(1);
y = P(2);
z = P(3);

% Dimensions des bras en mètre
l_bicep = param(1);
l_avantBras = param(2);

% Dimensions de la base et l'effecteur en mètre
base = param(3);
effecteur = param(4);

theta = [0, 0, 0];

%% 
% y1 = -base/(2*sqrt(3));
% k = effecteur/(2*sqrt(3));
y = y - effecteur;

a = (x^2 + y^2 + z^2 + l_bicep^2 - l_avantBras^2 + base^2)/(2*z);
b = (-base-y)/z;

d = -(a+b*-base)^2 + l_bicep*(b^2 * l_bicep + l_bicep);

if(d < 0) % Position impossible
    s = 1;
else 
    yj = (-base - a*b - sqrt(d))/(b^2 + 1);
    zj = a + b*yj;
    theta = 180 * atan(-zj/(-base - yj))/pi;
    
    if(yj > -base) % On choisi l'autre solution
        theta = theta + 180;
    end
    
    s = 0;
end
end

