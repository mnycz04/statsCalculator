"""
Contains all the functions for the calculator
"""


def find_mean(events_list):
    """Finds the mean of given events list"""

    mean_of_events = 0

    for cur_event in range(len(events_list)):
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
