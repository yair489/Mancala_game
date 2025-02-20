from enum import Enum

class Turn(Enum):
    ANOTHR = "another next"
    NEXT = "next player turn"
    CAPTURE = "Capture"




class Kalah:
    def __init__(self , holes , seedes):
        self.curr_player = 0
        self.seedes = seedes
        self.holes = holes
        self.kalah = [seedes]*(holes*2+2)
        self.kalah[6] = self.kalah[13] = 0
        self.player_one_home = holes
        self.player_two_home = holes*2 + 1

    def turn_option(self , hole):
        if self.curr_player == 0 and (0<= hole <= self.holes):
            if hole == self.holes:
                return Turn.ANOTHR
            elif self.kalah[hole] == 1:
                return Turn.CAPTURE

        if (self.curr_player == 1) and (self.holes < hole <= ((self.holes+1)*2)):
            if hole == (len(self.kalah)-1):
                return Turn.ANOTHR
            elif self.kalah[hole] == 1:
                return Turn.CAPTURE

        return Turn.NEXT

    def next_turn(self ,  hole):
        res = self.turn_option(hole)
        if res == Turn.NEXT:
            self.curr_player = (self.curr_player + 1) % 2
        if res == Turn.CAPTURE:
            # return Turn.CAPTURE
            self.kalah[hole] = 0
            num_holes_minus = 0 if self.curr_player == 0 else hole
            hole_next_player = (self.holes*2) - num_holes_minus
            num_seeds_next_player = self.kalah[hole_next_player]
            self.kalah[hole_next_player] = 0
            if self.curr_player:
                self.kalah[len(self.kalah)-1] += 1 + num_seeds_next_player
            else:
                self.kalah[self.holes] += 1 + num_seeds_next_player
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
                curr_hole = (curr_hole + 1) % len(self.kalah)
            self.kalah[curr_hole] += 1
            i += 1

        self.next_turn( curr_hole)
        return "Tie"

    def status(self):
        return tuple(self.kalah)

    def done(self):
        return True

    def score(self):
        return [0,0]

    def others_house(self , hole):
        if (self.curr_player == 0) and (hole == len(self.kalah)-1):
            return True
        if (self.curr_player ) and ( hole == self.holes ):
            return True
        return False