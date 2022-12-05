from pandas import read_csv


# this was a lot more complicated, but i simplified it a lot
def load_cluster_data():
    return read_csv('resources/cluster_data.csv').values


def load_round_data():
    return read_csv('resources/round_data.csv').values


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