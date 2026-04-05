class TrieNode:

        def __init__(self):
                self.children = {}
                self.endOfWord = False

class PrefixTree:

        def __init__(self):
                self.node = TrieNode()


        def insert(self, word: str) -> None:

                if(word == ""):
                        return

                curNode = self.node
                for c in word:
                        curChildren = curNode.children     
                        if c not in curChildren:
                                newNode = TrieNode()
                                curChildren[c] = newNode
                        curNode = curChildren[c]
                
                curNode.endOfWord = True                           


        def search(self, word: str) -> bool:

                curNode = self.node
                for c in word:
                        curChildren = curNode.children     
                        if c not in curChildren:
                                return False
                        curNode = curChildren[c]
                if(curNode.endOfWord == True):
                        return True
                else:
                        return False
                                                                                            

        def startsWith(self, prefix: str) -> bool:

                curNode = self.node
                for c in prefix:
                        curChildren = curNode.children     
                        if c not in curChildren:
                                return False
                        curNode = curChildren[c]
                return True

        