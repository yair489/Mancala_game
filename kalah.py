class Kalah:
    def __init__(self , holes , seedes):
        self.seedes = seedes
        self.holes = holes
        self.kalah = [seedes]*(holes*2+2)
        self.kalah[6] = self.kalah[13] = 0


    def  play(self , hole):
        if hole<0 or hole > 11:
            raise IndexError
        # if self.seedes == 0 raise Value erir
        seeds = self.kalah[hole]
        self.kalah[hole] = 0
        for i in range(seeds):
            self.kalah[hole+1+i] += 1
        return "Tie"

    def status(self):
        return tuple(self.kalah)

    def done(self):
        return True

    def score(self):
        return [0,0]