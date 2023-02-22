% W tym zadaniu należało tak skorygować fazę, aby sygnał przeznaczony dla
% 1. użytkownika miał jak najmniejszą moc u 2. użytkownika i odwrotnie,
% dzięki czemu wzajemne zakłócenia będą jak najmniejsze. 

%% ------------------------------------------------------------------------
clear all; close all; clc;

%% dane wejściowe
txpos = [100, 0];               % pozycja nadajnika
Ptx = 0.005;                    % W - moc nadajnika
f = 6;                          % GHz - częstotliwość pracy
lambda = 3*10.^8 / (f*10.^9);   % m - długość fali
ant1 = [100, -0.0125];          % pozycja 1. anteny w nadajniku
ant2 = [100, 0.0125];           % pozycja 2. anteny w nadajniku
noise = -135;                   %dBW - szumy w kanale

user1pos = [50, 70];            % pozycja 1. użytkownika 
user2pos = [160, 50];           % pozycja 2. użytkownika

%% main
%% router -> user2
fprintf('Transmisja do 2. użytkownika. Moc tego sygnału ma być minimalna z punktu widzenia user1.\n');
% wyliczanie odległości 1. użytkownika do obu anten
r1 = sqrt( (user1pos(1) - ant1(1)).^2 + (user1pos(2) - ant1(2)).^2 );
r2 = sqrt( (user1pos(1) - ant2(1)).^2 + (user1pos(2) - ant2(2)).^2 );

% wyliczanie transmitancji; zakładamy anteny izotropowe.
H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
H2 = exp(-1j*2*pi*r2/lambda) * lambda/(4*pi*r2);
% sumujemy transmitancje z obu linków
H = H1 + H2; 

% wyliczamy moc odebraną; moc dzielona na 2, bo są 2 anteny
Prx = 10*log10(Ptx/2) + 20*log10(abs(H));
fprintf('SNR przed modyfikacją dla user1 %f\n', Prx - noise);

% wyliczamy najlepsze przesunięcie fazowe, tak, aby oba sygnały były zgodne
% w fazie i się sumowały i przesówamy o pi, aby się wygasiły.
deltafi = 2*pi*(r1-r2)/lambda + pi;

H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
H2 = exp(-1j*2*pi*r2/lambda + (-1j)*deltafi) * lambda/(4*pi*r2);
H = H1 + H2; 

Prx = 10*log10(Ptx/2) + 20*log10(abs(H));
fprintf('SNR po modyfikacją dla user1 %f\n', Prx - noise');

r1 = sqrt( (user2pos(1) - ant1(1)).^2 + (user2pos(2) - ant1(2)).^2 );
r2 = sqrt( (user2pos(1) - ant2(1)).^2 + (user2pos(2) - ant2(2)).^2 );

H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
H2 = exp(-1j*2*pi*r2/lambda) * lambda/(4*pi*r2);
H = H1 + H2; 

Prx = 10*log10(Ptx/2) + 20*log10(abs(H));
fprintf('SNR przed modyfikacją dla user2 %f\n', Prx - noise');

H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
H2 = exp(-1j*2*pi*r2/lambda + (-1j)*deltafi) * lambda/(4*pi*r2);
H = H1 + H2; 

Prx = 10*log10(Ptx/2) + 20*log10(abs(H));
fprintf('SNR po modyfikacją dla user2 %f\n', Prx - noise');

%% space
fprintf(['____________________________________________________________\n' ...
         'Transmisja do 1. użytkownika. Moc tego sygnału ma być minimalna z punktu widzenia user2.\n']);

%% router -> user1
r1 = sqrt( (user2pos(1) - ant1(1)).^2 + (user2pos(2) - ant1(2)).^2 );
r2 = sqrt( (user2pos(1) - ant2(1)).^2 + (user2pos(2) - ant2(2)).^2 );

H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
H2 = exp(-1j*2*pi*r2/lambda) * lambda/(4*pi*r2);
H = H1 + H2; 

Prx = 10*log10(Ptx/2) + 20*log10(abs(H));
fprintf('SNR przed modyfikacją dla user2 %f\n', Prx - noise');

deltafi = 2*pi*(r1-r2)/lambda + pi;

H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
H2 = exp(-1j*2*pi*r2/lambda + (-1j)*deltafi) * lambda/(4*pi*r2);
H = H1 + H2; 

Prx = 10*log10(Ptx/2) + 20*log10(abs(H));
fprintf('SNR po modyfikacją dla user2 %f\n', Prx - noise');

r1 = sqrt( (user1pos(1) - ant1(1)).^2 + (user1pos(2) - ant1(2)).^2 );
r2 = sqrt( (user1pos(1) - ant2(1)).^2 + (user1pos(2) - ant2(2)).^2 );

H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
H2 = exp(-1j*2*pi*r2/lambda) * lambda/(4*pi*r2);
H = H1 + H2; 

Prx = 10*log10(Ptx/2) + 20*log10(abs(H));
fprintf('SNR przed modyfikacją dla user1 %f\n', Prx - noise');

H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
H2 = exp(-1j*2*pi*r2/lambda + (-1j)*deltafi) * lambda/(4*pi*r2);
H = H1 + H2; 

Prx = 10*log10(Ptx/2) + 20*log10(abs(H));
fprintf('SNR po modyfikacją dla user1 %f\n', Prx - noise);

%% Wniosek
fprintf(['____________________________________________________________\n' ...
         'Wniosek: sygnał z reguły traci na jakości u docelowego \n' ...
         'użytkownika, ale dzięki temu nie zakłóca drugiego.\n'])