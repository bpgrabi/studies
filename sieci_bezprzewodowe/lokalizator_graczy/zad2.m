% Modyfikacja zadania 1, która skupia się na średnim błędzie w zależności
% od miejsca na boisku.

%% ------------------------------------------------------------------------
clear all; close all; clc

%% dane wejściowe
N = 30;                 % liczba graczy
teren = [0,0; 80, 70];  % prostokątny teren gry (musi być 0,0 na początku), musi być int
fn = 2300;              % MHz
df = 5;                 % Mhz
Ptx = 100;              % mW
krotnosc = 5;           % ilość powtórzeń symulacji im większa, 
                        % tym mniej dokładniejszy wynik

%% stałe
% zakładamy, że nadajniki są w narożnikach boiska
R1 = [teren(1,1), teren(1,2)]; 
R2 = [teren(2,1), teren(1,2)];
R3 = [teren(2,1), teren(2,2)];
R4 = [teren(1,2), teren(2,2)];

%% main
dif = zeros(teren(2,1), teren(2,2));
for x = teren(1,1)+1:teren(2,1)
    for y = teren(1,2)+1:teren(2,2)
        for k=1:krotnosc*N
            f = fn + mod(k,N)*df;
            %% obliczanie dystansów od stacji
            d1 = sqrt( (R1(1) - x).^2 + (R1(2) - y).^2 );
            PL1 = -17.5 + 20*log10(d1) + 20*log10(f) + randn*0.3;
            d1new = 10.^ ((PL1 - 50)/20);
        
            d2 = sqrt( (R2(1) - x).^2 + (R2(2) - y).^2 );
            PL2 = -17.5 + 20*log10(d2) + 20*log10(f) + randn*0.3;
            d2new = 10.^ ((PL2 - 50)/20);
            
            d3 = sqrt( (R3(1) - x).^2 + (R3(2) - y).^2 );
            PL3 = -17.5 + 20*log10(d3) + 20*log10(f) + randn*0.3;
            d3new = 10.^ ((PL3 - 50)/20);
        
            d4 = sqrt( (R4(1) - x).^2 + (R4(2) - y).^2 );
            PL4 = -17.5 + 20*log10(d4) + 20*log10(f) + randn*0.3;
            d4new = 10.^ ((PL4 - 50)/20);
        
            %% obliczanie pozycji na podstawie dystansu
            A = [R2(1), R2(2); ...
                 R3(1), R3(2); ...
                 R4(1), R4(2)];
            b = 1/2 * [d1new.^2-d2new.^2 + R2(1).^2+R2(2).^2; ...
                       d1new.^2-d3new.^2 + R3(1).^2+R3(2).^2; ...
                       d1new.^2-d4new.^2 + R4(1).^2+R4(2).^2];
            
            r = ( transpose(A) * A )^(-1) * transpose(A) * b;
            posnew(k,:) = r;
        
            %% obliczanie różnic etc
            dif(x,y) = dif(x,y) + sqrt( (posnew(k,1)-x).^2 + (posnew(k,2)-y).^2 );
        end
        dif(x,y) = dif(x,y)/(krotnosc*N);
    end
end

%% plot
pcolor(transpose(dif))
shading('interp');
colorbar;

%% Wniosek
fprintf(['____________________________________________________________\n' ...
         'Wniosek: jak można zaobserwować, im bliżej środka boiska\n' ...
         'tym dokładnieszy jest pomiar. Większy błąd w narożniakch\n' ...
         'jest spowodowany tym, że pomiar najbliższej anteny jest\n' ...
         'mocno zaburzony. Pathloss w przypadku najbliższej anteny\n' ...
         'jest bardzo mały, a obciążony tym samym błędem, przez co\n' ...
         'błąd względny jest dużo większy.\n' ...
         'Przesunięcie w kierunku lewgo dolnego rogu wynika z tego,\n' ...
         'że wszystkie obliczenia odnoszą się względem punktu (0,0),\n' ...
         'w którym właśnie znajduje się lewa dolna antena. '])
