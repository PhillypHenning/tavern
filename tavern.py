import sys
import os

from tavern.patrons.shadowy_figure import load_check, monster_hunt
from tavern.backofhouse.database import create_all_database

def main(argv):
   #if load_check(): print('check failed, exiting.')

    if not argv[1]: return
    load_check()
    try:
        if argv[1] == 'monster': monster_hunt(sys.argv[2])
        if argv[1] == 'setup': create_all_database()
        
    except Exception:
        pass



if __name__ == '__main__':
    main(sys.argv)