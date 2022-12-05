from file_loader import *
from game_entities.cluster import Cluster


class Simulator:
    def __init__(self):
        self.round_data = load_round_data()
        self.queue = []

        # while all of this is nice, there really isn't too much of a point till you have a renderer

    # i need a way to nicely pass the **kwargs through this function
    def send_cluster(self, bloon_id):
        x = Cluster(bloon_id, fortified=True)  # this is just a demo
        self.queue.append(x)
        # print(self.queue)

    def round_info(self, num):
        try:
            print("Round {}: \nBloons: {}\nRound Length\nMin Time: {}\nMax Time: {}".format(num,
                                                                                            self.round_data[num][1],
                                                                                            self.round_data[num][2],
                                                                                            self.round_data[num][3],
                                                                                            self.round_data[num][4]))
        except Exception:
            print("What the fuck dumbass.")

