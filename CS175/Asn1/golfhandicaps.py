# golfhandicaps.py
# Reads a file containing players' scores, calculates their handicaps,
# and prints the handicap of each player that has played the required
# minimum number of games
#
# Copyright 2011, Mark Tupala.
# All rights reserved.
#
# Created: Mark Tupala (tupala@ualberta.ca)

import sys
from math import ceil

NUM_HOLES = 18
MIN_GAMES = 20
NUM_GAMES = 10
MAX_SCORE = 10

class Player(object):
    def __init__(self, name, par):
        self.name = name.strip()
        self.par = par
        self.scores = []
        self.qualifies = False
    
    def calc_handicap(self):
        if len(self.scores) >= MIN_GAMES: self.qualifies = True
        else: return
        
        self.clean_data()
        self.get_avg()
    
    # changes any scores above MAX_SCORE to MAX_SCORE
    def clean_data(self):
        for game in range(len(self.scores)):
            for hole in range(NUM_HOLES):
                if self.scores[game][hole] > MAX_SCORE: 
                    self.scores[game][hole] = MAX_SCORE
    
    # calculates the score (strokes - par) for every game, sorts them,
    # and calculates the average for the top NUM_GAMES games
    def get_avg(self):
        game_scores = [sum(scores) for scores in self.scores]
        game_scores.sort()
        top_scores = game_scores[:NUM_GAMES]
        self.handicap = ceil(sum(top_scores) / NUM_GAMES - self.par)
    
    def print_output(self):
        print(self.name, ':', sep='', end=' ')
        if not self.qualifies:
            print('Needs to play more golf!')
        elif self.handicap <= 0:
            print('Scratch')
        else:
            print(self.handicap)


if __name__ == "__main__":
    # get the file name, open it, read it into a list of strings, then close
    file_name = sys.argv[1]
    infile = open(file_name, 'r')
    lines = infile.readlines()
    infile.close()
    
    # par is the sum of all of the numbers on the first line
    par = sum([int(strokes) for strokes in lines[0].split()[1:]])
    
    # iterate over all of the lines. If you read a blank, the next line will
    # be a player's name, and the next will be his/her score
    players = {}
    ii = 1
    num_lines = len(lines)
    while ii < num_lines:
        line = lines[ii].strip()
        if not line: ii += 1
        else:
            name = line
            if name not in players:
                players[name] = Player(name, par)
            ii += 1
            players[name].scores.append(
                [int(strokes) for strokes in lines[ii].split()])
            ii += 1
    
    # iterate over all of the players, calculating their handicap
    # and printing it
    for player in players:
        players[player].calc_handicap()
        players[player].print_output()