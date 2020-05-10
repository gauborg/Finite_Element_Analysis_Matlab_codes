function Project_01_Trials(N,L)
% Inputs %
N=1001;
L=500;

% Connectivity and Nodes %
connect=[1:(N-1);2:N];
nodes=[0:(L/(N-1)):L];

% Stiffness Matrix Calculation %
Ae=(pi/4)*10*10*70000;      % Area * Elastic Modulus %
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

% Apply Force on the rightmost node %
f=zeros(N,1);
f(N,1)=78.5398;

u=zeros(N,1);
% Boundary Conditions %
K(1,2)=0;
K(2,1)=0;

% Solution %
u=K\f;
format long;

new_nodes=zeros(N,1);
for i=1:N
    new_nodes(i,1)=nodes(i)+u(i,1);
end

% Calculation of deformed element length at every node %
% Defines new element lengths matrix %
for i=1:N-1
    new_length(i,1)=new_nodes(i+1,1)-new_nodes(i,1);
end
% disp(new_length);

% Calculation of deformed element length at every node
strain=zeros(N-1,1);
for i=1:(N-1)
    strain(i,1)=((new_length(i,1)-Le)/Le);
end
disp(strain);
end
