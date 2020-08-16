#My attempt at making trees with lists

class node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
