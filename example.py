from pyspell.checker import *

check=Checker("./pyspell/data/wordlist.txt","./pyspell/data/bktree.pickle"); #The first is the intended wordlist. You can find the example one on the github repo, whereas the second is the intended tree name. This will be made.
check.load(); #Initialize the tree into memory.
print(check.check("grat",returnNum=0)) #Modes word, return# (0 is all), returnType(see docs for type),extreme_correction=boolean (default True, disable for speed)
print(check.check(["diiffficult","arnds"])) #Make a query 
''' response
['rat', 'grad', 'gras', 'gray', 'grab', 'goat', 'great', 'grant']
['difficult', 'and']
'''