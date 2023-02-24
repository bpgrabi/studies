
%% ------------------------------------------------------------------------
clear all; close all; clc

%% dane wejściwoe
fc = 3; %częstotliwość w GHz
rx_power = -85; % czułość odbiornika w dBm
tx_power = 8; % moc nadajnika w mW
N = 101; % ilość czujników
no_try = 100; %ilość prób

sis_x = 0;
succes_y = 0;
for sis = 3:10
%% obliczanie powierzchni
d = 10.^((10*log10(tx_power) - rx_power - 50)/25); % promień zasięgu nadajników
area = pi*d.^2/sis*N;

% disp("promień i powierzchnia w m i m^2")
% disp(d)
% disp(area)

%% symulowanie sieci
S = [0,0];
D = [floor(sqrt(area)), floor(sqrt(area))];

succes = 0;
for qwe = 1:no_try
other_pos = [S; rand(N-2, 2) * D(1); D];


%% sprawdzanie ilości sąsiadów
neig = zeros(N);
for k = 1:(N)
    for l = 1:(N)
        x = other_pos(k,:);
        y = other_pos(l,:);
        dystance = sqrt((x(1)-y(1)).^2 + (x(2)-y(2)).^2);
        if dystance < d
            neig(k,l) = 1;
            %line([x(1) y(1)], [x(2) y(2)])
        end
    end
end

num_neig = 0;
for k = 1:(N-2)
    num_neig = num_neig + sum(neig(k,:)); 
end
%disp(num_neig/(N-2))

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
end

if pack_poss == D
    succes = succes + 1;
end
end

sis_x = [sis_x sis];
succes_y = [succes_y succes];
end

plot(sis_x(2:end), succes_y(2:end)/no_try*100)
title("Skuteczność odnajdywania trasy w zależności od średniej ilości sąsiadów")
