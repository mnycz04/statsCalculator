"""
# A Calculator for common AP Stats Problems
"""

__author__ = 'Michael Nycz'
__version__ = '1.0'


def find_mean(events_list):
    """Finds the mean of given events list"""
    mean_of_events = 0

    for cur_event in range(len(events)):
        mean_of_event = events_list[cur_event][0] * events_list[cur_event][1]
        mean_of_events += mean_of_event

    return round(mean_of_events, 5)


def find_variance(mean, event_list):
    """Finds the variance of the events"""

    variance = 0

    for j in range(len(event_list)):
        current_variance = ((event_list[j][0] - mean) ** 2) * event_list[j][1]
        variance += current_variance

    return round(variance, 5)


while 1:
    points = input("Enter the number of events: ")
    try:
        points = int(points)
        if points <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a integer number, greater than 0:")
        continue

    events_base = []

    try:
        for i in range(points):
            event = input(f'Input event {i + 1}: ')
            try:
                event = float(event)
            except ValueError:
                print('Invalid event. Please enter decimals only.')
                raise ValueError
            events_base.append(event)
    except ValueError:
        continue

    events_probabilities = []

    try:
        for i in range(points):
            event_probability = input(f'Input the probability of event {i + 1}: ')
            try:
                event_probability = float(event_probability)
            except ValueError:
                print('Invalid input. Please use only decimals.')
                raise ValueError
            events_probabilities.append(event_probability)
        if sum(events_probabilities) != 1.0:
            print(f'WARNING: Probabilities do not add to 1. Σ = {sum(events_probabilities)}')
    except ValueError:
        continue

    events = list(zip(events_base, events_probabilities))

    events_mean = find_mean(events)
    events_variance = find_variance(events_mean, events)
    events_std_deviation = round(events_variance ** .5, 5)

    print(f'\nMean = {events_mean}')
    print(f'Variance = {events_variance}')
    print(f'Standard Deviation  = {events_std_deviation}\n\n')
