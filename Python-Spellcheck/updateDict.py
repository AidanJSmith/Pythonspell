import os
from bktree import *
import pickle


def repickle(newDictpath="../data/wordlist.txt"): #Deletes the current cached BKtree & rewrites it with the dict.
    if os.path.exists("../data/bktree.pickle"):
        os.remove("../data/bktree.pickle")
    with open(newDictpath,'r') as wordlist:
            dictionary=list(filter(lambda x: len(x)>1,map(lambda x: x.strip(),wordlist.readlines())));
    root=Node()
    fillTree(root,dictionary)
    with open(newDictpath, 'wb') as pickle_handle:
            pickle.dump(root, pickle_handle)
def addWord(word,priority=-1,dictPath="../data/wordlist.txt",repickle=True):
    file = open("dictPath", "r")
    content=file.readlines();
    file.close()
    if (type(word)==list):
        for item in word:
            if(priority<0):
                content.insert(len(content),item)
            content.insert(priority,item)
    elif type(word)==dict:
        for key in word.keys():
            if(type(key.location)==int):
                content.insert(key.location,key)
            elif(priority<0):
                content.insert(len(content),key)
            else:
                content.insert(priority,key)    
    elif type(word)==str:
         if(priority<0):
                content.insert(len(content),word)
         content.insert(priority,word)
    f = open(dictPath, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    if repickle:
        repickle(dictPath);
    