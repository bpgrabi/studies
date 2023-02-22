% Próba lokalizacji zawodników na boisku za pomocą anten umieszczonych w
% rogach boiska w oparciu o path loss. Znając odległość czujnika względem 4
% anten, z pewnym przybliżeniem, można wyznaczyć położenie czujnika.
% Odległość jest obliczana na podstawie path loss wyliczanego ze wzoru,
% który może wynikać np. z badań doświadczalnych, lub jakiś modeli 
% matematycznych.
% Czerwone gwiazdki - pozycja oryginalna
% Niebieskie gwiazdki - pozycja wyliczona
% Na końcu programu wyświetli się średni błąd lokalizacji (w metrach)

%% ------------------------------------------------------------------------
clear all; close all; clc

%% dane wejściowe
N = 30;                 % liczba graczy
teren = [0,0; 80, 70];  % prostokątny teren gry w metrach
fn = 2300;              % MHz - nośna
df = 5;                 % Mhz - każdy czujnik nadaje na innej 
                        % częstotliwości równej fn+k*df (k należy do Z)
Ptx = 100;              % mW - moc anten nadających sygnał
dp = 0.1;               % wahania w path lose wynikające z błędu pomiaru, 
                        % niedoskonałego modelu wyliczania path loss

%% stałe
% zakładamy, że nadajniki są w narożnikach boiska
R1 = [teren(1,1), teren(1,2)];
R2 = [teren(2,1), teren(1,2)];
R3 = [teren(2,1), teren(2,2)];
R4 = [teren(1,2), teren(2,2)];

%% pozycje graczy
% rozlosowanie pozycji czujników (graczy)
pos = rand([N,2]);
pos(:,1) = pos(:,1)*teren(2,1);
pos(:,2) = pos(:,2)*teren(2,2);
posnew = zeros(N,2);

%% main

dif = 0;
for k = 1:N
    %% obliczanie dystansów od stacji
    % obliczanie prawdziwej odległości czujnika od nadajnika w rogu (0,0)
    d1 = sqrt( (R1(1) - pos(k,1)).^2 + (R1(2) - pos(k,2)).^2 );     
    % obliczanie path loss na podstawie rzeczywistej odległości i dodanie
    % pewnej losowości (błąd pomiaru, niedoskonałość wzoru)
    PL1 = -17.5 + 20*log10(d1) + 20*log10(fn + k*df) + randn*dp;
    % obliczanie odległości jaką wyznaczy czujnik
    d1new = 10.^ ((PL1 - 50)/20);

    d2 = sqrt( (R2(1) - pos(k,1)).^2 + (R2(2) - pos(k,2)).^2 );
    PL2 = -17.5 + 20*log10(d2) + 20*log10(fn + k*df) + randn*dp;
    d2new = 10.^ ((PL2 - 50)/20);
    
    d3 = sqrt( (R3(1) - pos(k,1)).^2 + (R3(2) - pos(k,2)).^2 );
    PL3 = -17.5 + 20*log10(d3) + 20*log10(fn + k*df) + randn*dp;
    d3new = 10.^ ((PL3 - 50)/20);

    d4 = sqrt( (R4(1) - pos(k,1)).^2 + (R4(2) - pos(k,2)).^2 );
    PL4 = -17.5 + 20*log10(d4) + 20*log10(fn + k*df) + randn*dp;
    d4new = 10.^ ((PL4 - 50)/20);

    %% obliczanie pozycji na podstawie dystansu
    A = [R2(1), R2(2); ...
         R3(1), R3(2); ...
         R4(1), R4(2)];
    b = 1/2 * [d1new.^2-d2new.^2 + R2(1).^2+R2(2).^2; ...
               d1new.^2-d3new.^2 + R3(1).^2+R3(2).^2; ...
               d1new.^2-d4new.^2 + R4(1).^2+R4(2).^2];
    
    r = inv(( transpose(A) * A )) * transpose(A) * b;
    posnew(k,:) = r;

    %% obliczanie różnic etc
    dif = dif + sqrt( (posnew(k,1)-pos(k,1)).^2 + (posnew(k,2)-pos(k,2)).^2 );
end

blad_sredni = dif/N;
fprintf("Średni błąd pomiaru: %fm", blad_sredni);

%% plot
rectangle('Position',[teren(1,:), teren(2,:)]);
axis([teren(1,1) teren(2,1) teren(1,2) teren(2,2)]); 
hold on;

for k=1:N
    plot(pos(k,1), pos(k,2), '*r');
    plot(posnew(k,1), posnew(k,2), '*b');
end
