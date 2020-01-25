#!/usr/bin/env python
# coding: utf-8

# In[12]:


"""
Take the age as input from the user 
and print whether he is a 
infant, Child , 
Adult,  Senior Citizen
0 - 1 is Infant
> 1 and < than 18 is Child 
> 18 and < 60 is Adult
> 60 is Senior Citizen 
"""


# In[13]:


age = float(input("Enter the age: "))


# In[14]:


if (age > 0 and age <= 1):
    print("Infant")
    
elif (age <= 18):
    print("Child")

elif (age < 60):
    print("Adult")

else:
    print("Senior Citizen")


# In[ ]:




