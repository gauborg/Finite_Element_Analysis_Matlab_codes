function Project_01_Quadratic_02

% Inputs %
N=201;                                              % No of Elements %
L=0.5;                                              % Length of Rod %
ne=(N-1)/2;                                         % No. of Elements %

% Connectivity and Nodes %
conn=[1:2:N-2;2:2:N-1;3:2:N];
nodes=[0:(L/(N-1)):L];
end_nodes=[1:2:N-2];                                % End Nodes Matrix %

% Stiffness Matrix Calculation %
tic;
Ae=(pi/4)*0.01*0.01*70e9;                           % Area * Elastic Modulus %
Le=L/ne;                                            % Le = Element Length %
K=zeros(N);
k=(Ae/(6*Le))*[14,-16,2;-16,32,-16;2,-16,14];

for c = conn
        K(c,c) = K(c,c) + k;
end
toc;

% Calculation of Body Force on every element %
tic;                                                 % Time Start %
f=zeros(N,1);
for c=conn
    Xe=nodes(c);
    le=Xe(2)-Xe(1);
for q=[-1,1]/sqrt(3)
    n=[0.5*(q-1.0)*q,(1.0-q*q),0.5*(q+1.0)*q];
    x=n*Xe';
    f(c)=f(c)+n'*2000*(sin(10*pi*x))*le;
end
end
f(N)=f(N)-((pi/4)*0.01*0.01*1000000);                % Applying Traction Condition %
f(1)=0;                                              % Body force=0 at x=0 %

% Boundary Conditions %
K(1,2)=0;
K(1,3)=0;
K(2,1)=0;
K(3,1)=0;

% Solution %
u=zeros(N,1);
u=K\f;
toc;                                                 % Stop Time %

% Calculation of new node positions %
new_nodes=zeros(N,1);
for i=1:N
    new_nodes(i,1)=nodes(i)+u(i,1);
end
plot(nodes,u,'.b');                                 % Plotting graph for Displacement Field %
xlabel('X distance');
ylabel('Displacement U');
title('Displacement Field against X Distance');
legend('Displacement Field 100');
hold all;

% Elements lengths and strain calculations %

new_length=zeros(ne,1);
for i=1:2:N-2
    new_length((i+1)/2,1)=new_nodes(i+2,1)-new_nodes(i,1); % New Length of Elements %
    strain((i+1)/2,1)=((new_length((i+1)/2,1)-Le)/Le);
end
format long;

figure;
plot(end_nodes,strain,'.b');              % Plotting Graphs for Strain Variation %
title('Strain Field against X Distance');
legend('Strain Field FEM');
xlabel('X distance');
ylabel('Strain Value');

xx=[];
uu=[];
i=1;
for c=conn
    % for Linear Elements, c is 2 by 1, for quadratic, c is 3 by 1 %
    xe = nodes(c);
    de = u(c);
    for p=linspace(-1,1,10)
        shape=[0.5*(p-1.0)*p,(1.0-p*p),0.5*(p+1.0)*p];
        uu(i)=shape*de;
        i=i+1;
    end
end

plot(xx,uu,'ro');

end
