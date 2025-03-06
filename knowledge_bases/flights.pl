flight(bogota, cartagena, 250, 9000, 0.0278).
flight(bogota, cartagena, 300, 6300, 0.0476).
flight(bogota, medellin, 200, 6300, 0.0317).
flight(bogota, medellin, 250, 5400, 0.0463).
flight(bogota, cali, 500, 10800, 0.0463).
flight(bogota, cali, 450, 9900, 0.0455).
flight(bogota, quibdo, 300, 9900, 0.0303).
flight(bogota, san_andres, 450, 10800, 0.0417).
flight(cartagena, pasto, 350, 8400, 0.0417).
flight(cartagena, pasto, 400, 7800, 0.0513).
flight(medellin, cali, 300, 5400, 0.0556).
flight(medellin, cali, 280, 6000, 0.0467).
flight(medellin, quibdo, 270, 6000, 0.0450).
flight(quibdo, cali, 350, 8100, 0.0432).
flight(quibdo, cali, 320, 7800, 0.0410).
flight(medellin, cartagena, 280, 7800, 0.0359).
flight(cartagena, medellin, 280, 7800, 0.0359).
flight(cali, pasto, 400, 7200, 0.0556).
flight(cali, pasto, 380, 8100, 0.0469).
flight(pasto, quibdo, 220, 6600, 0.0333).
flight(san_andres, cartagena, 350, 6300, 0.0556).
flight(san_andres, cartagena, 320, 7200, 0.0444).
flight(medellin, pasto, 320, 7200, 0.0444).
flight(medellin, pasto, 340, 8100, 0.0420).

connectionFlight(Origin, Destination, Connection) :-
    flight(Origin, Connection, _, _, _),
    flight(Connection, Destination, _, _, _).

shortestFlight(Origin, Destination, flight(Origin, Destination, Price, MinTime, W)) :-
    findall(flight(Origin, Destination, Price, Time, W),
            flight(Origin, Destination, Price, Time, W),
            Flights),
    sort(4, @=<, Flights, SortedFlights),
    SortedFlights = [flight(Origin, Destination, Price, MinTime, W) | _].

cheapestFlight(Origin, Destination, flight(Origin, Destination, MinPrice, Time, _)) :-
    findall(flight(Origin, Destination, Price, Time, _),
            flight(Origin, Destination, Price, Time, _),
            Flights),
    sort(3, @=<, Flights, SortedFlights),
    SortedFlights = [flight(Origin, Destination, MinPrice, Time, _) |_].


similarFlight(ReferenceFlight, Threshold, Flight) :-
    ReferenceFlight = flight(_, _, _, _, RefWeight),
    findall(Flight,
            (flight(O, D, P, T, W),
             Flight = flight(O, D, P, T, W),
             abs(W - RefWeight) =< Threshold),
            SimilarFlights).