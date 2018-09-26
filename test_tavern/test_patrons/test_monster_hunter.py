import unittest
from tavern.patrons.monster_hunter import monster_appendix, monster_hunt, document_monster

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

    def test_monster_add(self):
        test_monster = {
            'name' : 'test',
            'type' : 'humanoid',
            'subtype' : 'goblin',
            'alignment' : 'neutral',
            'size' : 'small',
            'armor_class' : '11',
            'hit_dice' : 'd8',
            'hit_points': '19',
            'speed' : '30 ft.',
            'strength' : '12',
            'dexterity' : '12',
            'constitution' : '8',
            'intelligence' : '8',
            'wisdom' : '11',
            'charisma' : '12',
            'damage_resistances' : [],
            'damage_immunities' : [],
            'condition_immunities' : [],
            'damage_vulnerabilities' : [],
            'senses' : ['darkvision 60 ft'],
            'languages' : ['common', 'goblin'],
            'challenge_rating' : '1',
            'actions' : [{'name': '*Slap*'},{'desc': '*whap*'}],
            'special_abilities' : [{'name': ''}, { 'desc': ''}],
            'source' : 'CSTM_TEST',
            'url' : ''
        }

        document_monster(test_monster)
        self.assertIsNotNone(monster_hunt('test'))

