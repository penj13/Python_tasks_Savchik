class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class NodeList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.next = self.head.prev = self.tail.next = self.tail.prev = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = None
    
    def unshift(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.next = self.head.prev = self.tail.next = self.tail.prev = None
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.tail.next = None
    
    def pop(self):
        if self.head is None:
            retun (f"Нечего удалять")
        else:
            if self.head is not self.tail:
                self.data2 = self.tail.prev
                del self.tail
                self.tail = self.data2
            else:
                del self.tail
                
    def shift(self):
        if self.head is None:
            retun (f"Нечего удалять")
        else:
            if self.head is not self.tail:
                self.data2 = self.head.next
                del self.head
                self.head = self.data2
            else:
                del self.head
        
        
nodes = NodeList()
nodes.push(1)
nodes.push(10)
nodes.unshift(11)
nodes.push(1000)
nodes.push(200)
nodes.pop()
nodes.shift()
print(nodes.head.data)
print(nodes.tail.data)
print(nodes.tail.prev.data)
print(nodes.head.next.data)


