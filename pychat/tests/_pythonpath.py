
# -*- coding: utf-8 -*-

'''
just setting the pythonpath
'''

import sys
from pathlib import Path
HERE = Path(__file__).parent
PYPATH = str((HERE / '..').resolve())
if PYPATH not in sys.path:
    sys.path.append(str(PYPATH))
