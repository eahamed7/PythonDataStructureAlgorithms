from operator import itemgetter


class Node:
    def __init__(self,value):
        self.next=None
        self.previous=None
        self.value=value
        
class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def apend(self,value):
        node=Node(value)
        
        if self.tail is None:
            self.head=node
            self.tail=node
            self.size+=1
        else:
            self.tail.next=node
            node.previous=self.head
            self.tail=node
            self.size+=1

    def getSize(self):
        return self.size

    def remove(self,valueToRemove):
        node=self.head
        while node is not None:
            if node.value==valueToRemove:
                self.__removeNode

    def __str__(self):
        values=[]
        node=self.head
        while node is not None:
            values.append(node.value)
            node=node.next
        return f"[{', '.join(str(value) for value in values)}]"
        
if __name__=="__main__":
    myList=DoubleLinkedList()
    myList.apend(1)
    myList.apend(5)
    myList.apend(2)

    print(myList)
