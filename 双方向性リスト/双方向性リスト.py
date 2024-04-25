class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
 
    def insert(self, value):
        new = Cell(value)
        tmp = self.head
        if not tmp:
            new.next = new
            new.prev = new
            self.head = new
            return
        while not tmp == self.head:
            tmp = tmp.next
        tmp.prev.next = new
        new.prev = tmp.prev
        new.next = tmp
        tmp.prev = new
 
    def delete(self, value):
        tmp = self.head
        if not tmp:
            print("[*] List is empty.")
            return
        if tmp == tmp.next:
            self.head = tmp = None
            return
        if tmp.value == value:
            self.head = tmp.next
            tmp = None
            return
        isfound = False
        tmp = tmp.next
        while not tmp == self.head:
            if tmp.value == value:
                isfound = True
                break
            tmp = tmp.next
        if isfound:
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            tmp = None
        else:
            print("[*] Data not found")
 
    def show(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next
            if tmp == self.head:
                return
        else:
            print('[*] List is empty.')
            
            
            
            
url = "https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/doubly_linked_list"