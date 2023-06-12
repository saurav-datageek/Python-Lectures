#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'nb_black')


# In[2]:


print("Hello World")


# ### Data Types ###

# Numbers, Strings/Characters, Boolean

# In[3]:


4


# In[47]:


type(4)


# In[48]:


4.5


# In[6]:


type(4.5)


# In[7]:


"Saurav"


# In[8]:


type("Saurav")


# In[9]:


True


# In[10]:


type(True)


# ### Variables ###

# In[11]:


a = 10


# In[12]:


print(a)


# In[13]:


b = "This is my life and I will do whatever I want."


# In[14]:


print(b)


# ### More Data Types : Collection ###

# In[15]:


my_list = [1, 2, "Nepal"]
my_list


# In[16]:


my_list[2]


# In[17]:


my_list[:-1]


# In[18]:


my_list.append("Spain")


# In[19]:


my_list


# In[20]:


my_tuple = (1, 2, "Nepal")


# In[21]:


my_dictionary = {"Nepal": "Kathmandu", "India": "New Delhi", "Peru": "Lima"}


# In[22]:


my_dictionary["Peru"]


# In[23]:


my_dictionary.keys()


# In[24]:


my_dictionary.values()


# In[25]:


my_dictionary.items()


# In[26]:


my_set = {1, 2, 3, 3}


# ### Function ###

# Built in functions:

# In[27]:


len(my_set)


# In[28]:


max(my_set)


# In[29]:


def my_func():
    print("Just a random print function")


# In[30]:


my_func()


# In[31]:


def my_addition(a, b):
    c = a + b
    d = c + 10
    return d


# In[32]:


my_addition(3, 5)


# ### If Statement ###

# In[33]:


a = 10

if a >= 10:
    print("It's a double digit number")
else:
    print("It's a single digit number.")


# In[34]:


if a > 10:
    print("It's a double digit number")
elif a == 10:
    print("It's precisely 10.")
else:
    print("It's a single digit number.")


# ### For Loop ###

# In[35]:


for num in my_list:
    print(num)


# In[36]:


new_list = [1, 4, 10, 20]
for num in new_list:
    print(10 * num)


# ### Module ###

# In[37]:


import os


# In[38]:


os.getcwd()


# In[39]:


import sklearn


# In[40]:


import pandas as pd


# In[41]:


import my_module


# In[42]:


my_module.my_const


# In[43]:


my_module.my_func(1, 2)


# In[44]:


from my_module import my_func as rand_func


# In[45]:


rand_func(5, 6)


# In[46]:


my_module.my_const

