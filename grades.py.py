#!/usr/bin/env python
# coding: utf-8

# In[87]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('real.csv')


# In[97]:


print(df.loc[1105])


# In[102]:


distributions= []
def prof_class(class_num):
    grade_dis = []
    profs = []
    for i in range(1105, 1226):
        grades = {}
        if df.loc[i][0] == "CPSC":
            temp = {}
            temp["Course number"] = df.loc[i][1]
            
            if(class_num == temp["Course number"]):
                profs.append(df.loc[i][16])
                
                grades["A"] = df.loc[i][4]
                grades["B"] = df.loc[i][5]
                grades["C"] = df.loc[i][6]
                grades["D"] = df.loc[i][7]
                grades["F"] = df.loc[i][8]
                grade_dis.append(grades)
        
    return grade_dis, profs
        
    


# In[109]:


grades, teacher = prof_class("2120")
print(grades)
print(teacher)


# In[6]:


df_sheet_index = pd.read_excel('202201 (1).xlsx', sheet_name=1)

print(df_sheet_index.Course)


# In[ ]:




