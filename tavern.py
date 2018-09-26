import sys
import os
import logging

from tavern.patrons.monster_hunter import load_check, monster_hunt, monster_appendix, prepare_monster_appendix
from tavern.backofhouse.database import create_all_database
from tavern.backofhouse.functions import setup_logging

setup_logging()
log = logging.getLogger(__name__)


def main(argv):
    #TODO usage
    try:
        load_check()
        if argv[1] == 'monster': 
            if argv[2] == 'list': 
                monster_appendix()
            elif argv[2] == 'hunt' and argv[3] != None: 
                monster_hunt(argv[3])
            elif argv[2] == 'prep':
                prepare_monster_appendix()
                

        if argv[1] == 'setup': 
            # prepare_all
            create_all_database()

    except Exception as e:
        log.error(e)
        raise e



if __name__ == '__main__':
    main(sys.argv)