#!/usr/bin/env python
# coding: utf-8

# In[9]:


""" Clean the Messy salary into integers for Data Processing
salary = '$876,001' 

Hint:
    Remove the $
    Remove the ,
    Convert into integer
"""


# In[10]:


sal = input("Enter your salary: ")


# In[11]:


print("".join(sal[1:].split(',')))

