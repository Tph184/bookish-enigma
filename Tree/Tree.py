class Treenode():
    def __init__(self, data, children=[]) -> None:
        self.data = data
        self.children = children
    def __str__(self, level=0) -> str:
        result = f'{" "*level}{self.data}\n'
        # result = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result
    def addChild(self, node) -> None:
        self.children.append(node)

if __name__ == '__main__':
    tree1 = Treenode('Something1', [])
    tree2 = Treenode('Something2', [])
    tree3 = Treenode('Something3', [])
    tree1.addChild(tree3)
    tree1.addChild(tree2)
    print(tree1)