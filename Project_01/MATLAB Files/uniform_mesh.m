function [mesh] = uniform_mesh(lx, ly, ex, ey)
    nx = ex+1;  
    ny = ey+1;
    mesh.x = zeros(2, nx*ny);
    mesh.connectivity = zeros(3,ex*ey);
    for j=1:ny
        for i=1:nx
            mesh.x(:, i+(j-1)*nx) = [(i-1)*lx/ex; (j-1)*ly/ey];
            if i < ex+1 && j < ey+1
                a = i + (j-1)*nx;
                e = 2*(i+(j-1)*ex)-1;
                mesh.connectivity(:,e)   = [a;   a+1;    a+nx];
                mesh.connectivity(:,e+1) = [a+1; a+nx+1; a+nx];
            end
        end
    end
end