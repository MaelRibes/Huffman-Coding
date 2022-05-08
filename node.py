class Node:
    def __init__(self, char, proba, left=None, right=None):
        self.char = char
        self.proba = proba
        self.left = left
        self.right = right
        self.code = None

    def __str__(self):
        return f'Node({self.char},{self.proba},{self.left},{self.right},{self.code})'

    def is_leaf(self):
        if(self.left is None)and(self.right is None):
            return True
        return False
