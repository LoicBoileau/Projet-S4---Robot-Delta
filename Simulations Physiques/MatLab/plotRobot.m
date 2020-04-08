function [] = plotRobot(P, theta, param)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here


%% init
% Position désirée de l'effecteur
x = P(1);
y = P(2);
z = P(3);

% Positions angulaires des moteurs
theta1 = theta(1);
theta2 = theta(2);
theta3 = theta(3);

% Dimensions des bras en mètre
l_bicep = param(1);
% l_avantBras = param(2);

% Dimensions du rayon de la base et de l'effecteur en mètre
base = param(3);
effecteur = param(4);

% Rotation autour de l'axe z de 120 deg
deg = pi/180; % conversion rad -> deg
Rxy=[cos(120*deg),-sin(120*deg),0;...
     sin(120*deg),cos(120*deg),0;...
     0,0,1];
%% figure details
figure;
grid on;
hold on;
view(50, 35);

%% Draw base and effector
% base
viscircles([0,0], base, 'Color', 'g');

plot(0,0,'ok')


% effector
allAngles = [-pi:0.01:pi];
plot3(effecteur*cos(allAngles)+x, effecteur*sin(allAngles)+y, z*ones(1, length(allAngles)))

plot3(x,y,z,'*k')

%% Draw biceps
% Shoulders
A1 = [base, 0, 0];
A2 = (Rxy*A1')';
A3 = (Rxy*A2')';


plot3([A1(1);A2(1);A3(1)],[A1(2);A2(2);A3(2)], [A1(3);A2(3);A3(3)], 'sk')

% elbows
bRa_1 = [cos(theta1*deg), 0, sin(theta1*deg);...
         0, 1, 0;...
         -sin(theta1*deg), 0, cos(theta1*deg)];
bRa_2 = [cos(theta2*deg), 0, -sin(theta2*deg);...
         0, 1, 0;...
         sin(theta2*deg), 0, cos(theta2*deg)];
bRa_3 = [cos(theta3*deg), 0, -sin(theta3*deg);...
         0, 1, 0;...
         sin(theta3*deg), 0, cos(theta3*deg)];

B1 = A1 + (bRa_1 * [l_bicep, 0, 0]')';
B2 = A2 + ((bRa_2 * Rxy) * [l_bicep, 0, 0]')';
B3 = A3 + ((bRa_3 * Rxy * Rxy) * [l_bicep, 0, 0]')';

plot3([B1(1);B2(1);B3(1)],[B1(2);B2(2);B3(2)], [B1(3);B2(3);B3(3)], 'or')

% lines
line([A1(1), B1(1)], [A1(2), B1(2)], [A1(3), B1(3)], 'color', 'm')
line([A2(1), B2(1)], [A2(2), B2(2)], [A2(3), B2(3)], 'color', 'm')
line([A3(1), B3(1)], [A3(2), B3(2)], [A3(3), B3(3)], 'color', 'm')

%% Draw forearms

% wrists
D1 = [effecteur, 0, 0] + P;
D2 = (Rxy*[effecteur, 0, 0]')' + P;
D3 = ((Rxy*Rxy)*[effecteur, 0, 0]')' + P;

plot3([D1(1);D2(1);D3(1)],[D1(2);D2(2);D3(2)], [D1(3);D2(3);D3(3)], 'sk')


% lines
line([B1(1), D1(1)], [B1(2), D1(2)], [B1(3), D1(3)], 'color', 'm')
line([B2(1), D2(1)], [B2(2), D2(2)], [B2(3), D2(3)], 'color', 'm')
line([B3(1), D3(1)], [B3(2), D3(2)], [B3(3), D3(3)], 'color', 'm')

end

