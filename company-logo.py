import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    x=Counter(s).most_common(3)
    for i in x:
        print(*i)
