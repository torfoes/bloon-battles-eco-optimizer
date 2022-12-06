import matplotlib.pyplot as plt
from file_loader import *
import time


class Cluster:
    data = []  # SICK AS SHIT CLASS VARIABLE - avoids having to read in all the data and file each instance

    def __init__(self, bloon_id, **kwargs):
        self.id = bloon_id


        self.regrow = kwargs.get("regrow", False)
        self.camo = kwargs.get("camo", False)
        self.fortified = kwargs.get("fortified", False)
        self.grouped = kwargs.get("grouped", False)

        Cluster.data = load_cluster_data()

        self.name = self.data[bloon_id][0]
        self.num = self.data[bloon_id][1]
        self.cost = self.data[bloon_id][2]
        self.eco = self.data[bloon_id][3]
        self.delay = self.data[bloon_id][7]

    def info(self):
        try:
            print("Type {}: \nNumber: {}\nCost: {}\nEco Boost: {}\nSend Delay: {}".format(self.type,
                                                                                          self.num,
                                                                                          self.cost,
                                                                                          self.eco,
                                                                                          self.delay))

        except Exception:
            print("What the fuck dumbass")

    def send_individual(self):
        for i in range(self.num):

            time.sleep(self.delay/self.eco)

    # def graph_payoff_time(self):
    #     print(self.delay)
    #     x = []
    #     y = []
    #
    #     debt = -self.cost
    #     rounds_passed = 0
    #
    #     while debt < 0:
    #         x.append(compounding_freq * rounds_passed)
    #         y.append(debt)
    #
    #         rounds_passed += 1
    #
    #         x.append(compounding_freq * rounds_passed)
    #         y.append(debt)
    #
    #         debt += rounds_passed * self.eco
    #
    #     plt.plot(x, y)
    #
    #     plt.xticks(x)
    #     plt.xlabel('Time Passed')
    #     plt.ylabel('Debt')
    #     plt.title('{} payoff time'.format(self.type))
    #     plt.show()
