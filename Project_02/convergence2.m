%COMPUTES THE RATE OF CONVERGENCE
function [dconv] = convergence2
a = 2;                              %Length of the rod
r = 0.2;
qpts = [[-1, 1, 1,-1;
        -1,-1, 1, 1]/sqrt(3.0);
         1, 1, 1, 1];      %Quadrature points

L2 = zeros(1,5);                    %Soltuion values for L2 error norm
h = zeros(1,5);                     %Element size for each solution
m = 1;
mesh = [4, 5, 6, 7, 8];

for elm = mesh
    mm = solve_fem2(elm);
    err1 = 0; dnorm = 0;
    h(m) = mm.en;
    tt = make_mesh(elm,a,r);
    for c = tt.conn
        xe = tt.x(:,c);
        for q = qpts
            [N,dNdp] = shape(q);
            xq = xe*N';
            J = xe*dNdp';
            de = mm.d(c);
            %Exact solution
            T = 10*(xq(1)-a/2)*(xq(1)+a/2)*(xq(2)-a/2)*(xq(2)+a/2);
            %FEM solution
            Th = N*de;
            %L2 Error -Norm
            err1 = err1+((T-Th)^2)*det(J)*q(3);
            dnorm = dnorm +((T)^2)*det(J)*q(3);
        end
    end
    L2(m) = sqrt(err1)/sqrt(dnorm);
    log10(L2)
    log10(h)
    
    m = m+1;
end
figure(5),plot(abs(log10(h)), abs(log10(L2)), 'ro-')
title(sprintf('%d, %d, %d, %d, %d, mesh elements',.../
    mesh(1),mesh(2),mesh(3),mesh(4),mesh(5)));
xlabel('Log of Element size (m)'); ylabel('Log of L2 error norm');
%Rate of Convergence for L2 error norm
dconv = abs(diff(log10(L2)))./abs(diff(log10(h)));
end

function [N,dNdp] = shape(p)
N = 0.25*[(1-p(1))*(1-p(2)),(1+p(1))*(1-p(2)),(1+p(1))*(1+p(2)),.../
    (1-p(1))*(1+p(2))];
dNdp = 0.25*[(p(2)-1),(1-p(2)),(p(2)+1),-(p(2)+1);
    (p(1)-1),-(p(1)+1),(p(1)+1),(1-p(1))];
end


