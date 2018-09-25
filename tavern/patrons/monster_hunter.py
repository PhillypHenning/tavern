import requests
import json
import logging
from ..backofhouse.storeroom import settings
from ..backofhouse.functions import setup_logging

log = logging.getLogger(__name__)


##########
# VERIFY #
##########
def load_check():
    try:
        with open('5e-database/5e-SRD-Monsters.json') as f:
            data = json.load(f)
    except Exception:
        log.error('LOAD-CHECK FAILED')
        raise e
    return True


########
# LIST #
########
def monster_appendix():
    try:
        with open('5e-database/5e-SRD-Monsters.json') as f:
            data = json.load(f) 
            log.debug('-~-~-~-~-~-~-~-~-~')
            for i in data:
                monster = i['name'].lower()
                log.debug('monster found: [{}]'.format(monster))
            log.debug('-~-~-~-~-~-~-~-~-~')
        return True
    
    except Exception as e:
        log.error(e)
        raise e


########
# FIND #
########
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
                    log.debug('***********************')
                    log.debug('found: [{}]'.format(mn_srch))
                    log.debug('subtype: [{}], alignment: [{}] size:[{}]'.format(i['subtype'], i['alignment'], i['size']))
                    log.debug('armor class: [{}]'.format(i['armor_class']))
                    log.debug('hit points: [{}]'.format(i['hit_points']))
                    log.debug('speed: [{}]'.format(i['speed']))
                    log.debug('-------')
                    # TODO MODIFIERS
                    log.debug('str: [{}](), dex: [{}](), con: [{}](), int:[{}](), wis:[{}](), cha:[{}]()'.format(i['strength'], i['dexterity'], i['constitution'], i['intelligence'], i['wisdom'], i['charisma'],))
                    log.debug('-------')
                    log.debug('damage resistances: [{}]'.format(i['damage_resistances']))
                    log.debug('damage immunities: [{}]'.format(i['damage_immunities']))
                    log.debug('damage vulnerabilities: [{}]'.format(i['damage_vulnerabilities']))
                    log.debug('senses: [{}]'.format(i['senses']))
                    log.debug('lamnguages: [{}]'.format(i['languages']))
                    log.debug('challenge rating: [{}]'.format(i['challenge_rating']))
                    log.debug('-------')
                    log.debug('Actions')
                    log.debug('-------')
                    for action in i['actions']:
                        log.debug('{}: {}'.format(action['name'], action['desc']))
                    for spec in i['special_abilities']:
                        log.debug('{}: {}'.format(spec['name'], spec['desc']))
                    log.debug('***********************')

                    monster = mn_srch[i]
                    continue
                        
                else:
                    pass

            print(type(monster))

    except Exception as e:
        raise e



