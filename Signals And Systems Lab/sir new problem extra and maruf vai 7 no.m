clc;
clear all;
close all;

w = [0:1:500] * pi / 500; %[0:pi]
H = exp(1i*w) ./ (exp(1i*w) - 0.9 * ones(1, 501));
magH = abs(H);
angH = angle(H);

subplot(2, 1, 1);
plot(w/pi, magH);
grid on;
title('Magnitude Response');
xlabel('Frequency in pi units');
ylabel('Magnitude |H|');

subplot(2, 1, 2);
plot(w/pi, angH/pi);
grid on;
title('Phase Response');
xlabel('Frequency in pi units');
ylabel('Phase in pi radians');
