import os
os.chdir('/Users/ljudmilapetkovic/Desktop/Preprocesirani_tekstovi')     

import fileinput
import glob
import sys

for line in fileinput.input(glob.glob('*.txt'), inplace=True):
    sys.stdout.write(line.lower())
