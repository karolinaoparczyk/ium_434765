#!/usr/bin/python

import sys
import pandas as pd

data = pd.read_csv(sys.argv[1])
print(data.describe(include="all"))
print(data['likes'].value_counts())
