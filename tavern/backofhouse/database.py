import os
import os.path
import sqlite3
import logging
import pymongo
import json

import storeroom.settings as settings

log = logging.getLogger(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


def prepare_databases():
    if 'tavern-ledger-book' not in myclient.list_database_names():
        log.info('CREATING MONGODB [{}]'.format('tavern-ledger-book'))
        # TODO
    else:
        db = myclient['tavern-ledger-book']
        log.info('DB: [{}], COLLECTIONS: [{}]'.format(db, db.list_collection_names()))

        files = [f for f in os.listdir(os.path.join(settings.PROJECT_HOME, '5e-json')) if f.endswith('.json')]
        for fn in files:
            fn_p = fn
            fn = fn[7:-5].lower()
            if fn not in db.list_collection_names():
                log.info('CREATING COLLECTION: [{}]'.format(fn))
                with open(os.path.join(settings.PROJECT_HOME, '5e-json', fn_p), 'r') as f:
                    data = json.load(f)
                    
                    col = db['{}'.format(fn)]
                    col.insert_many(data)

                    log.info('CREATED COLLECTION: [{}]'.format(fn))

            else:
                log.debug('SKIPPING COLLECTION: [{}]'.format(fn))
    
    if check_all_databases(): return True
    return False

def check_all_databases():
    all_ok=False
    db = myclient['tavern-ledger-book']

    failures = []

    files = [f for f in os.listdir(os.path.join(settings.PROJECT_HOME, '5e-json')) if f.endswith('.json')]
    for fn in files:
        fn = fn[7:-5].lower()
        my_query = { }
        col = db[fn]
        res = col.find(my_query)
        if res: all_ok = True
        else: failures.append(fn)


    if not failures: return all_ok
    return False

def clean_databases():
    db = myclient['tavern-ledger-book']

    files = [f for f in os.listdir(os.path.join(settings.PROJECT_HOME, '5e-json')) if f.endswith('.json')]
    for fn in files:
        fn_p = fn
        fn = fn[7:-5].lower()

        log.warning('DROPPING COLLECTION: [{}]'.format(fn))
        col = db[fn]
        col[fn].drop()

        log.warning('PREPARING JSON')
        with open(os.path.join(settings.PROJECT_HOME, '5e-json', fn_p), 'r') as f:
            data = json.load(f)

            for entry in data:
                try:
                    entry.update({'source' : 'PHB'})
                except KeyError as e:
                    log.error('EXCEPTION WHILE PREPARING: [{}], EXCEPTION: [{}]'.format(fn, e))
                    raise e

        

    


