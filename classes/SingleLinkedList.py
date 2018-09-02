from Node import *

class SinglyLinkedList:
   
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0


    def add_head(self, value):
        'Adiciona um elemento no inicio da lista'
        node = Node(value, None)

        if self.__head is None:
            self.__head = node
            self.__tail = node
            self.__size += 1
        else:
            node.set_next_element(self.__head)
            self.__head = node
            self.__size += 1

    def add_tail(self, value):
        'Adiciona um elemento no final da lista'
        node = Node(value, None)

        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.set_next_element(node)
            self.__tail = node

    def remove_head(self):
        'Remove o elemento no inicio da lista'

        if self.__head is None:
            raise Exception("Empty.")

        self.__head = self.__head.get_next_element()


    def get_head(self):
        'Retorna o elemento do inicio da lista'
        return self.__head


    def get_tail(self):
        'Retorna o elemento do final da lista'
        return self.__tail


    def print(self):
        'Imprime a lista'
        node = self.__head

        while node is not None:
            print(node.get_value())
            node = node.get_next_element()

    def add_new_value(self, value, position):
        'Adicione um elemento em um lugar determinado da lista. Valor a ser inserido informado no parâmetro value. Posição informada no parâmetro position'
        if self.__head is None:
            raise Exception("Empty.")
        elif value < self.__size:
            raise Exception("Posição Inválida!")
        else:
            count = 0
            node = self.__head
    
            while node is not None:
                previous = node.get_value()
                node = node.get_next_element()
                if position == count:
                    node.set_value(value)
                    new = node.get_value
                    previous.set_next_value(new)
                    node.set_next_element(node)
                else:
                    count += 1
        pass
    
s = SinglyLinkedList()
s.add_head(125)
s.add_head(200)
s.add_head(25)
s.add_tail(600)
s.add_tail(700)
s.add_new_value(5, 2)
s.print()
