from gui.app_interface import AppInterface
from simulator import Simulator
from kivy.lang import Builder


def run():
    # sim = Simulator()
    # # # #
    # #
    # sim.send_cluster(4)
    # sim.send_cluster(4)
    # sim.round_info(3)
    AppInterface().run()


    # # an example of how you
    # bl = sim.bloon_data[3]
    # print(sim.bloon_data[3].info)
    #
    # # bl.graph_payoff_time()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


