%%%% RENAME from mini_project.m to (your_project_short_name).m
% Comments describing mini-project ~ 100-200 words

% Simulation parameters
%	These are values particular to the simulation 
%	that do not change later in the script
% Intial velocity (v0) = 2 m/s
% Intial height   (h0) = 5 m
% Gravity          (g) = 9.81 m/s
% Height of pulley (H) = 10 m 
% Radius of pulley (R) = 1 m
% Length of rope   (L) = 15 m 
% Masses          (m1) = 2 kg
%                 (m2) = 5 kg
% Computed parameters (from simulation parameters)
%	These are values that do not change later in the script
%	and are calculated from formulas using the simulation parameters

% Function calls and simple calculations for:
%	data read-in
%	simulation solution 
%	visualization
m1 = 2
m2 = 5
g = -9.81
v0 = 2
a = ((m2-m1).*g)/(m1+m2)
t = (0:0.1:10)
h = v0.*t + 0.5.*a*t.^2
plot(t,h) 
% Function definitions for simulation solution & visualization
%	Each function contains help text: https://www.mathworks.com/help/matlab/matlab_prog/add-help-for-your-program.html

