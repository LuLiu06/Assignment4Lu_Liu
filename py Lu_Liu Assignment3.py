#!/usr/bin/env python
# coding: utf-8

# # Exercise 3

# ## Lu Liu

# ### 2023/2/25

# ### question 1

# In[18]:


x = lambda num1,num2: num1*num2
x(5,6)


# ### question 2

# In[19]:


import math
def area_circle(r):
    return math.pi*r**2
area_circle(10)


# ### question 3

# In[20]:


def calculator(num1,num2,operation):
    if operation == "a":
        return num1 + num2
    if operation == "s":
        return num1 - num2
    if operation == "m":
        return num1 * num2
    if operation == "d":
        return num1 / num2
calculator(2,5,"d")


# ### question 4

# In[21]:


class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width    
    def area(self):
        return self.length * self.width
    
r = Rectangle(5,10)
r.area()


# In[22]:


class Shape():
    def __init__(self, name, length):
        self.name = name
        self.length = length
        
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name, length)
        
    def area(self):
        
        print ("the area is:")
        return self.length**2
    
    def describe(self):
        
        return "this is a: "+ self.name
    
    
s = Square('square',5)
print(s.area())
print(s.describe())


# In[ ]:





# In[ ]:





# In[ ]:




