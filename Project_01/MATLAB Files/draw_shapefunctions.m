function [] = draw_shapefunctions()
clc
clf
    % Length of domain.
    L  = 2.0;
    % Number of element divisions per side.
    ne = 4;    
    mesh = uniform_mesh(L, L, ne, ne);
    for n = 1:length(mesh.x)        
        draw_one_shapefunction(mesh, L, ne, n);
        patch('vertices', mesh.x', 'faces', mesh.connectivity', ...
              'facecolor', 'none', 'linewidth', 2); 
        axis([0,2,0,2,0,3]); axis off; 
        view(60, 45);
        pause(0.5);
    end
end

function [] = draw_one_shapefunction(mesh, L, ne, n)
    xx = linspace(0, L, 100);
    z = zeros(length(xx));
    % Loops over global coordinates (x,y) -> [xx(i),xx(j)], and determines
    % which element the global point is in using the structure of the mesh.
    % Once the element is found, evalute the shape functions and if element
    % contains the node that we want to plot, save it to matrix, z.
    for j = 1:length(xx)
        for i = 1:length(xx)
            % Estimate which row and column of elements the current point 
            % is located at.
            ex = min(floor(xx(i)*ne/L), ne-1);
            ey = min(floor(xx(j)*ne/L), ne-1);
            
            % Guess that point is located within the lower element.
            e = 2*(ex + ey*ne) + 1;                        
            x = [xx(i), xx(j)];
            xe = mesh.x(:, mesh.connectivity(:,e));            
            N = shape3(x, xe);
            % If shape functions are not 0<N<1, then we are not in this
            % element, switch to the upper element.
            if min(N) < 0.0 || max(N) > 1.0
                e = e + 1;
                xe = mesh.x(:, mesh.connectivity(:,e));
                N = shape3(x, xe);                
            end
            % If element contains the target node, then set z to be equal
            % to the corresponding shape function.
            if any(mesh.connectivity(:,e) == n)
                z(i, j) = N(mesh.connectivity(:,e) == n);
            end                        
        end        
    end
    surf(xx,xx,z, 'facealpha', 0.75, 'edgecolor', 'k', 'edgealpha', 0.2)
end

% Uses equation (7.7) in the textbook.
function [N] = shape3(x, xe)
    N = [1 x] / [[1;1;1], xe'];   
end