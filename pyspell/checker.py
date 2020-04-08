import bktree,updateDict,pickle
from bktree import makeSearch,Node,setDictionary
from updateDict import addWord,repickle
import os,time
class Checker:
    def __init__(self, newDictPath=False):
        if not os.path.exists("./data/bktree.pickle"):
            repickle();
        self.dictionaryPath="./data/wordlist.txt"
        if newDictPath!=False:
            self.dictionaryPath=newDictPath;
    def load(self,cachedTree="./data/bktree.pickle"):
        with open(self.dictionaryPath,'r') as wordlist:
            self.dictionary=list(filter(lambda x: len(x)>1,map(lambda x: x.strip(),wordlist.readlines())));
        file = open(cachedTree, 'rb')
        self.root = pickle.load(file)
        file.close()
    def check(self,word,returnNum=1,returnType="words",repeat=False):
        return makeSearch(word,self.root,self.dictionary,returnNum,returnType,repeat)
    def updateDict(self,word,priority=-1,dictPath="./data/wordlist.txt",repickle=True):
        addWord(word,priority,dictPath,repickle);
        with open(self.dictionaryPath,'r') as wordlist:
            self.dictionary=list(filter(lambda x: len(x)>1,map(lambda x: x.strip(),wordlist.readlines())));