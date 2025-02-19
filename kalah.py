class Kalah:
    def __init__(self , holes , seedes):
        self.curr_player = 0
        self.seedes = seedes
        self.holes = holes
        self.kalah = [seedes]*(holes*2+2)
        self.kalah[6] = self.kalah[13] = 0

    def next_turn(self ,  hole):
        if (self.curr_player and hole == (len(self.kalah) - 1)) or (self.curr_player == 0 and hole == 6):
            return
        self.curr_player = (self.curr_player + 1) % 2

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
        for i in range(seeds):
            curr_hole = (hole+1+i)%len(self.kalah)
            self.kalah[curr_hole] += 1
        self.next_turn( curr_hole)
        return "Tie"

    def status(self):
        return tuple(self.kalah)

    def done(self):
        return True

    def score(self):
        return [0,0]