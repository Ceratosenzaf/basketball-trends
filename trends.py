from data import *
import numpy as np
import matplotlib.pyplot as plt


def draw_player(scope, player, color = None, line = '-'):
    plt.plot(scope, label = player, c = color, ls = line)


if __name__ == "__main__":
    # add player to chart
    for player in Players:
        draw_player(Salary[Pdict[player]], player)

    # add legend to chart with its upper left corner to 1,1
    plt.legend(loc = 'upper left', bbox_to_anchor =  (1,1))

    # add seasons label
    plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical')

    #visualize graph
    plt.show()