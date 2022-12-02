from pandas import read_csv


class RoundSimulator:
    def __init__(self):
        self.round_data = read_csv('round_data.csv').values
        print(self.round_data, "\n")

    def round_info(self, num):
        try:
            print("Round {}: \nBloons: {}\nRound Length\nMin Time: {}\nMax Time: {}".format(num,
                                                                                            self.round_data[num][1],
                                                                                            self.round_data[num][2],
                                                                                            self.round_data[num][3],
                                                                                            self.round_data[num][4]))
        except Exception:
            print("What the fuck dumbass")

