function [d_res_max,stress_max] = project_3(ey)

tic
L = 3.0;
r = 0.2;
E = 69*1e9;
v = 0.34;
mesh = beam_mesh(ey, L, r);
nn = length(mesh.x);

qpts = [[-1 1 -1 1;-1 -1 1 1]/sqrt(3); 1 1 1 1];
K = zeros(2*nn);
f = zeros(2*nn,1);
B = zeros(3,8);
% D = E / (1-v^2) .*[1 v 0
%                    v 1 0
%                    0 0 0.5*(1-v)]; % plane stress
D = E / ((1+v)*(1-2*v)) .*[1-v v   0
                          v   1-v 0
                          0   0   0.5*(1-2*v)]; % plane strain
for c = mesh.conn   
    xe = mesh.x(:,c);                                   % Nodal displacements in element
    for q = qpts                                        % Using two point Gauss Quadrature
        [N,dNdp] = shape_beam(q);                       % Shape function 
        J = xe * dNdp';                                  % Jacobian
        dNdx = dNdp' / J;
        B(1,1:2:end) = dNdx(:,1);
        B(2,2:2:end) = dNdx(:,2);
        B(3,1:2:end) = dNdx(:,2);
        B(3,2:2:end) = dNdx(:,1);
        c2 = [c(1)*2-1;c(1)*2;c(2)*2-1;c(2)*2;c(3)*2-1;c(3)*2;c(4)*2-1;c(4)*2];
        K(c2,c2) = K(c2,c2) + B' * D * B * q(3) * det(J);        
    end
end

% Natural boudary condition
nodes_R = find(mesh.x(1,:)==1.5);
conn_R = [nodes_R(1):ey:nodes_R(end-1);nodes_R(2):ey:nodes_R(end)];
for c_R = conn_R
    y_R = mesh.x(2,c_R);
    le = abs(y_R(2)-y_R(1));
    for q = [-1 1]/sqrt(3)
        qq = 0.5 * [1-q;1+q];
        yq = y_R * qq;
        f(2*c_R-1) = f(2*c_R-1) + qq * 600 * 1e6 * yq * le/2;
    end
end

% Essential boundary condition
nodes_L = find(mesh.x(1,:)==-1.5);
cc = [nodes_L(:)*2-1, nodes_L(:)*2];
K(:,cc) = 0;
K(cc,:) = 0;
for i = 1:2*length(cc)
    K(cc(i),cc(i)) = 1;
end
f(cc) = 0;
d = K\f;
d_x = d(1:2:end)';
d_y = d(2:2:end)';
d_res = sqrt(d_x.^2 + d_y.^2);
d_res_max = max(d_res);

    
% Contour plot of approximated resultant displacement field
% figure(1),patch('vertices', mesh.x', 'faces', mesh.conn', 'facecolor', 'interp','facevertexcdata', d_res');
% title('Resultant displacement field')
% colorbar;       axis equal;
% hold on;
% p = colorbar;
% set(get(p,'title'),'string','Displacement');
% xlabel('X (meters)');        ylabel('Y (meters)');
% figure(1)
% quiver(mesh.x(1,:),mesh.x(2,:),d_x,d_y,'k');

% Contour plot of approximated displacement field along x direction
% figure(2),patch('vertices', mesh.x', 'faces', mesh.conn', 'facecolor', 'interp','facevertexcdata', d_x');
% title('Displacement Field along X axis')
% colorbar;       axis equal;
% hold on;
% p = colorbar;
% set(get(p,'title'),'string','Displacement');
% xlabel('X (meters)');ylabel('Y (meters)');
% figure(2)
% quiver(mesh.x(1,:),mesh.x(2,:),d_x,zeros(1,length(d_x)),'k');

% Contour plot of approximated displacement field along y direction
% figure(3),patch('vertices', mesh.x', 'faces', mesh.conn', 'facecolor', 'interp','facevertexcdata', d_y');
% title('Displacement Field along Y axis')
% colorbar;       axis equal;
% hold on;
% p = colorbar;
% set(get(p,'title'),'string','Displacement');
% xlabel('X (meters)');ylabel('Y (meters)');
% figure(3)
% quiver(mesh.x(1,:),mesh.x(2,:),zeros(1,length(d_x)),d_y,'k');


% Stress field calculation
strain = zeros(3,length(mesh.x));                       % Initializing strain field to zeros
stress = zeros(3,length(mesh.x));                       % Initializing stress field to zeros
for c = mesh.conn   
    xe = mesh.x(:,c);                                   % Nodal displacements in element
    c2 = [c(1)*2-1;c(1)*2;c(2)*2-1;c(2)*2;c(3)*2-1;c(3)*2;c(4)*2-1;c(4)*2];
    de = d(c2);
    i = 1;
    for q = qpts                                        % Using two point Gauss Quadrature
        [N,dNdp] = shape_beam(q);                       % Shape function 
        J = xe * dNdp';                                  % Jacobian
        dNdx = dNdp' / J;
        B(1,1:2:end) = dNdx(:,1);
        B(2,2:2:end) = dNdx(:,2);
        B(3,1:2:end) = dNdx(:,2);
        B(3,2:2:end) = dNdx(:,1);
        strain(:,c(i)) = B * de;
        stress(:,c(i)) = D * strain(:,c(i));
        i = i + 1;
     end
end
      
% Contour plot of sigma_xx field
figure(4),patch('vertices', mesh.x', 'faces', mesh.conn', 'facecolor', 'interp','facevertexcdata', stress(1,:)');
title('Sigma-xx Field (Stress along X)')
colorbar;axis equal;
hold on;
p = colorbar;
set(get(p,'title'),'string','Sigma XX');
xlabel('X (meters)');ylabel('Y (meters)');
stress_max = max(stress(1,:));

% Sigma xx along AA' line
% nodes_down = find((abs(mesh.x(1,:))<=1e-2 & mesh.x(2,:)<0));
% nodes_top = find((abs(mesh.x(1,:))<=1e-2 & mesh.x(2,:)>0));
% figure(5)
% plot(mesh.x(2,nodes_down),stress(1,nodes_down),'ko',mesh.x(2,nodes_top),stress(1,nodes_top),'ko',mesh.x(2,nodes_down),stress(1,nodes_down),'k',mesh.x(2,nodes_top),stress(1,nodes_top),'k')
% title('Sigma XX along AA` line');
% xlabel('Y (meters)');
% ylabel('Sigma-XX (Pascals)');

% Initial and deformed structures
% new_mesh = zeros(2,nn);
% new_mesh(1,:) = mesh.x(1,:) + d_x;
% new_mesh(2,:) = mesh.x(2,:) + d_y;
% for c = mesh.conn
%     figure(6)
%     plot(mesh.x(1,c),mesh.x(2,c),'k',new_mesh(1,c),new_mesh(2,c),'k--')
%     title('Undeformed and Deformed structures')
%     xlabel('X (meters)');ylabel('Y (meters)');
%     legend('Undeformed Structure','Deformed structure')
%     hold on
% end
% figure(6)
% c = [1;4*ey];
% plot(mesh.x(1,c),mesh.x(2,c),'k',new_mesh(1,c),new_mesh(2,c),'k--')
% toc

end

function [N,dNdp] = shape_beam(q)
N = 0.25*[(1-q(1))*(1-q(2)),(1+q(1))*(1-q(2)),(1+q(1))*(1+q(2)),.../
            (1-q(1))*(1+q(2))];
dNdp = 0.25*[(q(2)-1),(1-q(2)),(q(2)+1),-(q(2)+1);
         (q(1)-1),-(q(1)+1),(q(1)+1),(1-q(1))];
end