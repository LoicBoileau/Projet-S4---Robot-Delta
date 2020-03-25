clc;
clear all;
close all;

%%
rA = 0.08083;
rB = 0.06606;
L1 = 0.10183;
L2 = 0.21565;

% theta = 24,2535;

% Xp = [0:10000];
% Yp = Xp;
% Zp = Xp;
% 
% syms phi1_1 phi1_2 phi1_3 phi2_1 phi2_2 phi2_3 phi3_1 phi3_2 phi3_3
% r = rA - rB;
% 
% Xi = r + L1*cosd(theta);
% 
% Y1 = (r + L1*cosd(phi1_1) * sind(theta);
% Y2 = (r + L1*cosd(phi1_2) * sind(theta);
% Y3 = (r + L1*cosd(phi1_3) * sind(theta);
% 
% Zi = -L1 * sind(theta);

%% 
syms z real

param = [L1, L2, rA, rB, z];

% Entrez votre position ici: P = [x, y, z]
P = [-0.1, -0.03, -0.21]; 

% Résultat -> position angulaire des moteurs (deg)
phi_i = CinematiqueInverse(P, param)
