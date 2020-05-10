% CODE FOR ANALYTICAL SOLUTION %

N=50;                                     % No. of Calculation Points %
L=0.5;                                    % Length %
nodes=[0:(L/(N-1)):L];                    % Node Positions %
strain=zeros(N-1,1);                      % Defn of Strain and Displacement Matrices %
u=zeros(N,1);
E=70e9;                                   % Elasticity Modulus %
z=0;
A=(pi/4)*0.01*0.01;                       % Area %
for i=1:N
  x=nodes(i);
  u(i,1)=((20*sin(10*pi*x))/(E*A*(pi^2))+(((200/(pi*A*E))-(1e6/E))*x)); %Displacement
  strain(i,1)=(((200*cos(10*pi*x))/(E*A*pi))+((200/(pi*A*E))-(1e6/E))); %Strain
end
xlabel('X distance');
ylabel('Displacement U');
title('Displacement Field Analytical');
legend('Displacement Field');
plot(nodes,u);                            % Graph of Displacement Field %
figure;
plot(nodes,strain);                       % Graph of Strain Field %
xlabel('X distance');
ylabel('Strain');
title('Strain Field Analytical');
legend('Strain Field Analytical');