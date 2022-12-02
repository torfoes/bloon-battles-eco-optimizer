import matplotlib.pyplot as plt
import pandas as pd

compounding_freq = 6


class BloonSend:
    def __init__(self, type, num, cost, eco_boost, send_delay):
        self.type = type
        self.num = num
        self.cost = cost
        self.eco_boost = eco_boost
        self.send_delay = send_delay


        DIFFICULTY_SCORE = 0

    def graph_payoff_time(self):
        print(self.send_delay)
        x = []
        y = []

        debt = -self.cost
        rounds_passed = 0

        while debt < 0:
            x.append(compounding_freq * rounds_passed)
            y.append(debt)

            rounds_passed += 1

            x.append(compounding_freq * rounds_passed)
            y.append(debt)

            debt += rounds_passed * self.eco_boost

        plt.plot(x, y)

        plt.xticks(x)
        plt.xlabel('Time Passed')
        plt.ylabel('Debt')
        plt.title('{} payoff time'.format(self.type))
        plt.show()
