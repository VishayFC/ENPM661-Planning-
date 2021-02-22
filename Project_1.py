# -*- coding: utf-8 -*-

import numpy as np

class Queue:
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0 , item)
        
    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None
        
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return self.items == []
    
    
q = Queue()

root = np.array([[1,6,2,3],[9,5,7,4],[12,10,11,0],[13,14,15,8]])
root = np.reshape(root,(4,4))

vis = list()

print('Root Node: ', root)

q.enqueue(root)

print('Queue after adding root : ',q.items)

def currentnode():

    cn1 = q.dequeue()
    print('Queue after removing root : ',q.items)

    vis.append(cn1)
    
    z = np.where( cn1 == 0 )
    #print(a)
    a = z[0][0]
    b = z[1][0]
    
    return cn1,a,b


k,i,j = currentnode()

print('Visited List : ',vis)

print('A B C : ',k,i,j)
