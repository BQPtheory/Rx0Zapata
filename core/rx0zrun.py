#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import sys
from interface.banners import *


# Colors
COLOR = {
    'blue': '\033[94m',
    'default': '\033[99m',
    'grey': '\033[90m',
    'yellow': '\033[93m',
    'black': '\033[90m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'red': '\033[91m',
    'nullcolor': '\033[00m'
}

os.system("clear")

# Args Menu
def main():
    logo_master()
    print('''\t   $_\033[90m¡\033[00m\033[97mSELECT OPTION\033[00m - \033[91mOFENSIVE\033[00m & \033[94mDEFENSIVE\033[00m\033[90m!\033[00m_
    ''')
    print('''\tUsage: python3 rx0zrun -h [options]\n\n''')
    parser = argparse.ArgumentParser()
    #parser.add_argument("-- target", type = str, metavar = "<IP/IP+Port/Url>", help = "Target IP, IP and Port, URL" )
    parser.add_argument(" ", type = str, metavar = " ")
    parser.add_argument(" ", type = str, metavar = " ")
    parser.add_argument(" ", type = str, metavar = " ")
    parser.add_argument(" ", type = str, metavar = " ")





if __name__ == "__main__":
    main()















