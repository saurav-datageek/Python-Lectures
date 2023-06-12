#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'nb_black')

import pandas as pd
import numpy as np

import seaborn as sns


# Dataframe Convention:
# 
# - Excel type file in Python.
# - Usually rows are the observations and columns are the variables/features.
# - Usually all columns of the same length. 
# - Usually all columns have same data type within that column.

# In[2]:


data = {"name": ["Nepal", "Spain"], "capital": ["Kathmadu", "Madrid"]}
pd.DataFrame(data)


# In[3]:


data_list = [["Nepal", "Kathmandu", 20], ["Spain", "Madrid", 10]]
pd.DataFrame(data_list)


# In[4]:


df = pd.read_csv("mtcars.csv")
print(df.shape)
df.head()


# In[5]:


df["mpg"].sum()


# In[6]:


df["mpg"].mean()


# ### Indexing: iloc, loc, normal ones ###

# ### Filtering to try: ###

# - Normal greater than less than condition.
# - Two or more conditions clubbed.
# - nlargest, nsmallest one.
# - string starts with, contains ones.

# ### Group By ###

# In[7]:


group = df.groupby("cyl")


# In[8]:


group.size()


# In[9]:


group.apply(np.mean)


# In[10]:


df.groupby("am").apply(np.mean)


# In[11]:


df.groupby("vs").apply(min)


# In[12]:


df.groupby("cyl").agg("min")


# In[13]:


df.groupby("cyl").agg([min, max, np.mean])


# In[14]:


df.groupby("cyl").drat.agg(min)


# In[15]:


df.groupby("cyl").drat.agg(lambda x: np.mean(x) + 10)


# In[16]:


df["mpg"].median()


# In[17]:


df.describe()


# In[18]:


df["mpg"].std()


# In[19]:


df.head()


# In[20]:


df.shape


# In[21]:


### Select ###


# In[22]:


df[["mpg", "cyl"]].mean()


# In[23]:


df.loc[0:3, ["cyl", "hp"]]


# In[24]:


df.iloc[0:3, :]


# In[25]:


df.loc[df["mpg"] > 20]


# In[26]:


df[(df.mpg > 20) & (df.wt > 3)]


# In[27]:


df[(df.mpg > 20) | (df.wt > 3)].head(3)


# In[28]:


df.rename({"new_mpg": "mpg"}, inplace=True)


# In[29]:


df.head()


# In[30]:


df.groupby("cyl").mean()


# In[31]:


df.groupby("cyl").min()


# In[32]:


df.groupby("cyl").aggregate(["mean", "min", "max", "std"])


# In[33]:


df.groupby("vs")


# In[34]:


new_df = pd.DataFrame(
    {"name": ["Saurav", "Shreeya", "Suruchi", "Manasvi"], "age": [30, 29, 24, 28]}
)


# In[35]:


new_df


# In[36]:


type(new_df)


# In[37]:


new_df


# In[38]:


new_df = pd.DataFrame(
    [["Nepal", "Kathmandu", 1], ["Spain", "Madrid", 2]],
    columns=["Country", "Capital", "Number"],
)
new_df


# In[39]:


df["mpg_label"] = np.where(df["mpg"] > 20, "High", "Low")


# In[40]:


df["weight_label"] = np.where(df["wt"] > 3, "High", "Low")


# In[41]:


df["mpg"].corr(df["disp"])


# In[42]:


df.corr()


# In[43]:


df["mpg"].cov(df["disp"])


# In[44]:


df.cov()


# In[45]:


df.index = range(100, 132)


# In[46]:


df.head()


# In[47]:


df.loc[100:105, ["mpg", "hp"]]


# In[48]:


df.iloc[100:105, 5:8]


# In[49]:


df.iloc[1:5, 5:8]


# In[50]:


np.where(df["wt"] > 3, "New", "Old")


# In[51]:


df["weight_label"] = np.where(df["wt"] > 3, "New", "Old")


# In[52]:


df.groupby("cyl").mean()


# In[53]:


df.groupby("cyl").hp.mean()


# In[54]:


df.groupby("cyl").aggregate(["mean", "std", "min"])

