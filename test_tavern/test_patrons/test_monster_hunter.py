import unittest
from tavern.patrons.monster_hunter import monster_appendix, monster_hunt

class TestMonsterHunter(unittest.TestCase):

    def test_monster_appendix(self):
        ok = False
        if monster_appendix(): ok = True
        self.assertTrue(ok)

    def test_monster_hunt_found(self):
        ok = False
        monster = monster_hunt(monster='zombie')
        self.assertIsNotNone(monster)
    
    def test_monster_hunt_not_found(self):
        ok = False
        monster = monster_hunt(monster='zomie')
        self.assertIsNone(monster)