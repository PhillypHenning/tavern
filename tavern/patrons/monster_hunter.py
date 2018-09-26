import requests
import json
import logging
from ..backofhouse.storeroom import settings
from ..backofhouse.functions import setup_logging, calc_mod

log = logging.getLogger(__name__)


"""
MONSTER FIELDS
dexterity | wisdom_save | intelligence | actions | hit_dice
damage_resistances | speed | alignment | size | index | strength
constitution | languages | source | charisma | armor_class
condition_immunities | damage_vulnerabilities | senses | wisdom 
challenge_rating | special_abilities | name | url | type
damage_immunities | subtype | hit_points
"""


##########
# VERIFY #
##########
def load_check():
    try:
        with open('5e-json/5e-SRD-Monsters.json') as f:
            data = json.load(f)
        return True

    except ValueError as e:
        log.error('LOAD-CHECK FAILED')
        raise e


###########
# PREPARE #
###########
def prepare_monster_appendix():
    try:
        # HAS POTENTIAL TO OVERWRITE CUSTOM ENTRIES TODO
        with open('5e-json/5e-SRD-Monsters.json', 'r') as f:
            data = json.load(f)

            for monster in data:
                if not monster['source']: monster['source'] = 'PHB'
            
        with open('5e-json/5e-SRD-Monsters.json', 'w') as f: 
            f.write(json.dumps(data))

    except ValueError as e:
        log.error(e)
        raise e


########
# LIST #
########
def monster_appendix():
    try:
        with open('5e-json/5e-SRD-Monsters.json') as f:
            data = json.load(f) 
            log.debug('-~-~-~-~-~-~-~-~-~')
            for i in data:
                monster = i['name'].lower()
                log.debug('monster found: [{}]'.format(monster))
            log.debug('-~-~-~-~-~-~-~-~-~')
            return data
    
    except ValueError as e:
        log.error(e)
        raise e


########
# FIND #
########
def monster_hunt(monster):
    if not monster: raise Exception('NO MONSTER SPECIFIED')
    # find monster in json
    try:
        log.info('hunting {}s'.format(monster.lower()))
        with open('5e-json/5e-SRD-Monsters.json') as f:
            data = json.load(f)
            mn_fnd = None

            for i in data:
                monster = monster.lower()
                mn_srch = i['name'].lower()
                if monster == mn_srch:
                    log.info('prey found: [{}]'.format(monster))
                    log.debug('***********************')
                    log.debug('found: [{}]'.format(mn_srch))
                    log.debug('type: [{}], subtype: [{}], alignment: [{}] size:[{}]'.format(i['type'], i['subtype'], i['alignment'], i['size']))
                    log.debug('armor class: [{}]'.format(i['armor_class']))
                    log.debug('hit points: [{}]'.format(i['hit_points']))
                    log.debug('speed: [{}]'.format(i['speed']))
                    log.debug('-------')
                    # TODO MODIFIERS
                    log.debug('str: [{}]({}), dex: [{}]({}), con: [{}]({}), int:[{}]({}), wis:[{}]({}), cha:[{}]({})'.format(i['strength'], calc_mod(i['strength']), i['dexterity'], calc_mod(i['dexterity']), i['constitution'], calc_mod(i['constitution']), i['intelligence'], calc_mod(i['intelligence']), i['wisdom'], calc_mod(i['wisdom']), i['charisma'], calc_mod(i['charisma'])))
                    log.debug('-------')
                    log.debug('damage resistances: [{}]'.format(i['damage_resistances']))
                    log.debug('damage immunities: [{}]'.format(i['damage_immunities']))
                    log.debug('damage vulnerabilities: [{}]'.format(i['damage_vulnerabilities']))
                    log.debug('senses: [{}]'.format(i['senses']))
                    log.debug('languages: [{}]'.format(i['languages']))
                    log.debug('challenge rating: [{}]'.format(i['challenge_rating']))
                    log.debug('-------')
                    log.debug('Actions')
                    log.debug('-------')
                    for action in i['actions']:
                        log.debug('{}: {}'.format(action['name'], action['desc']))
                    for spec in i['special_abilities']:
                        log.debug('{}: {}'.format(spec['name'], spec['desc']))
                    log.debug('source: [{}]'.format(i['source']))
                    log.debug('***********************')

                    mn_fnd = mn_srch
                    continue
                        
                else:
                    pass

            if mn_fnd: return mn_fnd
            else: log.warning('UNABLE TO FIND MONSTER: [{}]'.format(mn_fnd))

    except ValueError as e:
        log.error(e)
        raise e


##########
# CREATE #
##########
def document_monster(monster):
    
    print('Adding monster')
    with open('5e-json/5e-SRD-Monsters.json', 'r') as f: 
        data = json.load(f)

        log.info('ADDING MONSTER: [{}]'.format(monster))

        print('type is: [{}]'.format(type(data)))
        data.append(monster)
    
    with open('5e-json/5e-SRD-Monsters.json', 'w') as f: json.dump(data, f)




##########
# DELETE #
##########
def remove_monster():
    pass


########
# EDIT #
########
def rewrite_monster():
    pass

