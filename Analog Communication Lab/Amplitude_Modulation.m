clc;
clear all;
close all;

t=0:0.001:2;
fm=5;
fc=50;

m=sin(2*pi*fm*t);
subplot(5,1,1);
plot(t,m);
title("massege Signal");
xlabel('Time');
ylabel('Amplitude');

c=sin(2*pi*fc*t);
subplot(5,1,2);
plot(t,c);
title("Carrer Signal");
xlabel('Time');
ylabel('Amplitude');

m1=0.5;
s1=(1+(m1*m)).*c;
subplot(5,1,3);
plot(t,s1);
title("Undder Signal");
xlabel('Time');
ylabel('Amplitude');

m2=1;
s2=(1+(m2*m)).*c;
subplot(5,1,4);
plot(t,s2);
title("Critical Signal");
xlabel('Time');
ylabel('Amplitude');

m3=1.5;
s3=(1+(m3*m)).*c;
subplot(5,1,5);
plot(t,s3);
title("Over Signal");
xlabel('Time');
ylabel('Amplitude');
