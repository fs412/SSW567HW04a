from HW04aFS import rep_comm
import unittest

class TestRepCommit(unittest.TestCase):
    def test_rep_commit(self):
        self.assertEqual(4, len(rep_comm("fs412")))
        self.assertEqual(1, rep_comm("fs412").get("helloworld"))
        self.assertIsNone(rep_comm("fs412").get("doesntexist"))

if __name__ == '__main__':
        unittest.main(exit=False, verbosity=2)