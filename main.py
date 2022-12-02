from pandas import read_csv
from BloonSend import BloonSend
from RoundSimulator import RoundSimulator


def run():
    bloon_data = read_csv('bloon_data.csv').values

    # this is just making sure that i can open monkey_data.py
    # monkey_data = read_csv('monkey_data.csv').values
    # print(monkey_data)

    # An array that contains BloonSend objects pulled from the CSV
    sends = []

    # Takes the bloon data and converts it in BloonSend objects.
    for traits in bloon_data:
        bloon_stats = BloonSend(traits[0], traits[1], traits[2], traits[3], traits[7])
        sends.append(bloon_stats)


    # Demonstrates a function that the BloonSend function may have
    sends[14].graph_payoff_time()

    #x = RoundSimulator()
    # gives information about the input round
    #x.round_info(3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


