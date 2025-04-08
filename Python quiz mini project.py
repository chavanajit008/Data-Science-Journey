#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Python Quiz Program

# In[4]:


score= 0
q1= input("What's the currency of India?")
if q1.lower()=="rupee"or"rupees":
    score+=1
    print("correct!")
else: print("incorrect!")
q2= input("What's the name of the planet closest to the earth?")
if q2.lower()=="venus":
    score+=1
    print("correct!")
else:
    print("incorrect!")
q3= input("What is the square root of 25?")
if q3=='5':
    score+=1
    print("correct!")
else: print("incorrect!")
print("your final score is",score)


# In[ ]:




