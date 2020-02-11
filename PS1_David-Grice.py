
# coding: utf-8

# In[135]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as ss
import matplotlib.pyplot as plt
import math


# In[136]:


salaryData =pd.read_csv("Salaries_Edit.csv")


# In[137]:


salaryData


# In[138]:


yearsApprox = salaryData[["Years Approx"]]


# In[139]:


yearsApprox


# In[140]:


plt.xticks(rotation=45)
sns.distplot(yearsApprox, bins = range(0,40,2),kde=False)

plt.ylabel("Clerk Jobs")
plt.xlabel("Years of Service")
plt.title("Clerk Jobs vs Years of Service")


# In[141]:


yearsApprox.describe()


# In[142]:


positionJob = salaryData[["Position Title"]]


# In[143]:


positionJob


# In[144]:


positionJob = salaryData[salaryData['Position Title'].fillna('').str.contains('Account Clerk')]


# In[145]:


positionJob


# In[146]:


positionJob = salaryData[salaryData["Position Title"].fillna('').str.contains('Account Clerk')]


# In[147]:


positionJob["Position Title"].value_counts()


# In[148]:


salaryPos = positionJob["Position Title"].value_counts(), positionJob["Salary"].value_counts()
positionJob["Salary"] = positionJob["Salary"].str.replace('$', '')
positionJob["Salary"] = positionJob["Salary"].astype('float')


# In[149]:


ct = pd.crosstab(index = positionJob["Department ID"], columns = positionJob["Position Title"], values = positionJob["Salary"], aggfunc = 'median')
ct


# In[150]:


ax = plt.axes()
sns.heatmap(ct, cmap = "BuPu")
ax.set_title("Comparing Department ID, Position Title and Salary")


# In[151]:


col=pd.read_csv('Key_Credit_Collection__Beginning_2010.csv')
col_2 = col[col['Company Name'] == 'CH']
plt.scatter(x =  col_2["Residential Average Sales"], y = col_2["Residential Customers"], data = col_2)

plt.ylabel("Residential Average Sales")
plt.xlabel("Residential Customers")
plt.title("Residential Average Sales vs Residential Customers")

np.corrcoef(col_2["Residential Average Sales"], col_2["Residential Customers"])[0, 1]


# In[152]:


resident


# In[153]:


dc = pd.read_csv("dc-wikia-data.csv")


# In[154]:


dc


# In[155]:


newDC = dc[dc['SEX'].fillna('').str.contains('Male Characters|Female Characters')]
dc["SEX"].value_counts()


# In[156]:


newDC


# In[157]:


sns.barplot( x = "SEX", y = "APPEARANCES", data = newDC)
plt.title("DC Sexuality of Characters")


# In[158]:


newDC = dc[dc['SEX'].fillna('').str.contains('Male Characters')]
newDC.describe()


# In[159]:


newDC = dc[dc['SEX'].fillna('').str.contains('Female Characters')]
newDC.describe()

