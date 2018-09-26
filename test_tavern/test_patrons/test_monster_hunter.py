import unittest
from tavern.patrons.monster_hunter import monster_appendix, monster_hunt

class TestMonsterHunter(unittest.TestCase):

    def test_monster_appendix(self):
        ok = False
        if monster_appendix(): ok = True
        self.assertTrue(ok)

    def test_monster_hunt(self):
        ok = False
        monster = monster_hunt(name='zombie')