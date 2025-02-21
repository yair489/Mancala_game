from enum import Enum
import streamlit as st

class Turn(Enum):
    ANOTHR = "another next"
    NEXT = "next player turn"
    CAPTURE = "Capture"
    WIN ="win player"




class Kalah:
    def __init__(self , holes , seedes):
        self.curr_player = 0
        self.seedes = seedes
        self.holes = holes
        self.kalah = [seedes]*(holes*2+2)
        self.kalah[6] = self.kalah[13] = 0
        self.player_one_home = holes
        self.player_two_home = holes*2 + 1
        self.winner = None


    def  play(self , hole):

        self.valid_play_hole(hole)

        seeds = self.kalah[hole]
        self.kalah[hole] = 0
        curr_hole = 0

        #
        i = 0
        while i  < seeds:

            curr_hole = (hole+1+i)%(len(self.kalah))
            if self.others_house(curr_hole):
                i += 1
                seeds += 1
                curr_hole = (hole+1+i)%(len(self.kalah))
            self.kalah[curr_hole] += 1
            i += 1

        self.next_turn( curr_hole)
        return "Tie"

    def status(self):
        return tuple(self.kalah)

    def done(self):
        return False if not self.winner else self.winner

    def score(self):
        return [self.kalah[self.player_one_home], self.kalah[self.player_two_home]]


    def __repr__(self):
        return f"Kalah({self.seedes}, {self.holes}, status={self.status()}, player={self.curr_player})"

    def render(self):
        """Return a text representation of the board."""
        p1_store = self.kalah[self.player_one_home]
        p2_store = self.kalah[self.player_two_home]
        p1_side = self.kalah[:self.holes]
        p2_side = self.kalah[self.holes + 1:self.player_two_home]

        board_str = f"P2 Store: {p2_store}\n"
        board_str += "\nP2: " + " | ".join(map(str, reversed(p2_side))) + "\n"
        board_str += "\nP1: " + " | ".join(map(str, p1_side)) + f"\nP1 Store: {p1_store}"
        return board_str

    def others_house(self , hole):
        if (self.curr_player == 0) and (hole == len(self.kalah)-1):
            return True
        if (self.curr_player ) and ( hole == self.holes ):
            return True
        return False
    def turn_option(self , hole):
        seeds_side = self.seedes * self.holes
        if (self.kalah[self.player_two_home] == seeds_side ) and (self.kalah[self.player_one_home] == seeds_side):
            self.winner = "Tie"
            return Turn.WIN

        if self.curr_player == 0 and (0<= hole <= self.holes):
            if self.kalah[self.player_one_home] > seeds_side:
                self.winner = "player one win"
                return Turn.WIN
            if sum(self.kalah[ : self.player_one_home]) == 0:
                self.winner = "player two win"
                return Turn.WIN
            if hole == self.player_one_home:
                return Turn.ANOTHR
            elif self.kalah[hole] == 1:
                return Turn.CAPTURE

        if (self.curr_player == 1) and (self.player_one_home < hole <= self.player_two_home):
            if self.kalah[self.player_two_home] > seeds_side:
                self.winner = "player two win"
                return Turn.WIN
            if sum(self.kalah[ self.player_one_home+1 :self.player_two_home]) == 0:
                self.winner = "player one win"
                return Turn.WIN
            if hole == (self.player_two_home):
                return Turn.ANOTHR
            elif self.kalah[hole] == 1:
                return Turn.CAPTURE

        return Turn.NEXT

    def next_turn(self ,  hole):
        res = self.turn_option(hole)
        if res == Turn.ANOTHR:
            return res
        elif res == Turn.WIN:
            return res

        elif res == Turn.CAPTURE:
            self.kalah[hole] = 0

            if self.curr_player == 1:
                self.kalah[len(self.kalah)-1] += 1 + self.kalah[len(self.kalah) - 2 -hole]
            else:
                self.kalah[self.holes] += 1 + self.kalah[len(self.kalah) - 2 -hole]
            self.kalah[len(self.kalah) - 2 - hole] =0

        self.curr_player = (self.curr_player + 1) % 2


        return res

    # [
    #     13[ 12 , 11, 10 , 9 ,8 ,7]
    #       [ 0  , 1 ,  2 , 3 ,4 ,5] 6
    # ]

    def valid_play_hole(self , hole):
        if self.curr_player == 0:
            if not (0<= hole < self.holes):
                raise IndexError(f"valid player must be between 0 and self.holes {hole}")
        else:
            if not self.holes < hole < len(self.kalah):
                raise IndexError
        if self.kalah[hole] == 0:
            raise ValueError
        return True

