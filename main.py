from pandas import read_csv
from BloonSend import BloonSend


def run():
    bloon_data = read_csv('bloon_data.csv').values

    # An array that contains BloonSend objects pulled from the CSV
    sends = []

    # Takes the bloon data and converts it in BloonSend objects.
    for traits in bloon_data:
        bloon_stats = BloonSend(traits[0], traits[1], traits[2], traits[3], traits[5])
        sends.append(bloon_stats)

    sends[5].graph_payoff_time()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


