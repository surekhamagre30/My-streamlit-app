#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# In[4]:


#loading dataset
# Read and store content of Excel file
read_file = pd.read_excel("Telco_customer_churn.xlsx")
# Write the dataframe object into csv file
read_file.to_csv("Telco_customer_churn.csv", index = None, header = True)
# Read csv file and convert into a dataframe object
df = pd.DataFrame(pd.read_csv("Telco_customer_churn.csv"))
# Show dataframe
df


# In[5]:


# Preprocessing the Dataset
# Check for missing values
print(df.isnull().sum())
# There is no missing values, outliers in the dataset


# ## Peforming EDA

# In[6]:



# Print the shape of the data
df = df.sample(frac=0.1, random_state = 1)
print(df.shape)
print(df.info())


# In[7]:


df.head(10)


# In[8]:


df.tail(10)


# In[9]:


df.City.unique()


# In[10]:


df[df["City"]=="Los Angeles"]


# In[11]:


df[df["City"]=="San Francisco"]


# In[12]:


df.describe()


# In[13]:


pd.DataFrame.duplicated(df)


# In[14]:


import plotly.express as px

import streamlit as st

# Create a sidebar
st.sidebar.title("Customer Churn Dashboard")

# Add a slider to select the number of months to display
num_months = st.sidebar.slider("Number of months", 1, 12, 6)

# Add a checkbox to select whether to show the filters
show_filters = st.sidebar.checkbox("Show filters")

# Add the filters
if show_filters:
    st.sidebar.markdown("**Filters**")
    for column in ["Gender", "SeniorCitizen", "InternetService", "OnlineSecurity", "OnlineBackup",
                   "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"]:
        selected_values = st.sidebar.multiselect(column, df[column].unique(), default=df[column].unique())
        df = df[df[column].isin(selected_values)]

# Create a plot of the churn rate over time
churn_rate = df.groupby("Contract")["Churn Score"].mean().reset_index()

# Create an interactive plot using Plotly Express
fig = px.line(churn_rate, x="Contract", y="Churn Score", title="Churn Rate by Contract Type")
st.plotly_chart(fig)

# Add a table of the customer churn data
st.table(df)

# Run the app
if __name__ == "__main__":
    st.write(df)


# In[ ]:




