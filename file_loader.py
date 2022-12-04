from pandas import read_csv
from classes.bloon_send import BloonSend


def load_bloon_data():
    # An array that contains BloonSend objects pulled from the CSV
    bloon_data = read_csv('resources/bloon_data.csv').values
    sends = []

    # Takes the bloon resources and converts it in BloonSend objects.
    for traits in bloon_data:
        bloon = BloonSend(traits[0], traits[1], traits[2], traits[3], traits[7])
        sends.append(bloon)

    return sends


# def load_round_data():
#     # An array that contains BloonSend objects pulled from the CSV
#     bloon_data = read_csv('resources/bloon_data.csv').values
#     sends = []
#
#     # Takes the bloon resources and converts it in BloonSend objects.
#     for traits in bloon_data:
#         bloon = BloonSend(traits[0], traits[1], traits[2], traits[3], traits[7])
#         sends.append(bloon)
#
#     return sends


# def load_monkey_data():
#     # An array that contains BloonSend objects pulled from the CSV
#     monkey_data = read_csv('resources/tower_data.csv').values
#     monkeys = []
#
#     # Takes the bloon resources and converts it in BloonSend objects.
#     for monkey in monkey_data:
#         bloon = BloonSend(traits[0], traits[1], traits[2], traits[3], traits[7])
#         towers.append(bloon)
#
#     return towers