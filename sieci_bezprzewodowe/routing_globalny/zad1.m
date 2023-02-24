% Celem zadania jest znalezienie trasy od węzła startowego do węzła
% docelowego z wykorzystaniem greedy routingu i wyrysowanie jej. 
% Położenie węzłów jest losowane, położenie węzła startowego i doecelowego
% jest na sztywno ustawione w danych wejściowych (można zmienić).
% Czerwona linia na grafice służy tylko do zobrazowanie połączenia w lini 
% prostej od węzła startowego do docelowego.
% Zielonia linia obrazuje trasę od węzła startowego do węzła docelowego lub
% do najdalszego węzła, do którego udało się wyznaczyć trasę.
% Jeżeli konice lini czerwonych i zielonych się pokrywają, oznacza, że
% udało się wyznaczyć trasę.
% Niebieskimi liniami połączono węzły, które są w swoim zasięgu. 

%% ------------------------------------------------------------------------
clear all; close all; clc

%% dane wejściwoe
fc = 3;             % częstotliwość w GHz
rx_power = -85;     % czułość odbiornika w dBm
tx_power = 8;       % moc nadajnika w mW
sis = 5;            % średnia ilość sąsiadów - główna zmienna
N = 101;            % ilość czujników
no_try = 10;        % ilość prób
S = [50,20];        % współrzędne punktu startowego
D = [262,201];      % współrzedne punktu docelowego

%% obliczanie powierzchni
d = 10.^((10*log10(tx_power) - rx_power - 50)/25); % promień zasięgu nadajników
area = pi*d.^2/sis*N;
square = floor(sqrt(area));

%% symulowanie sieci
succes = 0;
for qwe = 1:no_try
    other_pos = [S; rand(N-2, 2) * square; D];
    % zobrazowanie sieci
    figure
    hold on
    rectangle("Position",[0 0 square square])
    plot(other_pos(:,1) ,other_pos(:,2), "*r")
    plot(S(1), S(2), ".g")
    plot(D(1), D(2), ".g")
    
    
    %% sprawdzanie ilości sąsiadów
    neig = zeros(N);   % macierz sąsiedztwa
    for k = 1:(N)
        for l = 1:(N)
            x = other_pos(k,:);
            y = other_pos(l,:);
            dystance = sqrt((x(1)-y(1)).^2 + (x(2)-y(2)).^2);
            if dystance < d
                neig(k,l) = 1;
                line([x(1) y(1)], [x(2) y(2)])
            end
        end
    end
    num_neig = 0;
    for k = 1:(N-2)
        num_neig = num_neig + sum(neig(k,:)); 
    end

    %disp(num_neig/(N-2)) % wyświetlenie realnej średniej liczby sąsiadów

    %% routing
    pack_poss = S;
    node = 1;
    while pack_poss ~= D
        min_dystance = [1 sqrt(2)*D(1)];
        for l = 1:N
            if neig(node,l)==1
                dystance = sqrt(((other_pos(l,1)-other_pos(end,1)).^2 + (other_pos(l,2)-other_pos(end,2)).^2));
                if dystance < min_dystance(2)
                    min_dystance = [l, dystance];
                end
            end
        end
        node = min_dystance(1);
        old_pack_poss = pack_poss;
        pack_poss = other_pos(node,:);
        if pack_poss == old_pack_poss
            break
        end
        line([pack_poss(1) old_pack_poss(1)], [pack_poss(2), old_pack_poss(2)], "Color", "g")
    end
    
    if pack_poss == D
        succes = succes + 1;
    end
    line([S(1) D(1)], [S(2) D(2)], 'Color', 'r')
end
fprintf("Udało się odnaleźć trasę dla %d z %d różnych wariantów\n", [succes, no_try])
