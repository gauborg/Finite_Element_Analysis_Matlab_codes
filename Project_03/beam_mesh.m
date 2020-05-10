% Create biased mesh on a beam with center hole.
function [mesh] = beam_mesh(ey, L, r)                   
    center = plate_w_hole_mesh(ey/2, L/3, r);
    left   = uniform_mesh(ey, ey, L/3, L/3, -L/2, -L/6);
    right  = uniform_mesh(ey, ey, L/3, L/3,  L/6, -L/6);

    mesh = merge_meshes(center, left);
    mesh = merge_meshes(mesh, right);
end

% Combines two meshes (deleting overlapping nodes).
function [m] = merge_meshes(m1, m2)
    nn1  = length(m1.x);
    % Mesh 1 nodes retain the same id numbers, mesh 2 nodes are incremented.
    m.x = [m1.x, m2.x];
    m.conn = [m1.conn, m2.conn + nn1];
        
    % Approximate mesh size (this doesn't need to be very accurate).
    h = norm(m1.x(:,2)-m1.x(:,1));
    
    % Find common nodes (need to loop backwards over j).
    for j = length(m2.x):-1:1
        for i = 1:length(m1.x)
            if (norm(m1.x(:,i) - m2.x(:,j)) < 1e-9*h)
                % Replaces node j w/ node i.
                m = replace_node(m, j+nn1, i);                                
            end
        end
    end   
end

function [m] = replace_node(m, j, i)
    % Delete node j.
    m.x(:,j) = [];    
    m.conn(m.conn == j) = i;
    m.conn(m.conn > j) = m.conn(m.conn > j) - 1;    
end


function [mesh] = plate_w_hole_mesh(nh, side_len, hole_radius)
    % plate_w_hole_mesh Returns a mesh for a square plate with a center hole.
    %   Input arguments: nh - number of elements along half of a side.
    %                    side_length - length of a side of the plate.
    %                    hole_radius - radius of hole in center of plate.	    
    n_shell = nh+1;
    nns = 8*nh;  % number of nodes in a shell.            
    circle = hole_radius*make_circle(nns)';
    square = side_len*make_square(nh)';
    mesh.x = [];
    for s = 1:n_shell
        % f goes from 0 to 1 as a linear function.
        f = (s-1)/(n_shell-1);
        mesh.x = [mesh.x, square*(1-f) + circle*f];
    end            
    mesh.conn = [];
    for j=1:n_shell-1
        for i=1:nns-1               
          n0 = i + (j-1)*nns;          
          mesh.conn(:,end+1) = [n0; n0+1; n0+1+nns; n0+nns];           
       end               
       mesh.conn(:,end+1) = [1+(j-1)*nns; 1+(j)*nns; 
                             mesh.conn(3,end); mesh.conn(2,end)];
    end    
end

function [m] = uniform_mesh(ex, ey, lx, ly, x0, y0)
    % if origin is not specified, then set it to zero.
    if nargin < 5, x0 = 0; end
    if nargin < 6, y0 = 0; end       
        
    m.num_nodes = (ex+1)*(ey+1);
    % Nodal reference coordinates.
    m.x    = zeros(2, m.num_nodes);   
    for j=1:ey+1
        for i=1:ex+1
            m.x(:,i+(j-1)*(ex+1)) = [(i-1)*lx/ex + x0; (j-1)*ly/ey + y0];
        end
    end
    m.num_elements = ex*ey;
    m.conn = zeros(4, m.num_elements);
    for j=1:ey
        for i=1:ex            
            % First node in element
            n0 = i+(j-1)*(ex+1);            
            m.conn(:,i+(j-1)*ex) = [n0; n0+1; n0+ex+2; n0+1+ex];            
        end
    end
end
function [x] = make_square(nh)    
    x(1:nh+1,1) = 0.5;
    x(1:nh+1,2) = linspace(0, 0.5, nh+1);
    x(nh+1:3*nh+1,1) = linspace(0.5, -0.5, 2*nh+1);
    x(nh+1:3*nh+1,2) = 0.5;    
    x(3*nh+1:5*nh+1,1) = -0.5;
    x(3*nh+1:5*nh+1,2) = linspace(0.5, -0.5, 2*nh+1);    
    x(5*nh+1:7*nh+1,1) = linspace(-0.5, 0.5, 2*nh+1);
    x(5*nh+1:7*nh+1,2) = -0.5;
    x(7*nh+1:8*nh,1) = 0.5;    
    x(7*nh+1:8*nh,2) = linspace(-0.5,-0.5/nh,nh);
end
function [x] = make_circle(nns)
    q = linspace(0, 2*pi, nns+1)';
    x = [cos(q(1:end-1)), sin(q(1:end-1)) + 0.00*sin(7*q(1:end-1)) ];
end
