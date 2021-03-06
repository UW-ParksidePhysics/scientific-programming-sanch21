x = [0:.1:10]
mu = 5
e = 2.718
y1 = (1/((0.5)*sqrt(2*pi)))*e.^-((x-mu).^2)/(2*(0.5).^2)
y2 = (1/((1.0)*sqrt(2*pi)))*e.^-((x-mu).^2)/(2*(1.0).^2)
y3 = (1/((1.5)*sqrt(2*pi)))*e.^-((x-mu).^2)/(2*(1.5).^2)
function_values = []
sigma = 0.5:0.5:1.5
plot(x,y1,"-", x,y2,"--", x,y3,":")
xlabel('xaxis')
ylabel('phi(x-5,sigma)')
legend('sigma(0.5)','sigma(1.0)','sigma(1.5)')
