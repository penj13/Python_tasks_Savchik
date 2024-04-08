# возможно это задание по JS все-таки ??? :)
class Node:
    def __init__(self, data):
        self.data = data 
        self.next_node = None 
        self.prev_node = None
        
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.i = 0
    
    def menu(self):
        print('Что делаем со списком?')
        print('1. Добавить элемент в конец списка')
        print('2. Удалить элемент из конца списка')
        print('3. Добавить элемент в начало списка')
        print('4. Удалить элемент из начала списка')
        print('5. Показать список')
        a = input('Введите цифру действия:', )
        if a == '1':
            b = input('Введите значение узла:', )
            list.add_f(b)
        elif a == '2':
            i = -1
            list.del_f(i)
        elif a == '3':
            b = input('Введите значение узла:', )
            list.add_s(b)
        elif a == '4':
            i = -1
            list.del_s(i)
        elif a == '5':
            list.display()
    
    def add_f (self, data):
        new_node = Node(data)
        if self.head == None:
            self.i += 1
            self.head = self.tail = new_node
            self.head.prev_node = None
            self.tail.next_node = None
            print('-----------------------------------')
            list.menu()

        else:
            self.i += 1
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
            self.tail.next_node = None
            print('-----------------------------------')
            list.menu()
            
    def add_s (self, data):
        new_node = Node(data)
        if self.head == None:
            self.i += 1
            self.head = self.tail = new_node
            self.head.prev_node = None
            self.tail.next_node = None
            print('-----------------------------------')
            list.menu()
        else:
            self.i += 1
            self.head.prev_node = new_node
            new_node.next_node = self.head
            new_node.prev_node = None
            self.head = new_node
            print('-----------------------------------')
            list.menu()
    
    def del_f (self, data):
        if self.head == None:
            print('-----------------------------------')
            print ('Нечего удалять, спсисок пуст!')
            print('-----------------------------------')
            list.menu()
        else:
            self.i -= 1
            if(self.head != self.tail):
                self.tail = self.tail.prev_node 
                self.tail.next_node = None
                print('-----------------------------------')
                list.menu()
            else:   
                self.head = self.tail = None
                print('-----------------------------------')
                list.menu()
            
    def del_s (self, data):   
        if(self.head == None):   
            print('-----------------------------------')
            print ('Нечего удалять, спсисок пуст!')
            print('-----------------------------------')
            list.menu()
        else:
            self.i -= 1
            if(self.head != self.tail):   
                self.head = self.head.next_node 
                self.head.previous = None
                print('-----------------------------------')
                list.menu()
            else:   
                self.head = self.tail = None
                print('-----------------------------------')
                list.menu()
    
    def display (self):
        current = self.head
        if self.head == None:
            print('-----------------------------------')
            print('Двусвязный список пуст!')
            print('-----------------------------------')
            list.menu()
        else:
            print('-----------------------------------')
            print('Наш двусвязный список:')
            while current != None:
                print(current.data),
                current = current.next_node
            print("Количество узлов - ", self.i)
            print('-----------------------------------')
            list.menu()
            
list = MyList()
list.menu()





