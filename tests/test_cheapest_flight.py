from activity.main import cheapest_flight
import pytest

def test_empty_graph_returns_negative_one():
    # Arrange
    flights = []

    #Act
    answer = cheapest_flight(0, flights, 'Buffalo', 'Rochester', 1)

    #Assert
    assert answer == -1


def test_unconnected_route_returns_negative_one():
    #Arrange
    flights = [['Buffalo', 'NYC', 400], ['Rochester', 'Buffalo', 200]]
    #Act
    answer = cheapest_flight(3, flights, 'Buffalo', 'Rochester', 1)
    #Assert
    assert answer == -1


def test_connected_route_one_option():
    #Arrange
    flights = [['Buffalo', 'NYC', 400], ['NYC', 'Rochester', 200]]
    #Act
    answer = cheapest_flight(3, flights, 'Buffalo', 'NYC', 1)
    #Assert
    assert answer == 400


def test_required_layover_route_within_layover_limit():
    #Arrange
    flights = [['Buffalo', 'NYC', 400], ['NYC', 'Rochester', 200]]
    #Act
    answer = cheapest_flight(3, flights, 'Buffalo', 'Rochester', 1)
    #Assert
    assert answer == 600

def test_required_layover_route_outside_layover_limit():
    #Arrange
    flights = [['Buffalo', 'NYC', 400], ['NYC', 'Rochester', 200]]
    #Act
    answer = cheapest_flight(3, flights, 'Buffalo', 'Rochester', 0)
    #Assert
    assert answer == -1

def test_example_one_returns_700():
    #Arrange
    flights = [
        ['Buffalo', 'Syracuse', 100],
        ['Syracuse', 'NYC', 600],
        ['Rochester', 'Buffalo', 100],
        ['Rochester', 'NYC', 200],
        ['Syracuse', 'Rochester', 100]
    ]

    #Act
    answer = cheapest_flight(4, flights, 'Buffalo', 'NYC', 1)

    #Assert
    assert answer == 700

def test_example_two_returns_400():
    #Arrange
    flights = [
        ['Buffalo', 'Syracuse', 100],
        ['Syracuse', 'NYC', 600],
        ['Rochester', 'Buffalo', 100],
        ['Rochester', 'NYC', 200],
        ['Syracuse', 'Rochester', 100]
    ]

    #Act
    answer = cheapest_flight(4, flights, 'Buffalo', 'NYC', 3)

    #Assert
    assert answer == 400

def test_example_three_returns_negative_one():
    #Arrange
    flights = [
        ['Buffalo', 'Syracuse', 100],
        ['Syracuse', 'NYC', 600],
        ['Rochester', 'Buffalo', 100],
        ['Rochester', 'NYC', 200],
        ['Syracuse', 'Rochester', 100]
    ]

    #Act
    answer = cheapest_flight(4, flights, 'Buffalo', 'NYC', 0)

    #Assert
    assert answer == -1
