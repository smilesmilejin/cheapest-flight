import heapq
from typing import List
from collections import defaultdict


def cheapest_flight(cities: int, flights: List[List[str]], source: str,
                    dest: str, max_layovers: int) -> int:
    # Please note: the following commented-out code is an alternative to the method used below with the
    # adjacency dictionary. In order for the adjacency matrix implementation to work,
    # the nested for loop on line 52 will need to be altered as well.
    # ------
    # # turn the list of edges into an adjacency matrix to make it easier to perform Dijkstra's
    # adjacency_matrix = [[0] * cities for _ in range(cities)]

    # # for each node in flights
    # # set the cost of the edge from the departure_city to the arrival_city as the flight_cost
    # # a cost of 0 indicates there is no flight from departure_city to arrival_city
    # for departure_city, arrival_city, flight_cost in flights:
    #     adjacency_matrix[departure_city][arrival_city] = flight_cost

    # This statement and the one below ensure we can avoid a KeyError when appending to our dictionaries
    adjacency_list = defaultdict(list)
    visited = defaultdict(bool)
                        
    for departure_city, arrival_city, flight_cost in flights:
        adjacency_list[departure_city].append((flight_cost, arrival_city))
        visited[departure_city] = False

    #Initialize our priority queue with the source city
    # We pass in a tuple where the 0th element is the price to get from source to arrival_city
    # the 1st element is the number of layovers we can still use
    # set initial amount of possible layovers to max_layovers + 1 to account for destination city
    # the 2nd element is the arrival_city
    pq = []
    heapq.heappush(pq, (0, max_layovers+1, source))

    while pq:
        #pop the cheapest city off the queue
        current_price, layovers_left, current_city = heapq.heappop(pq)

        #if the city we are visiting is the destination city
        if current_city == dest:
            #return the price to get to that city
            return current_price
            
        #Add city to visited dictionary
        visited[current_city] = True

        #If we can add another flight
        if layovers_left > 0:
            #loop through the connecting flights from our current city
            for cost_to_neighbor, neighbor in adjacency_list[current_city]:
                #if we have not yet been to that city
                if not visited[neighbor]:
                    #add the city to the queue
                    # set its price equal to the cost to get to the current city + the cost of the flight from currente city to neighboring city
                    # decrease number of layovers left by one
                    heapq.heappush(pq, (current_price + cost_to_neighbor, layovers_left - 1, neighbor))
    return -1

