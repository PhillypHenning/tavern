import requests
import json


def load_check():
    try:
        with open('5e-database/5e-SRD-Monsters.json') as f:
            data = json.load(f)
    
    except Exception:
        #logging to come
        raise e
    
    return True

def monster_hunt(monster):
    if not monster: return
    # find monster in database
    try:
        print('hunting {}s'.format(monster.lower()))
        with open('5e-database/5e-SRD-Monsters.json') as f:
            data = json.load(f)

            for i in data:
                monster = monster.lower()
                mn_srch = i['name'].lower()
                if monster == mn_srch:
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
                        
                    
                else:
                    #print('skipping: [{}]'.format(mn_srch))
                    pass

    except Exception as e:
        raise e
