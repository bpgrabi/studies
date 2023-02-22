% Tym razem pozycja jest obliczana na podstawie kąta spoda jakiego dotarł
% do czujnika sygnał od anteny. 
% Czerwone gwiazdki - pozycja oryginalna
% Niebieskie gwiazdki - pozycja wyznaczona

%% ------------------------------------------------------------------------
clear all; close all; clc

%% dane wejściowe
N = 100;                % liczba graczy
teren = [0,0; 80, 70];  % prostokątny teren gry
fn = 2300;              % MHz
df = 5;                 % Mhz
Ptx = 100;              % mW
% jeżeli chcesz podać błąd pomiaru kąta w radianach użyj linii
% 17, a jeżli w stopniach użyj 18
dfi = 0.139626;    
%dif_st = 8; dif = dif_st/180*pi;                       


%% stałe
% zakładamy, że nadajniki są w narożnikach boiska
R1 = [teren(1,1), teren(1,2)];
R2 = [teren(2,1), teren(1,2)];
R3 = [teren(2,1), teren(2,2)];
R4 = [teren(1,2), teren(2,2)];

%% pozycje graczy
pos = rand([N,2]);
pos(:,1) = pos(:,1)*teren(2,1);
pos(:,2) = pos(:,2)*teren(2,2);
posnew = zeros(N,2);

dif = 0;
for k = 1:N
    %% obliczanie kątów
    alfa1 = atan((pos(k,1)-R1(1))/(pos(k,2)-R1(2)));
    alfa2 = atan((pos(k,1)-R2(1))/(pos(k,2)-R2(2)));
    alfa3 = atan((pos(k,1)-R3(1))/(pos(k,2)-R3(2)));
    alfa4 = atan((pos(k,1)-R4(1))/(pos(k,2)-R4(2)));

    %% mierzone kąty 
    % zakładamy, że kąt został zmierzony poprawnie z błędem +- dfi
    alfa1 = alfa1 + (rand*2-1)*dfi;
    alfa2 = alfa2 + (rand*2-1)*dfi;
    alfa3 = alfa3 + (rand*2-1)*dfi;
    alfa4 = alfa4 + (rand*2-1)*dfi;

    %% obliczanie pozycji na podstawie dystansu
    A = [1, -tan(alfa1); ...
         1, -tan(alfa2); ...
         1, -tan(alfa3); ...
         1, -tan(alfa4)];

    b = [R1(1) - R1(2)*tan(alfa1); ...
         R2(1) - R2(2)*tan(alfa2); ...
         R3(1) - R3(2)*tan(alfa3); ...
         R4(1) - R4(2)*tan(alfa4)];
    
    r = ( transpose(A) * A )^(-1) * transpose(A) * b;
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