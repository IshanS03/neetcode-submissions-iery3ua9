class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        curNode = self.root
        for c in word:
            
            if c not in curNode.children:
                newNode = TrieNode()
                curNode.children[c] = newNode
            
            curNode = curNode.children[c]

        curNode.endOfWord = True

        

    def search(self, word: str) -> bool:
        
        return self.dfs(word, self.root)
        

    def dfs(self, word:str, node: TrieNode):

        if(word == ""):
            return node.endOfWord
           
        


        if(word[0]) == '.':
            for letter in node.children:
                if(self.dfs(word[1:], node.children[letter])):
                    return True
            return False
        else: 
            if(word[0] in node.children):
                return self.dfs(word[1:], node.children[word[0]])
            else:
                return False

        
            
        

            




        