import HW04aFS
import unittest
from unittest import mock

class TestRepCommit(unittest.TestCase):
    @mock.patch('requests.get')
    def test_repo_commit(self,mockapi):
        mockapi.return_value.json.return_value = ([{"gh":1,"name":"repo_a"},{"gh":2,"name":"repo_b"}])
        self.assertEqual(2, len(HW04aFS.rep_comm("fs412")))
        self.assertEqual(2, HW04aFS.rep_comm("fs412").get("repo_a"))
        self.assertEqual(2, HW04aFS.rep_comm("fs412").get("repo_b"))

if __name__ == '__main__':
        unittest.main(exit=False, verbosity=2)