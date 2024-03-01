#!/usr/bin/env python
# coding: utf-8

# **Data analysis project**

# PROJECT SUMMARY:
#       we have provided with a california  housing dataset where they have mentioned the latitude,longitude,housing prices and their median income of the people.in this dataset they have provided with a sample data of the people living accordng to their budget.its showing us the entire population as well.we can say that the overall data is given to take the sample estimation of how people are living as per their standards.
#       This data set has around 20640 Rows and 10 columns and its a mix between categorical and numerical values.

# In[1]:


import pandas as pd #importing libraries
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('housing.csv') #reading or importing csv file


# In[3]:


df.head(10) #finding the n number of rows from the data


# In[4]:


df.shape #we use shape to find thetotal rows and columnscv


# In[5]:


df.info() #getting information about the data


# In[6]:


df["ocean_proximity"].value_counts() #categorical variable data


# In[7]:


df.describe() #descriptive statistics


# 1.What is the average median income of the data set and check the distribution of data using appropriate plots. Please explain the distribution of the plot.

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[9]:


df['median_income'].mean() #finding average median income of the given dataset


# In[10]:


df.hist(edgecolor="black",bins=50,figsize=(10,8)) #to deal with one numeric data we can use histogram 


# **Observation :As we can see that above graphs shows the that the house value of the people is too high as per their increasing of incomes the values of the houses are also high**

# 2. Draw an appropriate plot to see the distribution of housing_median_age and explain your observations.

# In[11]:


plt.hist(df.housing_median_age,color="r",edgecolor="black",bins=15) ##Using a histogram to show the single numerical data# Creating  a histogram to visualize the distribution of median_income
plt.xlabel("housing_median_age")
plt.ylabel("frequency")
plt.title("Calculating distribution of housing_median_age")
plt.show()


# Observation: in the above graph we comes to know that the people having median age between 35 - 38are are having the higher income.as we can see that the people having more income are opting to have a better standard of living

# 3.Show with the help of visualization, how median_income and median_house_values are related?

# In[12]:


# Creating a scatter plot
plt.figure(figsize=(8, 6))  # we can Adjust the figure size as well
plt.scatter(df.median_income, df.median_house_value, alpha=0.7, color='b',edgecolor="black")

# Add labels and title
plt.xlabel("Median Income")
plt.ylabel("Median House Values")
plt.title("Relationship between Median Income and Median House Values")

# Display the plot
plt.show()                      #as we see that  oth are continuous data 


# **observation::As the points generally moving upwards from left to right, it suggests a positive correlation: areas with higher median incomes tend to have higher median house values.in our scenario as we can see that the graph is moving towards the left to right that means the people having higher incomes are moving towards to higher pricing houses.somewhat its showing a slight differnce inbetween median incomes and hosue value may be due to their own choices some people tend to locate at the same place.overall there is a positive correlation we can say**

# 4.Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.

# In[13]:


df.isna().sum() #it will count the number of null values are there.


# In[14]:


df_New_data=df.dropna() #removing rows where values are null
df_New_data #created new data set by removing certain rows of null values


# In[15]:


df_New_data.isna().sum() #it will give the total null values


# In[16]:


df.dropna(subset= ["total_bedrooms"]) #dropping specific column rows from the data


# 5. Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.

# In[17]:


df


# In[8]:


df2=df.fillna(value=df.mean()) #filling the null values with the mean values
df2 #created a new dtat set which comntains the null values as mean


# In[9]:


df2.isna().sum()


# 6. Write a programming construct (create a user defined function) to calculate the median value of the data set wherever required.

# In[10]:


import pandas as pd #importing library
df=pd.read_csv('housing.csv') #for calculation of median on dataset we need to import data first


# In[11]:


def median_value(df2):
  New_sorted_data=sorted(df2)
  n=len(New_sorted_data)


  if n % 2 == 1:                               #as u can see that it will print the odd numbers
        median = New_sorted_data[n // 2]
  else:                                        # as u can see that it will print th Even number of elements
        middle1 = New_sorted_data[(n - 1) // 2]
        middle2 = New_sorted_data[n // 2]
        median = (middle1 + middle2) / 2

  return median


#calculating median of total bedrooms

median_total_bedrooms = median_value(df2['total_bedrooms'])
print("Total_Median_Bedrooms:", median_total_bedrooms)

#calculating median of population
median_total_population =median_value(df2["population"])
print ("Total_median_population:",median_total_population)

#calculating median of median_house_value
median_house_value =median_value(df2["median_house_value"])
print("total median of house value:",median_house_value)


# 7. Plot latitude versus longitude and explain your observations.

# In[12]:


#Extracting latitude and longitude
latitude=df2["latitude"]
longitude=df2["longitude"]
latitude
longitude


# In[13]:


#creating a scatter plot to see the relationship between both
plt.figure(figsize=(10,8))    #As we know that scatter plot is commonly used to visualize the relationship between two numerical variables.
plt.scatter(longitude,latitude,facecolor="red",marker="D",alpha=0.5)
plt.title("latitude VS longitude")
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.show()


# **observation: As the points generally moving upwards from right to left, it suggests a negative correlation:as we can see that its showing the negative correlation between both the longitude and the latitude**

# 8. Create a data set for which the ocean_proximity is ‘Near ocean’.

# In[14]:


import pandas as pd #importing library
df=pd.read_csv('housing.csv') #as we know that firstly we have to import the file


# In[18]:


filtered_data=df2[df2['ocean_proximity']=="NEAR OCEAN"] #it will give the data by filtering neccesary data.


# In[19]:


filtered_data


# In[17]:


df2["ocean_proximity"].value_counts() #by this value count we can know that how many values are there in a particular column


# 9. Find the mean and median of the median income for the data set created in question 8.

# In[ ]:


filtered_data["median_income"].mean() #it will find the average of the data by using mean


# In[ ]:


filtered_data["median_income"].median() #it will find the median value


# 10. Please create a new column named total_bedroom_size. If the total bedrooms is 10 or less, it should be quoted as small. If the total bedrooms is 11 or more but less than 1000, it should be medium, otherwise it should be considered large.

# In[7]:


df['total_bedroom_size']=["small" if x<=10 else "large" for x in df.total_bedrooms]
df.head(20)


# In[6]:


df["total_rooms"].count()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




