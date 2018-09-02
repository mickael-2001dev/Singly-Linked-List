class Node:
    
    def __init__(self, value, next_element):
        self.__value = value
        self.__next_element = next_element

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def get_next_element(self):
        return self.__next_element

    def set_next_element(self, next_element):
        self.__next_element = next_element  