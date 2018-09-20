import sqlite3


def create_database(database):
    print('creating database: [{}]'.format(database))
    conn = sqlite3.connect('{}.db'.format(database))
    c = conn.cursor()
    # TODO

def create_all_database():
    dn = '5e-database/'
    af = os.listdir(dn)
    print('checking folder: [{}], found: [{}]'.format(dn, af))

