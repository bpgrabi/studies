% Celem zadania jest rozkodowanie jak największej ilości wciśniętych
% symboli na wybieraku DTMF. Wybierak DTMF oddalał się od mikrofonu w
% czasie trwania testu, przez co jest coraz ciężej odkodować kolejne
% symbole. 

%% ------------------------------------------------------------------------
clear all; close all; clc;
% wszystkie ploty zostały zakomentowane

%% Dane
oryginal = "123456789*0#962861#46889*535569*347559#6609257394*91028548076330*5#0737772#"; %oryginalny ciąg znaków
[signal,fs] = audioread('challenge 2021.wav'); % plik dźwiękowy 
N  = length(signal);        % liczba probek


%% Tablica
Table = [   1,2,3;
            4,5,6;
            7,8,9;
            "*",0,"#"];
ftable = [697, 770, 852, 941, 1209, 1336, 1477];



%% Filtry
for i=1:7
    [filtr(i,:), bm(i,:), an(i,:)] = myfiltr(ftable(i), fs);
end

% Plot charakterystyki filtrów
% figure(1) 
% hold on;
% for i=1:7
%     plot(0:fs-1,20*log10(abs(filtr(i,:))));
% end
% xlim([500 1600]);
% ylim([-60 0]);
% grid;
% hold off;



%% Plot sygnału po filtracji
how_many_small = 0;

for che = 1:7
    filtered(che,:) = filter(bm(che,:), an(che,:), signal); %filtracja sygnału
    yupper(che,:) = (abs(lowpass(filtered(che,:), 10^(-4), fs))); %wygładzanie funkcji i wzięcie wartości bezwzględnej
%     Plot sygnału w czasie po przejściu przez dany filtr
%     Na początku mikrofon jest blisko, więc lepiej słychać = większa
%     amplituda sygnału. 
%     figure(che+1)
%     hold on;
%     plot(0:N-1,abs(yupper(che,:)));
%     hold off;
end

%% proces decyzyjny

count = 1;
poss = 1;
step = fs/10;   % ilość próbek w 0.1s

number = '0'; 
    
while (poss<N-step)

    % do V przypisujemy średnią wartość amplitudy sygnału w określonej 
    % chwili w czasie (poss:poss+step) po przejściu
    % przez filtry pasmowo-przepustowe o częstotliwościach pasmowych
    % równych pionowej części DTMF
    V = [mean(yupper(1,poss:poss+step)), mean(yupper(2,poss:poss+step)), mean(yupper(3,poss:poss+step)), mean(yupper(4,poss:poss+step))];
    
    % to samo co dla V tylko pozioma część DTMF
    H = [mean(yupper(5,poss:poss+step)), mean(yupper(6,poss:poss+step)), mean(yupper(7,poss:poss+step))];

    % wybieramy najmocniejszą częstotliwość pionową i poziomą (ich wartość
    % i indeks)
    [My, indey] = max(V);
    [Mx, index] = max(H);

    % wyliczamy szum po przez zsumowanie wszystkich "kanałów"
    noise = sum(V) + sum(H);
    % i odjęcie od wyniku najmocniejszych częstotliwości
    noise = noise - My - Mx;
    % przeskalowanie szumu dla lepszego wyniku
    noise = 2.3*noise;

    % jeśli iloczyn średnich amplitud wybranych częstotliwości jest większy
    % od wyznaczonego szumu, to można uznać, że klawisz, który odpowiada
    % tym częstotliwościom został wciśnięty
    if My*Mx > noise^2
        number(count) = Table(indey, index);
        count = count + 1;

        % przeskakujemy w czasie aż przycisk zostanie zwolniony, w celu
        % uniknięcia powielania danego symbolu (wciśnięcie symblu "1" przez
        % 1 sekundę, generowałoby co najmniej 9 "1" w wyniku)
        while(poss<N-step && mean(yupper(indey,poss:poss+step))+mean(yupper(index+4,poss:poss+step))>noise)
            poss = poss+step;
        end
    end
    poss = poss + step;
end

wynik = [number; oryginal];
display(wynik)
display('by Pater Bartłomiej')


%% funkcja filtru; można było użyć jakiegokolwiek innego filtru bandpass

function [X, bm, an] = myfiltr(fc, fs)

fmin = fc - 25;
fmax = fc + 25;
f = 0:fs-1;
w = 2*pi*f;

w1 = 2*fs * tan(pi*fmin/fs);
w2 = 2*fs * tan(pi*fmax/fs);

[bm, an] = butter(3, [w1, w2], 's');
[z,p,k]  = tf2zp(bm,an);        
[zd,pd,kd] = bilinear(z,p,k,fs);
pow  = exp(1i*w/fs);
bm = poly(zd);          
an = poly(pd);

Hd   = kd * polyval(bm, pow)./polyval(an, pow);
X    = Hd./max(Hd);

end
