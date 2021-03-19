#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis: SuperStore Dataset

# # Anika Bizla

# # Task 3

# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## Reading the Dataset

# In[52]:


df=pd.read_csv("/Users/anikabizla/Downloads/SampleSuperstore.csv")
df.head()


# In[53]:


#checking the data types
df.dtypes


# In[54]:


#checking the shape of dataset
df.shape


# In[55]:


df.describe()


# In[56]:


df.describe(include="all")


# # Univariate Analysis

# In[57]:


#Analysing the segment of people buying from the supermarket.
df['Segment'].value_counts()


# In[58]:


df['Segment'].value_counts()/len(df['Segment'])*100


# In[59]:


S=(df['Segment'].value_counts()/len(df['Segment'])*100).plot(kind='bar',color='r')


# #### Following conclusions can be made from the graph:
# #### 1. 50% of people belongs to consumer class.
# #### 2.20-30% people belongs to Corporate and Home Offices.

# In[60]:


#Analysing Ship Mode for the SuperMart
df['Ship Mode'].value_counts()


# In[61]:


M=(df['Ship Mode'].value_counts())/len(df['Ship Mode'])*100
M


# In[62]:


M.plot(kind="bar")


# In[63]:


#Analysing Category of Items in the SuperMart
df['Category'].value_counts()


# In[64]:


C=(df['Category'].value_counts())/len(df['Category'])*100
C.plot(kind="bar",color="g")


# In[65]:


#Analysing the Sub-Category of items in the SuperMart
((df['Sub-Category'].value_counts())/len(df['Sub-Category'])*100).plot(kind='bar')


# # Bivariate Analysis

# In[66]:


fig,ax=plt.subplots()
colors={'Consumer':'red','Corporate':'blue','Home Office':'green'}
ax.scatter(df['Sales'],df['Profit'],c=df['Segment'].apply(lambda x:colors[x]))
plt.show()


# ##### We can conclude that there is more profit in consumer segment

# In[67]:


df.pivot_table(values='Sales',index='Segment',columns='Discount',aggfunc='median')


# In[68]:


df.pivot_table(values='Profit',index='Segment',columns='Discount',aggfunc='median')


# #### We can conclude that the SuperStore was going on loss for Discount more than 30% and for items having discount b/w 0 to 20% the sales of superstore was average

# In[69]:


temp_df=df.loc[(df['Segment']=='Consumer')&(df['Discount']==0.1)]
temp_df['Profit'].plot.hist(bins=50)


# In[70]:


temp_df=df.loc[(df['Segment']=='Consumer')&(df['Discount']==0.2)]
temp_df['Profit'].plot.hist(bins=50)


# In[71]:


temp_df=df.loc[(df['Segment']=='Corporate')&(df['Discount']==0.8)]
temp_df['Profit'].plot.hist(bins=50)


# In[72]:


temp_df=df.loc[(df['Segment']=='Consumer')&(df['Discount']==0.8)]
temp_df['Profit'].plot.hist(bins=50)


# #### For all the segments when superstore is offering discount less than 40%  its going on Profit as depicted by above graphs and if discount>50%  like we have taken discount=80% ,superstore is going on loss

# In[73]:


temp_df=df.loc[(df['Category']=='Furniture')&(df['Discount']==0.2)]
temp_df['Profit'].plot.hist(bins=50)


# In[74]:


temp_df=df.loc[(df['Category']=='Technology')&(df['Discount']<=0.3)]
temp_df['Profit'].plot.hist(bins=50)


# In[75]:


temp_df=df.loc[(df['Category']=='Technology')&(df['Discount']>=0.3)]
temp_df['Profit'].plot.hist(bins=50)


# In[76]:


temp_df=df.loc[(df['Category']=='Office Supplies')&(df['Discount']<=0.3)]
temp_df['Profit'].plot.hist(bins=50)


# In[77]:


temp_df=df.loc[(df['Category']=='Office Supplies')&(df['Discount']>=0.3)]
temp_df['Profit'].plot.hist(bins=50)


# #### We conclude that when Discount<=30% in items, Sales was going into Profit and  when Discount>=30% in items, SuperStore is experiencing a huge loss
# 

# In[78]:


temp=df.groupby(['Segment','Discount']).Profit.median()
temp.plot(kind='bar',stacked=True)


# #### This shows the Scenario of Profit of all the segments when following Discount was offered by SuperStore

# ## ThankYou!
