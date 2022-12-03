from simulator import Simulator


def run():
    sim = Simulator()

    sim.round_info(4)

    # an example of how you
    bl = sim.bloon_data[3]
    print(sim.bloon_data[3].info)

    # bl.graph_payoff_time()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
