#Stack.py

class Stack:
    def __init__(self):
        self.keystore = {}

    def add(self,key,value):
        if key in self.keystore:
            self.keystore[key].append(value)
            return True
        else:
            #create a list in the key
            self.keystore[key] = []
            self.keystore[key].append(value)
            return True

    def pop(self,key):
        try:
            return self.keystore[key].pop()
        except(IndexError,KeyError):
            return None

