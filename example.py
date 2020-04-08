from pyspell.checker import *

check=Checker("./pyspell/data/wordlist.txt","./pyspell/data/bktree.pickle"); #The first is the intended wordlist. You can find the example one on the github repo, whereas the second is the intended tree name. This will be made.
check.load(); #Initialize the tree into memory.
print(check.check("phone",4))
print(check.check("maste")) #make a query