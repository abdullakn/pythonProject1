
class Node:
    def __init__(self):
        self.end=False
        self.suffix_dict = {}

class SuffixTrie:
    def __init__(self,str):
        self.root=Node()

        if str is not None:
            for i in range(0,len(str)):
                self.populate_suffix_trie(i,str)


    def populate_suffix_trie(self,i,str):
        # for i in range(0,len(str)):
        print(str[i])
        self.insert_substring(i,str)

    def insert_substring(self,index,str):
        node=self.root

        for i in range(index,len(str)):
            letter=str[i]
            # letter=node.suffix_dict.keys(i)

            if letter in node.suffix_dict:
                node = node.suffix_dict[letter]
            else:
                new_node = Node()
                node.suffix_dict[letter] = new_node
                node = new_node
                # node=node.suffix_dict[letter]
        node.end=True


    def contains(self, search):
        node = self.root
        for i in search:
            if not i in node.suffix_dict.keys():
                return False
            else:
                node = node.suffix_dict[i]
        return node.end




obj=SuffixTrie("abdu")
print(obj.contains("hello"))
print(obj.contains("abdu"))
print(obj.contains("bdu"))
print(obj.contains("du"))

