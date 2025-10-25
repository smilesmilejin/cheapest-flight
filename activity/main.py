import heapq
from typing import List
from collections import defaultdict

def cheapest_flight(cities, flights, source, dest, max_layovers):
    pass

    # Q: every city at least have one edge?

    # create a adj_dict
        # key will city, value will list of edges [(neighbor, price)]

    # create a distances_from_source dict to track the shortest price from source to current city
        # key will current cities, value will the price
        # the initial value will be float('inf')
    

    # create previous dict to track the previous city for shortedst path from source to current 
        # key will current city, value will be the preivou city
        # initial value will be None


    # create num_cities_from_source dict to track the number of cities from source to current
        # key will the current city, value will the number of cities 
        # source does not count 
        # if there is no layover, count = 0
        # if there is one layover, count = 1
        # initial value will be -1 

    # create a visited set to track visited cities

    # create a priority queue using heapq [(price, city)]


    # set up source_city in distances, previous, num_cities
    # in distances dict[source_city] = 0
    # num_cities_from_source[source_city] = 0

    # add the source_city to priority queue

    # while priority queue is not empty:
        # current city = pop the first element from queue
        # add current city to visited

        # for neighbor of current city
            # if neighbor is not visited
                # calculate distance = distanct[current] + distance
                # if calculate distance < distance[neighbor] and num_cities_from_source[current] < max_layovers + 1:
                    # distance[neighbor] = calculate distance
                    # previous[neighbor] = current
                    # num_cities_from_source += 1

                # add neighbor to the queue

    # if distance_from_source[destiantion] is inifity
        # return -1

    # return distance_from_source[destiantion]


    if not cities or not flights:
        return -1 
    
    adj_dict = {}
    distances_from_source = {}
    previous = {}
    num_cities_from_source = {}

    for source_city, destination_city, price in flights:
        if source_city not in adj_dict:
            adj_dict[source_city] = [(destination_city, price)]
        else:
            adj_dict[source_city].append((destination_city, price))

        if source_city not in distances_from_source:
            distances_from_source[source_city] = float('inf')
        if destination_city not in distances_from_source:
            distances_from_source[destination_city] = float('inf')

        if source_city not in previous:
            previous[source_city] = None
        if destination_city not in previous:
            previous[destination_city] = None

        if source_city not in num_cities_from_source:
            num_cities_from_source[source_city] = 0
        if destination_city not in num_cities_from_source:
            num_cities_from_source[destination_city] = 0

        

    # # {'Buffalo': [('Syracuse', 100)], 'Syracuse': [('NYC', 600), ('Rochester', 100)], 'Rochester': [('Buffalo', 100), ('NYC', 200)]}
    # print("adj_dict:", adj_dict)
    # # distances_from_source: {'Buffalo': inf, 'Syracuse': inf, 'NYC': inf, 'Rochester': inf}
    # print("distances_from_source:", distances_from_source)
    # # previous: {'Buffalo': None, 'Syracuse': None, 'NYC': None, 'Rochester': None}
    # print("previous:", previous)
    # # num_cities_from_source: {'Buffalo': 0, 'Syracuse': 0, 'NYC': 0, 'Rochester': 0}
    # print("num_cities_from_source:", num_cities_from_source)

    distances_from_source[source] = 0
    # num_cities_from_source[source] += 1

    # print('##### ')
    # print("distances_from_source:", distances_from_source)
    # # print("num_cities_from_source:", num_cities_from_source)

    visited = set()

    import heapq

    priority_queue = []
    heapq.heappush(priority_queue, (0, source))
    # print('priority_queue: ', priority_queue)

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)
        visited.add(current)

        neighbors = adj_dict.get(current, [])

        if not neighbors:
            continue

        for neighbor, neighbor_distance in neighbors:
            if neighbor not in visited:
                calculated_distance = distances_from_source[current] + neighbor_distance

                if calculated_distance < distances_from_source[neighbor] and num_cities_from_source[current] < max_layovers + 1:
                    distances_from_source[neighbor] = calculated_distance
                    previous[neighbor] = current
                    num_cities_from_source[neighbor] = num_cities_from_source[current] + 1

                heapq.heappush(priority_queue, (calculated_distance, neighbor))


    # print('######## After queue')
    # print("distances_from_source:", distances_from_source)
    # print("previous:", previous)
    # print("num_cities_from_source:", num_cities_from_source)

    if distances_from_source[dest] == float('inf'):
        return -1

    return distances_from_source[dest]

