class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

# Membuat objek double linked list
dll = DoublyLinkedList()

# Menambah node data 1, 2, 3, 4 ke list
for val in [1, 2, 3, 4]:
    new_node = Node(val)
    if dll.head is None:
        dll.head = new_node
    else:
        # cari node terakhir
        current = dll.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

# Mencetak isi list sebelum penghapusan
print("List sebelum penghapusan:")
current = dll.head
while current is not None:
    print(current.data, end=" <-> ")
    current = current.next
print("None")

# Menghapus node pertama
if dll.head is not None:
    if dll.head.next is None:
        dll.head = None
    else:
        dll.head = dll.head.next
        dll.head.prev = None

# Mencetak isi list setelah menghapus node pertama
print("List setelah menghapus node pertama:")
current = dll.head
while current is not None:
    print(current.data, end=" <-> ")
    current = current.next
print("None")

# Menghapus node terakhir
if dll.head is not None:
    if dll.head.next is None:
        dll.head = None
    else:
        current = dll.head
        while current.next is not None:
            current = current.next
        if current.prev:
            current.prev.next = None

# Mencetak isi list setelah menghapus node terakhir
print("List setelah menghapus node terakhir:")
current = dll.head
while current is not None:
    print(current.data, end=" <-> ")
    current = current.next
print("None")

# Menghapus node berdasarkan nilai data = 2
val_to_delete = 2
current = dll.head
while current is not None:
    if current.data == val_to_delete:
        if current.prev is not None:
            current.prev.next = current.next
        else:
            # node yang dihapus adalah head
            dll.head = current.next
        if current.next is not None:
            current.next.prev = current.prev
        break
    current = current.next

# Mencetak isi list setelah menghapus node dengan nilai 2
print("List setelah menghapus node dengan nilai 2:")
current = dll.head
while current is not None:
    print(current.data, end=" <-> ")
    current = current.next
print("None")
