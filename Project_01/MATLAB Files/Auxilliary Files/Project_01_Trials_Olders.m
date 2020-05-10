function Project_01_Trials(N,L)
% Inputs %
N=101;
L=0.5;

% Connectivity and Nodes %
connect=[1:(N-1);2:N];
nodes=[0:(L/(N-1)):L];

% Stiffness Matrix Calculation %
Ae=(pi/4)*0.01*0.01*70e9;   % Area * Elastic Modulus %
Le=L/(N-1);                 % Le = Element Length %
k=Ae/Le;                    % Individual Element Stiffness (Calculated in N/m) %
K=zeros(N);
for i=2:N
    K(1,1)=k;
    K(i,i-1)=(-1)*k;
    K(i-1,i)=(-1)*k;
    K(i,i)=2*k;
    K(N,N)=k;
end

f=zeros(
for i=

% Boundary Conditions %
% Fix the nodes on the left side of Rod %
K(1,1)=0;
K(1,2)=0;
K(2,1)=0;


% Solution %
u=K\f;

% Calculation of deformed element length at every node %
new_length=zeros(N-1,1);        % Defines new element lengths matrix %
for i=1:N-1
    new_length(i,1)=u(i+1,1)-u(i,1);
end

% Calculation of deformed element length at every node %
strain=zeros(N-1,1);
for i=1:N-1
    strain(i,1)=((new_length(i,1)-Le)/Le);
end
end

