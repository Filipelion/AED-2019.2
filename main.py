from tree import *

def screen():
    print("Escolha a função que deseja:")
    print("Para inserir nó. Digite [1]")
    print("Para mostrar árvore. Digite [2]")
    print("Para sair do programa. Digite [0]")
    choice = input("Digite aqui: ")
    return choice

def insert_node():
    tree = Tree()
    while True:
        insert = input("Digite o nó que deseja inserir e [.] 'ponto' para sair: ")
        if insert == '.':
            break
        else:
            tree.insert(int(insert))
    return tree

def tree_print(tree):
    print('[1] InOrder')
    print('[2] PreOrder')
    print('[3] PosOrder')
    type = int(input('Digite a opção de exibição: '))
    return tree.TreeWalk(type)


while True:
    try:
        choice = screen()
        if choice == '0':
            break
        elif choice == '1':
            x = insert_node()
        elif choice == '2':
            walk = tree_print(x)
            print(walk)
    except:
        print("Insira valores válidos")
