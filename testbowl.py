import unittest as ut
import Bowling


class TestBowling(ut.TestCase):

    def setUp(self):
        self.bowl = Bowling.Bowling()

    def testforgutter(self):
        for i in range(20):
            self.bowl.throw(0)

        assert self.bowl.score() == 0, " zero score"

    def testscore_one_is20(self):
        for i in range(20):
            self.bowl.throw(1)

        assert self.bowl.score() == 20

    def testThrowsForMoreThanTwentyOneRolls(self):
        try:
            for i in range(22):
                self.bowl.throw(10)
        except ValueError:
            pass
        else:
            self.fail("Expected a ValueError")

    def testBowlforOneStrike(self):
        self.bowl.throw(10)
        self.bowl.throw(1)
        self.bowl.throw(1)

        for i in range(17):
            self.bowl.throw(0)

        assert self.bowl.score() == 14

    def testPerfectGameScores300(self):
        for i in range(12):
            self.bowl.throw(10)

        assert self.bowl.score() == 300, "Perfect Game should score 300"

    if __name__ == "__main__":
        ut.main()
