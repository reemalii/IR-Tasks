from binarytree import build, Node

def add_node(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = add_node(node.left, value)
    elif value > node.value:
        node.right = add_node(node.right, value)
    return node

def delete_node(node, value):
    if node is None:
        return node
    if value < node.value:
        node.left = delete_node(node.left, value)
    elif value > node.value:
        node.right = delete_node(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.value = temp.value
            node.right = delete_node(node.right, temp.value)
    return node

def menu():
    print('Choose an option:')
    print('1. Add an element to the binary tree')
    print('2. Delete an element from the binary tree')
    print('3. Print the binary tree')
    print('4. Quit')
    choice = input('Enter your choice: ')
    return choice

def main():
    values = input('Enter a list of integers, separated by spaces: ').split()
    root = build(values)
    while True:
        choice = menu()
        if choice == '1':
            value = int(input('Enter a value to add: '))
            root = add_node(root, value)
        elif choice == '2':
            value = int(input('Enter a value to delete: '))
            root = delete_node(root, value)
        elif choice == '3':
            print(root)
        elif choice == '4':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()