import os
import pickle

TOLERANCE=2; #Increase this number to get a wider degree of results. Naturally, it's slower as well. This code is specialized around 2, due to the huge wordlist.
pickle_filepath = "../data/bktree.pickle" #This makes redundant runs slightly faster

TOLERANCE=2; #Increase this number to get a wider degree of results. Naturally, it's slower as well. This code is specialized around 2, due to the huge wordlist.
class Node: # Node of the BK tree: contains a dict of children of key distance from root word.
    def __init__(self,data="",diff=0):
        self.data=data;
        self.branch=diff; 
        self.children={};
    def nextOpen(self,integer): #Finds the next child without a certain key in its own children
        if integer in children.keys():
            nextOpen(children[integer])
        return self
    def printSelf(self): #Used to print all items in the dict beneath a root node. Primarily for debugging.
        print(self.data)
        for child in self.children.keys():
            self.children[child].printSelf()
def getDistance(s1, s2): #https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
    return d[lenstr1-1,lenstr2-1]
def placeInTree(currentRoot,word,currentDistance): #Inserts words into the tree rationally
     if currentDistance in currentRoot.children.keys():
         placeInTree(currentRoot.children[currentDistance],word,getDistance(word,currentRoot.children[currentDistance].data))
     else:
         currentRoot.children[currentDistance]=Node(word,currentDistance)
def fillTree(root,dictionary): #The initial function that establishes a data root and fills the dict. (if necessary)
    #print("Filling Tree.");
    for word in dictionary:
        if (root.data==""):
            root.data=word
        else:
            placeInTree(root,word,getDistance(word, root.data))
    #print("Loaded.")
def matchWord(root,word): #Navigates the BK tree
    matches=[]
    if (root.data == ""):
       return matches
    distance=getDistance(root.data,word)
    if (distance<TOLERANCE):
        matches.append(root.data)
    start=distance-TOLERANCE
    if (start < 0):
        start=1;
    for child in sorted(list(filter(lambda x: x>distance-TOLERANCE and x<distance+TOLERANCE, root.children.keys()))):
        if (start < distance + TOLERANCE):
            nextwords=matchWord(root.children[child],word)
            for newwords in nextwords:
                matches.append(newwords)
            start+=1
    return matches;
def makeSearch(word,returnNum=1,returnType="words",repeat=False): #The actual search function
    word=word.lower();
    sortedOptions=matchWord(root,word) #all the possible words
    rankings=map(lambda x: dictionary.index(x),sortedOptions) #word ranks based on wordlist.txt
    pairing=sorted(zip(sortedOptions,rankings), key=lambda x: x[1]); #combines the two efficiently and sorts them
    if returnType=="pairings":
        return pairing
    elif returnType=="rankings":
        return rankings
    elif returnType=="words":
        global TOLERANCE
        if word in sortedOptions:
            #If the word is already possible, don't bother returning other options
            return word;
        else:
            if (pairing!=[]): #Attempt to find a word that fits with tolerance 2, but sacrifice speed and go to tolerance 3 if there's nothing.
                if(len(pairing)>=returnNum):
                    return [pairing[i][0] for i in range(0,returnNum)]
                else:
                    return [pairing[i][0] for i in range(0,len(pairing))]                 
                TOLERANCE=2
            elif TOLERANCE==2 and repeat==True:
                TOLERANCE=3;
                makeSearch(word);
            else:
                TOLERANCE=2
                return None;
with open("../data/wordlist.txt",'r') as wordlist:
        dictionary=list(filter(lambda x: len(x)>1,map(lambda x: x.strip(),wordlist.readlines())));
if not os.path.exists(pickle_filepath):
    root=Node("")
    fillTree(root,dictionary)
    # Read data set from disk
    with open(pickle_filepath, 'wb') as pickle_handle:
        pickle.dump(root, pickle_handle)
else:
    file = open(pickle_filepath, 'rb')
    root = pickle.load(file)
    file.close()
        
while True:
    makeSearch(input("Word:"))
