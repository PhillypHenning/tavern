import sys
import os
import logging

from tavern.patrons.monster_hunter import load_check, monster_hunt, monster_appendix, prepare_monster_appendix, document_monster
from tavern.backofhouse.database import prepare_databases, clean_databases
from tavern.backofhouse.functions import setup_logging
import tavern.backofhouse.storeroom.settings as settings

setup_logging()
log = logging.getLogger(__name__)


def main(argv):
    #TODO usage
    usage="""
    python tavern.py <command>
    
    COMMAND OPTIONS
    tavern.py monster list - list all monsters. Returns json object.
    tavern.py monster hunt <creature name> - looks through data for matching monster
    tavern.py monster prep - **TO REMOVE LATER** prepare script
    tavern.py monster doc - add monster to data
    """
    try:
        if argv[1] == 'monster': 
            if argv[2] == 'list': 
                monster_appendix()
            elif argv[2] == 'hunt' and argv[3] != None:
                monster_hunt(argv[3])
            elif argv[2] == 'doc':
                print('testing doc')
                document_monster()
            else:
                print(usage)

        elif argv[1] == 'setup': 
            if settings.FULL_CLEAN: clean_databases()
            else: print('skipping')
            prepare_databases()


        else:
            print(usage)

    except ValueError as e:
        print(usage)
        log.error(e)
    
    except IndexError as e:
        print(usage)
        log.error('Parameter out of bounds. [{}]'.format(e))


if __name__ == '__main__':
    main(sys.argv)