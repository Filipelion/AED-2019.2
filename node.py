class Node:

    def __init__(self, data):
        self.__parent = None
        self.__color  = None
        self.__data   = data
        self.__left   = None
        self.__right  = None

    def getColor(self):
        """Retorna chave de acesso."""
        return self.__color

    def getData(self):
        """Retorna conteúdo armazenado."""
        return self.__data

    def getLeft(self):
        """Retorna filho esquerdo."""
        return self.__left

    def getRight(self):
        """Retorna filho direito."""
        return self.__right

    def getParent(self):
        """Retorna nó pai."""
        return self.__parent

    def setColor(self, color):
        """
        Define chave de acesso.
        ex:
        x.setColor('red')
        """
        self.__color = color

    def setData(self, data):
        """Define conteúdo armazenado."""
        self.__data = data

    def setLeft(self, left):
        """Define filho esquerdo."""
        self.__left = left

    def setRight(self, right):
        """Define filho direito."""
        self.__right = right

    def setParent(self, parent):
        u"""Define nó pai."""
        self.__parent = parent