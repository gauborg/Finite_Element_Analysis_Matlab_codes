%Program to solve 2D Heat transfer equation
%
%     ?.q - s = 0;   where q = -k?T
%
%  with b.c
%
%    T = 0 on the plate boundary
%
%  using the FEM for 4-node quadrilateral element.
%
%  No. of elements along half side 'nel' is the input argument.
%  Returns the computed temperature distribution d, the norm errors
%  and the field  plots.

function [h] = solve_fem2(nel)
%PREPROCESSING
a = 2;                      %Dimension of the plate
r = 0.2;                    %Radius of the hole
k = 54;                     %Conductivity W/(mK)
Tbar = 0;                   %Prescribed temperature on the plate boundary.
D = k*eye(2);

m = make_mesh(nel,a,r);
h.en = length(m.conn);
h.nn = length(m.x);           %Total number of nodes

%ASSEMBLY
qpts = [[-1, 1, 1,-1;                   
         -1,-1, 1, 1] / sqrt(3.0);       
          1, 1, 1, 1];      %Quadrature points

f = zeros(h.nn,1);
K = zeros(h.nn);
fq = zeros(h.nn,1);

for c = m.conn
    xe = m.x(:,c); 
    for q = qpts
        [N,dNdp] = shape(q);
        xq = xe*N';
        J = xe*dNdp';
        B = dNdp'/J;
        s = -10*k*(2*xq(1)^2 + 2*xq(2)^2 - a^2);      %in W/m^2.        
        K(c,c) = K(c,c) + B*D*B'*det(J)*q(3);  
        f(c) = f(c) + N'*s*det(J)*q(3);
    end
end

le = norm((m.x(:,end) -m.x(:,end-1)));
connflux = [(h.nn+1-8*nel):h.nn-1,h.nn;(h.nn+2-8*nel):h.nn,(h.nn+1-8*nel)];


for c = connflux
    xe = m.x(:,c);
    for q =[-1 1]/sqrt(3)
        N = 0.5*[1+q 1-q];
        xq = N*xe';
        qq = -k*[20*xq(1)*(xq(2)^2 - a^2/4);20*xq(2)*(xq(1)^2 - a^2/4)];
        n = [xq(1);xq(2)]/r;
        fq(c) = fq(c) + N'.*(qq'*n*le/2);
    end
end
f = f + fq;

%BOUNDARY CONDITIONS
% Enforce essential boundary condition (nodes on the plate edges)
for i = 1:(8*nel)
    K(i,:) = 0.0;       
    K(i,i) = 1.0;
    f(i) = Tbar;
end


%SOLUTION
h.d = K\f;
max(h.d)
clf;

%PLOT

%Mesh
x2d = m.x(1,1:end);
y2d = m.x(2,1:end);
figure(1),plot(x2d, y2d, 'o')
title('Mesh')

%FEM Solution
% for c = m.conn
%     xe = m.x(:,c);
%     hold on
%     figure(2),patch('vertices', xe', 'faces', [1,2,3,4], 'facecolor', 'interp', ...
%           'facevertexcdata', h.d(c));
%     colorbar;
%     axis equal;
%     hold on;
% 
%     pp = linspace(-1+1/30, 1-1/30, 15);
%     qq = [];
%     xx = [];
%     for i = 1:length(pp)
%         for j = 1:length(pp)
%             [N,dNdp] = shape([pp(i); pp(j)]);
%             J = xe*dNdp';
%             B = dNdp'/J;
%             qq(end+1,:) = -k*h.d(c)'*B;
%             xx(end+1,:) = xe*N';            
%         end
%     end
%     figure(2),quiver(xx(:,1), xx(:,2), qq(:,1), qq(:,2), 0.25, 'linewidth', 3, 'color', 'k');    
% end

%Plot of temperature along the center y=0 || -l/2 < x < l/2
kk = find(abs(m.x(2,:))<= 1e-10);
left = kk(2:2:end); right = kk(end-1:-2:1);
figure(2),plot(m.x(1,left),h.d(left),'b*-',m.x(1,right),h.d(right),'b*-')


end

%Shape function & its derivate for a 4-node quadrilateral element
function [N,dNdp] = shape(p)
N = 0.25*[(1-p(1))*(1-p(2)),(1+p(1))*(1-p(2)),(1+p(1))*(1+p(2)),.../
            (1-p(1))*(1+p(2))];
dNdp = 0.25*[(p(2)-1),(1-p(2)),(p(2)+1),-(p(2)+1);
         (p(1)-1),-(p(1)+1),(p(1)+1),(1-p(1))];
end
       