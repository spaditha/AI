echo "# AI" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/spaditha/AI.git
git push -u origin main

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import json
import math
import os
import random
import modeling
import optimization
import tokenization
import six
import numpy as np
import tensorflow as tf
