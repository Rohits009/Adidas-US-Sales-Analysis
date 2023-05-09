#!/usr/bin/env python
# coding: utf-8

# # Adidas US Sales Analysis

# #### Importing Necessary Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import warnings
warnings.filterwarnings ("ignore")


# #### Importing the data

# In[2]:


data = pd.read_excel("Adidas US Sales Datasets.xlsx")


# In[3]:


data


# #### Exploratory data analysis

# In[4]:


data.isnull().sum()


# In[5]:


data.shape


# In[6]:


data.size


# In[7]:


data.ndim


# In[8]:


data.describe()


# In[9]:


data.dtypes


# #### Renaming the columns

# In[10]:


data = data.rename(columns = {"Units Sold":"Quantity","Operating Profit":"Profit","Operating Margin":"Margin"})
data


# #### Changing the format of datetime

# In[11]:


data["Month"] = data["Invoice Date"].dt.month_name()
data['year'] = data['Invoice Date'].dt.year


# In[12]:


data


# ### Data Analysis

# #### Checking correlation

# In[13]:


sns.heatmap(data.corr(), annot = True)


# #### Regionwise top selling and profit product

# In[14]:


Region_top_product = data.groupby(['Region','Product'])['Total Sales','Profit'].sum()
Region_top_product['sales_rank'] = Region_top_product.groupby('Region')['Total Sales'].rank(ascending = False)
Region_top_product['Profit_rank'] = Region_top_product.groupby('Region')['Profit'].rank(ascending = False)
Region_top_product = Region_top_product.loc[(Region_top_product['sales_rank'] == 1.0) & (Region_top_product['Profit_rank']==1.0)].reset_index()
Region_top_product


# In[19]:


sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(x='Region', y='Total Sales', hue='Product', data = data)
plt.title('Top Selling and Profitable Products by Region', fontsize = 20)
plt.xlabel('Region')
plt.ylabel('Sales (in thousands)')
plt.show()


# In[24]:


top_5_States = data.groupby('State')['Profit'].sum().sort_values(ascending = False).reset_index()
top_5_States = top_5_States[['State','Profit']].head(5)
top_5_States


# In[26]:


sns.barplot(x='Profit', y='State', data=top_5_States)
plt.title('Top 5 Profitable States', fontsize = 20)
plt.xlabel('Profit (in thousands)')
plt.ylabel('State')
plt.show()


# #### Bottom 5 States

# In[29]:


Bottom_5_States = data.groupby('State')['Profit'].sum().sort_values(ascending = True).reset_index()
Bottom_5_States = Bottom_5_States[['State','Profit']].head(5)
Bottom_5_States


# In[41]:


sns.barplot(y = 'Profit', x='State', data = Bottom_5_States)
plt.title('Bottom 5 States by Profit',size = 20)
plt.xlabel ('States', size = 17)
plt.ylabel('Profit (in thousands)', size = 17)
plt.show()


# #### Top 5 Profitable cities

# In[42]:


Top_5_Cities = data.groupby('City')['Profit'].sum().sort_values(ascending = False).reset_index()
Top_5_Cities=Top_5_Cities[['City','Profit']].head(5)
Top_5_Cities


# In[51]:


plt.pie(Top_5_Cities['Profit'], labels = Top_5_Cities['City'], autopct='%1.1f%%')
plt.title('Top 5 Cities by Profit',size = 20)
plt.show()


# #### Yearwise Sales by Retailer 

# In[76]:


retailer_sales = data.groupby(['Retailer','year'])['Total Sales'].sum().reset_index()
retailer_sales


# In[77]:


retailer_sales = retailer_sales.set_index('Retailer')
sns.set(rc={'figure.figsize':(20,10)})
sns.barplot(x=retailer_sales.index, y='Total Sales', hue='year', data=retailer_sales)
plt.title('Year-wise Retailer Sales Analysis',size = 20)
plt.xlabel('Retailer', size = 16)
plt.ylabel('Sales', size = 16)
plt.legend(title='Year')
plt.show()


# #### Quarterly sales analysis by each retailer

# In[78]:


data['quarter'] = pd.PeriodIndex(data['Invoice Date'], freq = 'Q')
data


# In[79]:


quarterly_sales_retailer = data.groupby(['Retailer','quarter'])['Total Sales'].sum().reset_index()
quarterly_sales_retailer['rank'] = quarterly_sales_retailer.groupby('Retailer')['Total Sales'].rank(ascending = False)
quarterly_sales_retailer = quarterly_sales_retailer.loc[quarterly_sales_retailer['rank'] == 1.0]
quarterly_sales_retailer


# In[82]:


sns.barplot(x='Retailer', y='Total Sales', hue='quarter', data=data)
plt.title('Quarterly Sales by Retailer', size = 20)
plt.xlabel('Retailer',size=16)
plt.ylabel('Sales (in thousands)',size=16)
plt.show()


# In[ ]:




