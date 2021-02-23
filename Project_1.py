import numpy as np

#Creating a QUEUE CLASS to access queue methods
class Queue:
    
    def __init__(self):
        self.items = []
    #To insert an element at the back of the queue 
    
    def enqueue(self, item):
        self.items.insert(0 , item)
        
    #To remove the back element     
    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None
    #To return the back element   
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    #To get the length of the queue
    def size(self):
        return len(self.items)
    #To see if the queue is empty    
    def is_empty(self):
        return self.items == []
    
    
q = Queue()

#GOAL STATE
goal_state = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])

#TEST CASES
root = np.array([[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]])    #1
#root = np.array([[1, 0, 3, 4],[ 5, 2, 7, 8], [9, 6, 10, 11] , [13, 14, 15, 12]])   #2
#root = np.array([[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]])    #3
#root = np.array([[5, 1, 2, 3],[0,6, 7, 4], [9, 10, 11, 8] , [13, 14, 15, 12]])     #4
#root = np.array([[1, 6, 2, 3], [9,5, 7, 4], [0, 10, 11, 8] , [13, 14, 15, 12]])     #5

root = np.reshape(root,(4,4))

#Declaring lists for Visited Nodes, Visited Nodes in String and Path
vis = list()
path = list()
vis_str = list()

#Adding the root to the queue
q.enqueue(root)
#Appending root to visited list
vis.append(root)

#This function updates the Current Node(Parent Node) on every iteration
#It also returns the location of the blank tile in each updated current node
def currentnode():

    cn1 = q.dequeue()
    
    z = np.where( cn1 == 0 )
    a = z[0][0]
    b = z[1][0]
    
    return cn1,a,b

#To move the tile upwards and return string converted node as well
def up(i,j):
    cn2 = np.copy(cn1)
    cn2[i-1][j],cn2[i][j] = cn2[i][j],cn2[i-1][j]             #up
    st = string(cn2)
    return st,cn2

#To move the tile downwards and return string converted node as well   
def down(i,j):
    cn3 = np.copy(cn1)
    cn3[i+1][j],cn3[i][j] = cn3[i][j],cn3[i+1][j]             #down
    st = string(cn3)
    return st,cn3

#To move the tile to the right and return string converted node as well   
def right(i,j):
    cn4 = np.copy(cn1)
    cn4[i][j+1],cn4[i][j] = cn4[i][j],cn4[i][j+1]                      #right
    st = string(cn4)
    return st,cn4

#To move the tile to the left and return string converted node as well       
def left(i,j):
    cn5 = np.copy(cn1)
    cn5[i][j-1],cn5[i][j] = cn5[i][j],cn5[i][j-1]                      #left
    st = string(cn5)
    return st,cn5

#This function calls the appropriate move functions according to the restrictions of the tile --
#   -- and store the string and array value of the generated nodes

#The function returns the child nodes created of the current parent node and the current parent
def move(i,j,cn1):
    
    children = list ()
    children_string = list()
                                        
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

#This function checks if the current node is in the visited list or not
def visitornot(cn,childstr,cn1):
                                                           
            counter=2
            for i in range(len(vis_str)):
                if childstr == i:
                   counter=1
                   break
                else: 
                    counter=2
            if counter==2:
                for i in range(len(cn)):
                    vis_str.append(childstr)
                    vis.append((cn[i],cn1))  

#Checking if the node is Goal State or not
def gsornot(children,parent) :
    
    childs = np.asarray(children)
    
    for i in range(len(children)):
        if np.array_equiv(childs[i],goal_state) == True:
           return childs[i],parent
        else: 
            q.enqueue(childs[i])
    return 

#Running the loop till the goal state is found
y = None
    
while y is None: 
    
    cn1,i,j = currentnode()
    
    lis, parent = move(i,j,cn1)

    y = gsornot(lis , parent)  

          
#Taking the node only from Y
child=y[0]

#Tracking back from Goal State to the first child
while np.array_equiv(parent,root) ==  False:
    
    for i in range(len(vis)):
        
        if np.array_equiv(child,vis[i][0]) == True:   
            parent = vis[i][1] 
            child  = vis[i][1]                           
            path.append(vis[i][0])
            break

#Appending the root node and reversing to get the path             
path.append(root)
path.reverse()

file = open("nodePath_TestCase5.txt", "w")
for i in range(len(path)):
    a = string(path[i])
    #print(type(a))
    #print('A : ',a)
    file.write(a)
    file.write('\n')

file.close()   
print(path)

'''#Generating text file of the path for TEST CASE 1
file = open("nodePath_TestCase1.txt", "w")
for i in range(len(path)):
    a = string(path[i])
    #print(type(a))
    #print('A : ',a)
    file.write(a)
    file.write('\n')

file.close()    
print(path)'''

#Generating text file of the path for TEST CASE 2
'''file = open("nodePath_TestCase2.txt", "w")
for i in range(len(path)):
    a = string(path[i])
    #print(type(a))
    #print('A : ',a)
    file.write(a)
    file.write('\n')

file.close()    
print(path)'''


#Generating text file of the path for TEST CASE 3
'''file = open("nodePath_TestCase3.txt", "w")
for i in range(len(path)):
    a = string(path[i])
    #print(type(a))
    #print('A : ',a)
    file.write(a)
    file.write('\n')

file.close()    
print(path)'''


#Generating text file of the path for TEST CASE 4
'''file = open("nodePath_TestCase4.txt", "w")
for i in range(len(path)):
    a = string(path[i])
    #print(type(a))
    #print('A : ',a)
    file.write(a)
    file.write('\n')

file.close()    
print(path)'''


#Generating text file of the path for TEST CASE 5
'''file = open("nodePath_TestCase5.txt", "w")
for i in range(len(path)):
    a = string(path[i])
    #print(type(a))
    #print('A : ',a)
    file.write(a)
    file.write('\n')

file.close()   
print(path)'''

