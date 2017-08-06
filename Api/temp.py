# temp file, just to test things out
import sys
sys.path.insert(0, '/home/dinos/twitterBot/')
from secrets import *

from Auth import TokenGenerator

tokenGenerator = TokenGenerator(C_KEY, C_SECRET)
print tokenGenerator.generate()
