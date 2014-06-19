#!/usr/bin/env python
import sys, os

import chpl_tasks
from utils import memoize

@memoize
def get():
    hwloc_val = os.environ.get('CHPL_HWLOC')
    if not hwloc_val:
        tasks_val = chpl_tasks.get()
        if tasks_val == 'qthreads':
            hwloc_val = 'hwloc'
        else:
            hwloc_val = 'none'
    return hwloc_val


def _main():
    hwloc_val = get()
    sys.stdout.write("{0}\n".format(hwloc_val))


if __name__ == '__main__':
    _main()
