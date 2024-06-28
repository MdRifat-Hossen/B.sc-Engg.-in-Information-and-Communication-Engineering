clc;
clear all;
close all;

fm=25;
fc=400;
b=10;
t=0:0.0001:0.25;



m=cos(2*pi*fm*t);
subplot(3,1,1);
plot(t,m);
title("Frequrency Signal");
xlabel('Time');
ylabel('Amplitude');

c=sin(2*pi*fc*t);
subplot(3,1,2);
plot(t,c);
title("Cariar Signal");
xlabel('Time');
ylabel('Amplitude');


s=sin((2*pi*fc*t)+b.*sin(2*pi*fm*t));
subplot(3,1,3);
plot(t,s);
title("Mulated Signal");
xlabel('Time');
ylabel('Amplitude')
