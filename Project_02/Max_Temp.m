% Calculation of Temperature Plot %

x=[-1:0.01:1];
y=[-1:0.01:1];

k=54;
L=2;
for i=1:201
    for j=1:201
        if (x(i)^2)+(y(i)^2)>=0.04
        T = 10*(x(i)-L/2)*(x(i)+L/2)*(y(i)-L/2)*(y(i)+L/2);
        plot(x,y,T,'o');
        hold on;
        end
    end
end
format long;
b=max(T);
disp(b);                 % Display Maximum Temperature %

% Calculation of Source %

x=[-1:0.01:1];
y=[-1:0.01:1];
s=zeros(1,201);

for i=1:201
    for j=1:201
        if (x(i)^2)+(y(i)^2)>=0.04
        s(i) = -20*k*((x(i)^2)+(y(i)^2)-2);
        end
    end
end
format long;
a=max(s);
disp(a);                 % Display Maximum Source Value %

% Calculation of Heat Flux %

x=[-1:0.01:1];
y=[-1:0.01:1];
q=zeros(1,201);
for i=1:201
    for j=1:201
        q(i) = -20*k*((x(i)+(y(i)))*((x(i)*y(i))-1));
        end
end
format long;
a=max(q);
disp(a);                 % Display Maximum Source Value %


