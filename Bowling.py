maxThrows = 21
maxFrames = 10
Score_Strike = 10
Score_Spare = 10


class Bowling:
    def __init__(self):
        self.ScArr = []

    def numberofThrows(self):
        return len(self.ScArr) + 1

    def scoreTwoThrows(self, index):
        return self.ScArr[index] + self.ScArr[index + 1] + self.ScArr[index + 2]

    def frameScore(self, index):
        return self.ScArr[index] + self.ScArr[index + 1]

    def throw(self, pins):
        if self.numberofThrows() > maxThrows:
            raise ValueError
        self.ScArr.append(pins)

    def score(self):
        score = 0
        throw = 0
        frame = 0
        while frame < maxFrames:
            if self.ScArr[throw] == Score_Strike:
                score += self.scoreTwoThrows(throw)
                throw += 1
            elif self.ScArr[throw] == Score_Spare:
                score += self.scoreTwoThrows(throw)
                throw += 2
            else:
                score += self.frameScore(throw)
                throw += 2

            frame = frame + 1
        return score
