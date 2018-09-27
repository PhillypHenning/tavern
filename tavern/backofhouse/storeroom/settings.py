import os
import os.path
import yaml


PROJECT_CONF = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_CONF, '..'))
PROJECT_BASE = os.path.abspath(os.path.join(PROJECT_ROOT, '..'))
PROJECT_HOME = os.path.abspath(os.path.join(PROJECT_BASE, '..'))
PROJECT_NAME = PROJECT_ROOT.split(os.sep)[-1]


if not os.path.isdir(os.path.join(PROJECT_CONF, 'freezer')): os.mkdir(os.path.join(PROJECT_CONF, 'freezer'))
TVRN_FREEZER = os.path.join(PROJECT_CONF, 'freezer')

fn = 'settings.yaml'
ab_fn = os.path.abspath(os.path.join(PROJECT_CONF, fn))
if not os.path.isfile(ab_fn):
    with open(dn, 'w') as f: f.write('---\n...\n')
TVRN_SETTINGS = yaml.load(open(ab_fn, 'r'))

LOG_LEVEL = TVRN_SETTINGS.get('log_level', 'info')

FULL_CLEAN = TVRN_SETTINGS.get('wipe-databases', False)