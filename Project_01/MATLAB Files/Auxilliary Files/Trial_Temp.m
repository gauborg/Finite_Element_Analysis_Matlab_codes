function Project_01_Trials(N,L)
% Inputs %
N=501;
L=500;

% Connectivity and Nodes %
connect=[1:(N-1);2:N];
nodes=[0:(L/(N-1)):L];
disp(nodes);

% Stiffness Matrix Calculation %
Ae=(pi/4)*10*10*70000; % Area * Elastic Modulus %
Le=L/(N-1);            % Le=Element Length %
k=Ae/Le;               % Individual Element Length %
K=zeros(N);
for i=2:N
    K(1,1)=k;
    K(i,i-1)=(-1)*k;
    K(i-1,i)=(-1)*k;
    K(i,i)=2*k;
    K(N,N)=k;
end

% Boundary Conditions %
% Fix the nodes on the left side of Rod %
K(1,2)=0;
K(2,1)=0;

% Apply Traction (Load) and Body Force %
f=zeros(N,1);
f(N,1)=(pi/4)*100*1;

% Solution %
u=K\f;
format long;
disp(u);
end
