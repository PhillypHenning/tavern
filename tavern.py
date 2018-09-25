import sys
import os
import logging

from tavern.patrons.shadowy_figure import load_check, monster_hunt, monster_appendix, monster_find
from tavern.backofhouse.database import create_all_database
from tavern.backofhouse.functions import setup_logging

setup_logging()
log = logging.getLogger(__name__)


def main(argv):
    try:
        if not argv[1]: return
        load_check()
        if argv[1] == 'monster': 
            if sys.argv[2] == 'list': 
                monster_appendix()
            elif sys.argv[2] == 'hunt' and sys.argv[3] != None: 
                monster_hunt(sys.argv[3])
            elif sys.argv[2] == 'find' and sys.argv[3] != None:
                if sys.argv[3] == 'cr':
                    monster_find(sys.argv[3], sys.argv[4])
                else:
                    log.error('unable to search by that criteria')
                monster_find(sys.argv[3])

        if argv[1] == 'setup': create_all_database()

    except Exception as e:
        log.error(e)
        raise e



if __name__ == '__main__':
    main(sys.argv)