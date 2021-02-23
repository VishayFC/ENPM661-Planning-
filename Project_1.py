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

def up(i,j):
    cn2 = np.copy(cn1)
    #print('CN1 : ',cn1)
    cn2[i-1][j],cn2[i][j] = cn2[i][j],cn2[i-1][j]                      #up
    #visitornot(cn2,cn1)
    #print('up')
    st = string(cn2)
    return st,cn2
    
def down(i,j):
    cn3 = np.copy(cn1)
    #print('CN1 : ',cn1)
    cn3[i+1][j],cn3[i][j] = cn3[i][j],cn3[i+1][j]                      #down
    #visitornot(cn3,cn1)
    #print('down')
    st = string(cn3)
    return st,cn3
    
def right(i,j):
    cn4 = np.copy(cn1)
    #print('CN1 : ',cn1)
    cn4[i][j+1],cn4[i][j] = cn4[i][j],cn4[i][j+1]                      #right
    #visitornot(cn4,cn1)
    #print('right')
    st = string(cn4)
    return st,cn4
        
def left(i,j):
    cn5 = np.copy(cn1)
    #print('CN1 : ',cn1)
    cn5[i][j-1],cn5[i][j] = cn5[i][j],cn5[i][j-1]                      #left
    #visitornot(cn5,cn1)
    #print('left')
    st = string(cn5)
    return st,cn5

def move(i,j,cn1):
    
    children = list ()
    children_string = list()
    #goal = None
    #print(i,j)
            
       
                              
    if i == 0:
        if j == 0:
            st,cn = down(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = right(i,j)
            children.append(cn)
            children_string.append(st)
                
        elif j == 1 or j == 2:
            st,cn = down(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = left(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = right(i,j)
            children.append(cn) 
            children_string.append(st)
                
        elif j == 3:
            st,cn = down(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = left(i,j)
            children.append(cn) 
            children_string.append(st)
            
    if i == 1 or i == 2:
        if j == 0:
            st,cn = up(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = down(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = right(i,j)
            children.append(cn) 
            children_string.append(st)
                
        elif j == 1 or j == 2:
            st,cn = up(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = down(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = right(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = left(i,j)
            children.append(cn)
            children_string.append(st)
            
        elif j == 3:
            st,cn = up(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = down(i,j)
            children.append(cn)
            children_string.append(st)
            st,cn = left(i,j)
            children.append(cn)
            children_string.append(st)
                
    if i == 3:
       if j == 0:
           st,cn = up(i,j)
           children.append(cn)
           children_string.append(st)
           st,cn = right(i,j)
           children.append(cn)
           children_string.append(st)
               
       elif j == 1 or j == 2:
           st,cn = up(i,j)
           children.append(cn)
           children_string.append(st)
           st,cn = left(i,j)
           children.append(cn)
           children_string.append(st)
           st,cn = right(i,j)
           children.append(cn)
           children_string.append(st)
               
       elif j == 3:
           st,cn = up(i,j)
           children.append(cn)
           children_string.append(st)
           st,cn = left(i,j)
           children.append(cn) 
           children_string.append(st)
           
    visitornot(children,children_string,cn1) 
     
    return children,cn1

#This function converts the incoming numpy arrays to strings
def string(cn):
    string=""
    for i in range(len(cn)):
        for j in range(len(cn[0])):
            string=string+" "+str(cn[i][j])
    return string

#This function 
def visitornot(cn,childstr,cn1):
                                                           
            counter=2
            for i in range(len(vis_str)):
                if childstr == i:
                   counter=1
                   #return None,None
                   break
                else: 
                    counter=2
                    #break
            if counter==2:
                for i in range(len(cn)):
                    #print('CN : ',cn)
                    vis_str.append(childstr)
                    vis.append((cn[i],cn1))  

def gsornot(children,parent) :
    
    childs = np.asarray(children)
    
    for i in range(len(children)):
        if np.array_equiv(childs[i],goal_state) == True:
           return childs[i],parent
        else: 
            q.enqueue(childs[i])
    return


y = None
    
while y is None: 
    
    cn1,i,j = currentnode()
    
    lis, parent = move(i,j,cn1)

    y = gsornot(lis , parent)
