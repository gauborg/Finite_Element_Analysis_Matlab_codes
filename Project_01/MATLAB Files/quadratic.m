function[] = quadratic()
    nn = 17;                        % Number of nodes.
    xI = linspace(0, 10.0, nn);     % Coordinates at nodes.
    fI = myfunction(xI);            % Value of function f at nodes.    
    conn = [1:2:nn-2; 2:2:nn-1; 3:2:nn];    
    xx = [];
    ff = [];
    for c = conn
        xe = xI(c);
        fe = fI(c);
        for p = linspace(-1, 1, 50)
            N = shape3(p);
            xx(end+1) = xe*N;
            ff(end+1) = fe*N;
        end
    end
    
    x = linspace(xI(1), xI(end), 1000);
    f = myfunction(x);
    
    % Plots f(x) using the interpolation from shape functions.
    subplot(2,1,1);
    hold on;
    h1 = plot(x, f, 'k');     % Plots exact function as line.
    h2 = plot(xx, ff, 'r-');  % Plot interpolated solution as line.    
    plot(xI, fI, 'ro');       % Plot nodal values as circles.
    xlabel('x');
    ylabel('f(x)');
    legend([h1,h2], {'exact', 'quadratic interpolation'});
    
    % Plots f(x) using default MATLAB (linear) interpolation.
    subplot(2,1,2);
    plot(x, f, 'k', xI, fI, 'o-');
    xlabel('x');
    ylabel('f(x)');
    legend('exact', 'linear interpolation');
end
% Defines an arbitrary function to be interpolated.
function [f] = myfunction(x)
    f = sin(2*x) .* exp(-x/ 10.0);
end
% Shape functions of quadratic, 3-node element.
function [N] = shape3(p) 
    N = [0.5*(p-1.0)*p; 1.0-p*p; 0.5*(p+1.0)*p];
end