clc;
clear all;
close all;

% Define the system impulse response h(n)
n = 0:100; % Range of values for n
h = (0.9).^n .* (n >= 0); % Impulse response h(n)

% Compute the frequency response H(e^(jw))
w = linspace(-pi, pi, 1000); % Range of values for w
H = freqz(h, 1, w); % Frequency response H(e^(jw))

% Plot the magnitude response
subplot(2, 1, 1);
plot(w, abs(H));
xlabel('Frequency (rad/sample)');
ylabel('|H(e^{jw})|');
title('Magnitude Response');
grid on;

% Plot the phase response
subplot(2, 1, 2);
plot(w, angle(H));
xlabel('Frequency (rad/sample)');
ylabel('Phase (rad)');
title('Phase Response');
grid on;
