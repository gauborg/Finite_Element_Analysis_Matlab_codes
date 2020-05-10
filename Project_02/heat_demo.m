function [] = heat_demo()
    % node    1    2    3  4
    xe = [0.5, 2.5, 3, 0;    % x-coordinates
          0,   0,   2, 2];   % y-coordinates    
    % Defines 3x4 matrix of quadrature points.
    qpts = [[-1, 1, 1,-1;                   % xi value
             -1,-1, 1, 1] / sqrt(3.0);      % eta value 
              1, 1, 1, 1];                  % integration weight              
    kappa = 54; % W / (m K)
    qbar  = 1000.0; % Heat flux out of bottom edge.
    Tbar  = 30.0;   % Prescribed temperature on top edge.
    s0    = 1000.0; % Heat source; s0*x is in W/m^2
    
    K = zeros(4);
    f = zeros(4,1);       
    % Integrate conductance matrix & heat source term.
    for q = qpts
        [N,dNdp] = shape(q);
        J = xe*dNdp;
        B = dNdp/J;
        xq = xe*N;
        s = s0 * xq(1);  % in W/m^2.        
        K = K + B*kappa*B'*det(J)*q(3);            
        f = f + N*s*det(J)*q(3);                
    end
    % Integrate heat flux on bottom edge (nodes 1-2) (1 pt quadrature).
    N = [0.5; 0.5];        
    f(1:2) = f(1:2) - N*qbar * norm(xe(:,2)-xe(:,1));
    % Enforce essential boundary condition (nodes 3-4).
    for i = [3,4]
        K(i,:) = 0.0;       
        K(i,i) = 1.0;
        f(i) = Tbar;
    end
    
    d = K\f;
    clf;
    patch('vertices', xe', 'faces', [1,2,3,4], 'facecolor', 'interp', ...
          'facevertexcdata', d);
    colorbar;
    axis equal;
    hold on;
        
    pp = linspace(-1+1/30, 1-1/30, 15);
    qq = [];
    xx = [];
    for i = 1:length(pp)
        for j = 1:length(pp)
            [N,dNdp] = shape([pp(i); pp(j)]);
            J = xe*dNdp;
            B = dNdp/J;
            qq(end+1,:) = -kappa * d'*B;
            xx(end+1,:) = xe*N;            
        end
    end
    quiver(xx(:,1), xx(:,2), qq(:,1), qq(:,2), 0.25, 'linewidth', 3, 'color', 'k');    
    axis([0, 3, 0, 2]);
end

function [N, dNdp] = shape(p)
    N = 0.25*[(1-p(1))*(1-p(2));
              (1+p(1))*(1-p(2));
              (1+p(1))*(1+p(2));
              (1-p(1))*(1+p(2))];          
    % derivative   p(1)       p(2)         node
    dNdp = 0.25*[-(1-p(2)), -(1-p(1));    %  1
                  (1-p(2)), -(1+p(1));    %  2
                  (1+p(2)),  (1+p(1));    %  3
                 -(1+p(2)),  (1-p(1))];   %  4
end