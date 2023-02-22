% W tym zadaniu nasi użytkownicy zaczynają się poruszać, więc poziom mocy
% odczytywany przez ich urządzenia będzie się zmieniał. Ciekawym
% zjawiskiem, obnażającym podstawową wadę negatywnego beamformingu
% (zadanie2), jaką jest nagły spadek mocy sygnału, kiedy oba urządzenia są
% w jednej lini z nadajnikiem. 

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

%% ruch
u1speed = [10 0];               % m/s
u2speed = [-20 0];              % m/s
dt = 0.01;                      % krok w czasie

%% main

Prx1 = [];
Prx2 = [];

for k = 0:dt:6
    %% pozycja
    user1pos = user1pos + u1speed*dt;
    user2pos = user2pos + u2speed*dt;

    %% router -> user2
    % wyliczanie odległości 1. użytkownika do obu anten
    r1 = sqrt( (user1pos(1) - ant1(1)).^2 + (user1pos(2) - ant1(2)).^2 );
    r2 = sqrt( (user1pos(1) - ant2(1)).^2 + (user1pos(2) - ant2(2)).^2 );

    % wyliczamy najlepsze przesunięcie fazowe, tak, aby oba sygnały były zgodne
    % w fazie i się sumowały i przesówamy o pi, aby się wygasiły.
    deltafi = 2*pi*(r1-r2)/lambda + pi;

    % wyliczanie odległości 1. użytkownika do obu anten
    r1 = sqrt( (user2pos(1) - ant1(1)).^2 + (user2pos(2) - ant1(2)).^2 );
    r2 = sqrt( (user2pos(1) - ant2(1)).^2 + (user2pos(2) - ant2(2)).^2 );
    
    % wyliczanie transmitancji; zakładamy anteny izotropowe.
    H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
    H2 = exp(-1j*2*pi*r2/lambda + (-1j)*deltafi) * lambda/(4*pi*r2);
    
    % sumujemy transmitancje z obu linków
    H = H1 + H2; 
    
    % wyliczamy moc odebraną; moc dzielona na 2, bo są 2 anteny
    Prx2(end+1) = 10*log10(Ptx/2) + 20*log10(abs(H));    

    %% router -> user1
    r1 = sqrt( (user2pos(1) - ant1(1)).^2 + (user2pos(2) - ant1(2)).^2 );
    r2 = sqrt( (user2pos(1) - ant2(1)).^2 + (user2pos(2) - ant2(2)).^2 );

    deltafi = 2*pi*(r1-r2)/lambda + pi;
    
    r1 = sqrt( (user1pos(1) - ant1(1)).^2 + (user1pos(2) - ant1(2)).^2 );
    r2 = sqrt( (user1pos(1) - ant2(1)).^2 + (user1pos(2) - ant2(2)).^2 );
    
    H1 = exp(-1j*2*pi*r1/lambda) * lambda/(4*pi*r1);
    H2 = exp(-1j*2*pi*r2/lambda + (-1j)*deltafi) * lambda/(4*pi*r2);
    H = H1 + H2; 
    
    Prx1(end+1) = 10*log10(Ptx/2) + 20*log10(abs(H));

end

hold on;
plot(0:dt:6, Prx1)
plot(0:dt:6, Prx2)


%% Wniosek
fprintf(['____________________________________________________________\n' ...
         'Wniosek: kiedy użytkownik docelowy jest w jednej linii \n' ...
         'z nadajnikiem i innym użytkownikiem odbierana moc drastycznie \n' ...
         'spada. Powodem jest to, że staramy się maksymalnie obniżyć \n' ...
         'moc odbieraną u użytkownika, który nie jest adrestem, \n' ...
         'a skoro są w jednej linii to minimalizujemy moc dla obu.\n'])