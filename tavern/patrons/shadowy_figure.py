import requests
import json
import logging
from ..backofhouse.storeroom import settings
from ..backofhouse.functions import setup_logging

log = logging.getLogger(__name__)

def load_check():
    try:
        with open('5e-database/5e-SRD-Monsters.json') as f:
            data = json.load(f)
    except Exception:
        log.error('LOAD-CHECK FAILED')
        raise e
    return True


def monster_appendix():
    try:
        with open('5e-database/5e-SRD-Monsters.json') as f:
            data = json.load(f) 
            print('-~-~-~-~-~-~-~-~-~')
            for i in data:
                monster = i['name'].lower()
                print('monster found: [{}]'.format(monster))
            print('-~-~-~-~-~-~-~-~-~')
    
    except Exception as e:
        log.error(e)
        raise e


def monster_hunt(monster):
    if not monster: return
    # find monster in database
    try:
        log.info('hunting {}s'.format(monster.lower()))
        with open('5e-database/5e-SRD-Monsters.json') as f:
            data = json.load(f)

            for i in data:
                monster = monster.lower()
                mn_srch = i['name'].lower()
                if monster == mn_srch:
                    log.info('prey found: [{}]'.format(monster))
                    print('***********************')
                    print('found: [{}]'.format(mn_srch))
                    print('subtype: [{}], alignment: [{}] size:[{}]'.format(i['subtype'], i['alignment'], i['size']))
                    print('armor class: [{}]'.format(i['armor_class']))
                    print('hit points: [{}]'.format(i['hit_points']))
                    print('speed: [{}]'.format(i['speed']))
                    print('-------')
                    # TODO MODIFIERS
                    print('str: [{}](), dex: [{}](), con: [{}](), int:[{}](), wis:[{}](), cha:[{}]()'.format(i['strength'], i['dexterity'], i['constitution'], i['intelligence'], i['wisdom'], i['charisma'],))
                    print('-------')
                    print('damage resistances: [{}]'.format(i['damage_resistances']))
                    print('damage immunities: [{}]'.format(i['damage_immunities']))
                    print('damage vulnerabilities: [{}]'.format(i['damage_vulnerabilities']))
                    print('senses: [{}]'.format(i['senses']))
                    print('lamnguages: [{}]'.format(i['languages']))
                    print('challenge rating: [{}]'.format(i['challenge_rating']))
                    print('-------')
                    print('Actions')
                    print('-------')
                    for action in i['actions']:
                        print('{}: {}'.format(action['name'], action['desc']))
                        
                    for spec in i['special_abilities']:
                        print('{}: {}'.format(spec['name'], spec['desc']))
                    print('***********************')
                        
                    return monster
                else:
                    pass

    except Exception as e:
        raise e

def monster_find(by, value):
    if by not in ['cr']: raise Exception('UNPERMITTED SEARCH BY METHOD BY:[{}]'.format(by))

    if by == 'cr':
        monster_find_by_cr()

def test_test():
    pass
    #yeep

