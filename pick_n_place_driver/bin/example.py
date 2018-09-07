#!/usr/bin/env python3

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

from lib.PickNPlace import PickNPlace

pick_n_place = PickNPlace()

pick_n_place.right(100)
pick_n_place.down(100)
pick_n_place.up(100)
pick_n_place.left(100)
