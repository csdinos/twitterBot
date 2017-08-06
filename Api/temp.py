# temp file, just to test things out
import sys
sys.path.insert(0, '/home/dinos/twitterBot/')
from secrets import *
from ListRetriever import *

listRetriever = ListRetriever(C_KEY, C_SECRET);

print listRetriever.getLists()
