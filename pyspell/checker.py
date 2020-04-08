import bktree,updateDict,pickle
from bktree import makeSearch,Node
from updateDict import addWord,repickle
class Checker:
    def __init__(self, newDictPath=False):
        self.dictionary="./data/wordlist.txt";
        if newDictPath!=False:
            repickle(newDictPath)
            self.dictionary=newDictPath;
    def load(self,cachedTree="./data/bktree.pickle"):
        with open(self.dictionary,'r') as wordlist:
            dictionary=list(filter(lambda x: len(x)>1,map(lambda x: x.strip(),wordlist.readlines())));
        file = open(cachedTree, 'rb')
        self.root = pickle.load(file)
        file.close()
    def check(self,word,returnNum=1,returnType="words",repeat=False):
        return makeSearch(word,returnNum,returnType,repeat)
    def updateDict(self,word,priority=-1,dictPath="./data/wordlist.txt",repickle=True):
        addWord(word,priority,dictPath,repickle)