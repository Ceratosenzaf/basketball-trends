from data import Seasons,Sdict,Players,Pdict,Salary,Games,MinutesPlayed,FieldGoals,FieldGoalAttempts,Points
import numpy as np
import matplotlib.pyplot as plt


def draw_chart(scope):
    # add player to chart
    for player in Players:
        plt.plot(scope[Pdict[player]], label = player, c = None, ls = '-')

    # add legend to chart with its upper left corner to 1,1
    plt.legend(loc = 'upper left', bbox_to_anchor =  (1,1))

    # add seasons label
    plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical')

    #visualize graph
    plt.show()


if __name__ == "__main__":
    minutes_per_game = np.matrix.round(MinutesPlayed / Games, 2)
    field_goals_accuracy = np.matrix.round(FieldGoals / FieldGoalAttempts, 2)

    minutes_per_game[Pdict['DerrickRose']][Sdict['2012']] = field_goals_accuracy[Pdict['DerrickRose']][Sdict['2012']] = 0

    draw_chart(Salary)
    draw_chart(minutes_per_game)
    draw_chart(FieldGoals)
    draw_chart(field_goals_accuracy)
    draw_chart(Points)