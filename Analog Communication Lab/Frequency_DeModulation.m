clc;
close all;

fm=2000;
fc=5000;
fs=200000;
t=0:1/fs:0.01;
mi=2;
m=sin(2*pi*fm*t);
subplot(4,1,1);
plot(t,m);
title("Messege Signal");
xlabel('Time');
ylabel('Amplitude');

c=sin(2*pi*fc*t);
subplot(4,1,2);
plot(t,c);
title("Carier Signal");
xlabel('Time');
ylabel('Amplitude');

s=sin(2*pi*fc*t+(mi.*sin(2*pi*fm*t)));
subplot(4,1,3);
plot(t,s);
title("FM Signal");
xlabel('Time');
ylabel('Amplitude');

s=diff(s);
s=abs(s);
subplot(4,1,4);
[b,a]=butter(1,0.005);
z=filter(b,a,s);
z=10.*z;
plot(z);