
# coding: utf-8

# # Titanic: Machine Learning from Disaster

# In[1]:


#Import Modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#Initial Exploration of dataset
data = pd.read_csv('C:/OTHER_THAN_C_FOLDERS/Training/DataScience/Kaggle/Titanic/Try_with_matlab/train_orig.csv',sep=',')


# In[5]:


data.shape


# In[6]:


data.head()


# In[8]:


#DATA
#PassengerId - type should be integers
#Survived - Survived or Not
#Pclass - Class of Travel
#Name - Name of Passenger
#Sex - Gender
#Age
#SibSp - Number of Sibling/Spouse aboard
#Parch - Number of Parent/Child aboard
#Ticket
#Fare
#Cabin
#Embarked - The port in which a passenger has embarked. C - Cherbourg, S - Southampton, Q = Queenstown


# In[10]:


#How Unique Ticket is
ticket = data['Ticket'].unique().tolist()
len(ticket)


# In[11]:


#How Unique Cabin numbers are 
cabin = data['Cabin'].unique().tolist()
len(cabin)


# In[12]:


data.head(15)


# In[13]:


#is any row NULL ?
data.isnull().any().any(), data.shape


# In[14]:


data.isnull().sum(axis=0)


# So we have 'null' values in 'Age','Cabin','Embarked' columns
# Let's check relationships of Cabin and Embarked with other columns, see if we can drop these columns

# In[15]:


data.info()


# In[16]:


data.describe()


# In[17]:


data.describe(include='all')


# In[3]:


#Check test dataset
data_test = pd.read_csv('C:/OTHER_THAN_C_FOLDERS/Training/DataScience/Kaggle/Titanic/Try_with_matlab/test_orig.csv',sep=',')


# In[21]:


data_test.shape


# In[22]:


data_test.head()


# In[23]:


data_test.info()


# Age and Fare have null values

# #### 1. CORRECT The Data

# In[6]:


data['Embarked'].mode()


# In[7]:


data['Embarked'].mode()[0]


# In[4]:


data['Age'].fillna(value=data['Age'].median(),inplace=True)
data.info()


# In[5]:


data['Embarked'].fillna(value=data['Embarked'].mode()[0],inplace=True)
data.info()


# In[6]:


data_test['Fare'].fillna(value=data_test['Fare'].median(),inplace=True)
data_test.info()


# In[7]:


data_test['Age'].fillna(value=data_test['Age'].median(),inplace=True)
data_test.info()


# ### 2. CLEAN the data
# Convert Categorical values to numerical ones
# 
# We will use onehotencoding

# In[8]:


data.columns


# In[9]:


col_y = ['Survived']
col_x = ['Pclass', 'Sex', 'Age', 'SibSp',
       'Parch', 'Fare', 'Embarked']


# In[12]:


data.head()


# In[14]:


data.head()


# In[10]:


data_2 = pd.get_dummies(data, columns=['Sex','Embarked'])


# In[11]:


data_2.columns


# In[12]:


data_2.head()


# In[16]:


col_x = ['Pclass','Age','SibSp','Parch','Fare','Sex_female','Sex_male','Embarked_C','Embarked_Q','Embarked_S']


# In[17]:


data_2.info()


# In[29]:


data_2.shape


# In[18]:


data_2_x = data_2[col_x]


# In[31]:


data_2_x.shape


# In[19]:


data_2_x.head()


# In[20]:


data_2_y = data_2[col_y]


# In[34]:


data_2_y.info()


# #### Let's split Training data in 75/25 ratio
# ##### We will use 75% data to train the model, Rest 25% we will use for Cross Validation (model accuracy)

# #### Time to import sklearn :)

# In[21]:


from sklearn.model_selection import train_test_split


# In[22]:


x_train, x_test, y_train, y_test = train_test_split(
    data_2_x, data_2_y, test_size=0.25, random_state=42)


# Check correlation between datasets

# In[23]:


import seaborn as sns


# In[24]:


def heatMap(self, df):
    """
    Params: df - DataFrame of our Abalone data
    Return: Generates a heatmap plot
    """
    #Create Correlation df
    
    corr = df.corr()
    #Plot figsize
    fig, ax = plt.subplots(figsize=(12, 10))
    #Generate Color Map, red & blue
    colormap = sns.diverging_palette(220, 10, as_cmap=True)
    #Generate Heat Map, allow annotations and place floats in map
    sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
    #Apply xticks
    plt.xticks(range(len(corr.columns)), corr.columns);
    #Apply yticks
    plt.yticks(range(len(corr.columns)), corr.columns)
    #show plot
    plt.show()


# In[25]:


heatMap(data_2,data_2)


# In[38]:


# Drop Self Correlations
# Not Working, will look into it later
def halfHeatMap(df, mirror):
    # Create Correlation df
    corr = df.corr()
    # Plot figsize
    fig, ax = plt.subplots(figsize=(10, 10))
    # Generate Color Map
    colormap = sns.diverging_palette(220, 10, as_cmap=True)
    if mirror == True:
        #Generate Heat Map, allow annotations and place floats in map
        sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
        #Apply xticks
        plt.xticks(range(len(corr.columns)), corr.columns);
        #Apply yticks
        plt.yticks(range(len(corr.columns)), corr.columns)
        #show plot
        
    else:
        # Drop self-correlations
        dropSelf = np.zeros_like(corr)
        dropSelf[np.triu_indices_from(dropSelf)] = True# Generate Color Map
        colormap = sns.diverging_palette(220, 10, as_cmap=True)
        # Generate Heat Map, allow annotations and place floats in map
        sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f", mask=dropSelf)
        # Apply xticks
        plt.xticks(range(len(corr.columns)), corr.columns);
        # Apply yticks
        plt.yticks(range(len(corr.columns)), corr.columns)
        #show plot
        plt.show()
        
    plt.show()


# In[39]:


#halfHeatMap(data_2,data_2)


# ### Now the data is clean, let's move to Model

# Let's First use logistic regresstion
# 
# We will use other algoritms later

# In[41]:


# import Logistic regression from sklearn
from sklearn.linear_model import LogisticRegression


# In[42]:


logreg = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(x_train, y_train)


# In[43]:


y_train.info()


# In[44]:


y_train.shape


# In[47]:


from sklearn.utils import validation


# In[49]:


y_train_2 = validation.column_or_1d(y_train, warn=True)


# In[54]:


y_train['Survived'].head()


# In[55]:


y_train_2 = y_train.as_matrix(columns = y_train['Survived'])


# In[57]:


y_train_2.shape


# In[58]:


y_train.columns


# In[62]:


y_train.columns[1:]


# In[63]:


y_train.columns


# In[74]:


y_train.iloc[:,:].values


# In[75]:


y_train.info()


# In[76]:


y_train_2 = y_train.iloc[:,:].values


# In[77]:


y_train_2


# In[78]:


y_train_3 = validation.column_or_1d(y_train_2, warn=True)


# In[79]:


y_train_3 = y_train_2.ravel()


# In[80]:


y_train_3[1:5]


# In[81]:


y_train_3.shape


# In[82]:


y_train_3


# In[83]:


y_train


# In[84]:


logreg = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(x_train, y_train_3)


# In[87]:


logreg.predict(x_train)


# In[88]:


logreg.predict_proba(x_train)


# In[89]:


logreg.score(x_train,y_train_3)


# In[94]:


y_test.iloc[:,:].values


# In[96]:


y_test_2 = y_test.iloc[:,:].values
y_test_2.ravel()
y_test_2[:5]


# In[99]:


type(y_train)


# In[105]:


y_predict_train = logreg.predict(x_train)


# In[106]:


type(y_predict_train)


# In[107]:


from sklearn.metrics import accuracy_score


# In[108]:


#accuracy_score(y_true = y_train, y_pred = y_predict_train)
y_predict_train[:5]


# In[109]:


accuracy_score(y_true = y_train, y_pred = y_predict_train)


# In[110]:


#Test on cross validation set
y_predict_test = logreg.predict(x_test)
accuracy_score(y_true = y_test, y_pred = y_predict_test)


# In[118]:


data_test.head()


# In[117]:


# Now, prepare test data and predict on this data using logistic regression technique

data_test = pd.get_dummies(data_test, columns=['Sex','Embarked'])


# In[119]:


data_test_x = data_test[col_x]

#y = logreg.predict(data_test_x)


# In[120]:


y = logreg.predict(data_test_x)


# In[121]:


y[:10]


# In[122]:


len(y)


# In[147]:


np.savetxt('C:\OTHER_THAN_C_FOLDERS\Training\DataScience\Kaggle\Titanic\predict.txt', y, delimiter=',',fmt = '%d')


# In[148]:


data_test_x.head(10)

