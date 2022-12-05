from gui_launcher import MyApp
from simulator import Simulator


def run():
    sim = Simulator()

    sim.send_cluster(4)
    sim.round_info(3)

    MyApp().run()

    # # an example of how you
    # bl = sim.bloon_data[3]
    # print(sim.bloon_data[3].info)
    #
    # # bl.graph_payoff_time()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


