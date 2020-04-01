clc;
clear all;
close all;

%% Init parameters
rA = 0.08083; % rayon de la base
rB = 0.06606; % rayon de l'effecteur
L1 = 0.10183; % Longueur du bicep
L2 = 0.21565; % longueur de l'avant bras

param = [L1, L2, rA, rB];

%% Inverse Kinematic inputs
% On considère que le point central entre les moteurs est [0, 0, 0].

% Entrez votre position ici: P = [x, y, z]
P = [-0.1, -0.03, -0.21]

%% Execution

% Résultat -> position angulaire des moteurs (deg)
phi_i = CinematiqueInverse(P, param)

%% Validation
% https://www.marginallyclever.com/other/samples/fk-ik-test.html
