import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')
import streamlit as st 

# set the title and description for app
st.title('Lifestyle Data Visualization')
st.write('This application analyzes the Lifestyle data of people for better understanding ')

# import the dataset
data = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\SENAPATI SIR FSDS NOTE\SEPTMBER MONTH DS NOTE\3rd - MOVIE RATING_ADVANCE VISUALIZATION\Sleep_health_and_lifestyle_dataset.csv")
# display the lifestyle data
st.subheader('Display the lifestyle data')
st.dataframe(data)

# distplot
st.subheader('Distplot of Age')
fig,ax = plt.subplots()
m = sns.distplot(data['Age'])
st.pyplot(m.figure)

st.subheader('Distplot of Daily Steps')
fig,ax = plt.subplots()
m1 = sns.distplot(data['Daily Steps'])
st.pyplot(m1.figure)

st.subheader('Distplot of Sleep Duration')
fig,ax = plt.subplots()
m2 = sns.distplot(data['Sleep Duration'])
st.pyplot(m2.figure)

# i want to show the 5 column of Sleep Duration
st.subheader('Displot of Daily Steps shows 5 column')
fig,ax = plt.subplots()
m3 = sns.displot(data['Sleep Duration'], bins = 5)
st.pyplot(m3.figure)

st.subheader('Distplot of Stress level')
fig,ax = plt.subplots()
m4 = sns.distplot(data['Stress Level'])
st.pyplot(m4.figure)

st.subheader('Distplot of Quality of Sleep')
fig,ax = plt.subplots()
m5 = sns.distplot(data['Quality of Sleep'])
st.pyplot(m5.figure)

st.subheader('Distplot of Sleep Duration')
fig,ax = plt.subplots()
m6 = sns.distplot(data['Sleep Duration'])
st.pyplot(m6.figure)

# i eant to show the 12 column of age with back ground colour'darkgrid'
sns.set_style('darkgrid')
st.subheader('Distplot of Age')
fig,ax = plt.subplots()
m7 = sns.distplot(data['Age'],bins = 12)
st.pyplot(m7.figure)
# Hist plot of Stress levele
st.subheader('Hist plot of Stress Levele')
fig,ax = plt.subplots()
sns.set_style('dark')
m8 = plt.hist(data['Stress Level'])
st.pyplot(fig)

# Histplot of Physical Activity Levele and bins = 9
st.subheader('Hist plot of Physical Activity Level')
fig,ax = plt.subplots()
m9 = plt.hist(data['Physical Activity Level'],bins=9)
st.pyplot(fig)

# joinplot 1:scatter
st.subheader('Relation between Age and Sleep Duration')
j = sns.jointplot(data=data,x = 'Age', y = 'Sleep Duration')
st.pyplot(j.figure)

# joinplot 2: scatter
st.subheader('Relation between Age and Physical Activity Level')
j1 = sns.jointplot(data=data,x = 'Age', y = 'Physical Activity Level')
st.pyplot(j1.figure)

# joinplot 3 : Regression
st.subheader('Relation between Age and Sleep Duration')
j2 = sns.jointplot(data=data,x = 'Age', y = 'Sleep Duration',kind = 'reg')
st.pyplot(j2.figure)

# joinplot 4: scatter
st.subheader('Relation between Quality of Sleep and Heart Rate')
j3 = sns.jointplot(data=data,x = 'Quality of Sleep', y = 'Heart Rate')
st.pyplot(j3.figure)

# joinplot 5 : scatter with kind = 'resid'
st.subheader('Relation between Quality of Sleep and Heart Rate')
j4 = sns.jointplot(data=data,x = 'Quality of Sleep', y = 'Heart Rate',kind='resid')
st.pyplot(j4.figure)

# joinplot 6: regression
st.subheader('Relation between Quality of Sleep and Heart Rate')
j5 = sns.jointplot(data=data,x = 'Quality of Sleep', y = 'Heart Rate',kind = 'reg')
st.pyplot(j5.figure)

# joinplot 7: regression
st.subheader('Relation between Heart Rate and Daily Steps')
j6 = sns.jointplot(data=data, x = 'Heart Rate', y = 'Daily Steps',kind = 'reg')
st.pyplot(j6.figure)

# joinplot 8 : Hexabian
st.subheader('Relation between Heart Rate and Daily Steps')
j7 = sns.jointplot(data=data, x = 'Heart Rate', y = 'Daily Steps',kind = 'hex')
st.pyplot(j7.figure)

# Joinplot 9: Hexabian
st.subheader('Relation between Quality of Sleep and Heart Rate')
j8 = sns.jointplot(data=data,x = 'Quality of Sleep', y = 'Heart Rate',kind = 'hex')
st.pyplot(j8.figure)

# joinplot 10:Histohram
st.subheader('Relation between Quality of Sleep and Heart Rate')
j9 = sns.jointplot(data=data,x = 'Quality of Sleep', y = 'Heart Rate',kind = 'hist')
st.pyplot(j9.figure)

# joinplot 11:Hexabian
st.subheader('Relation between Age and Physical Activity Level')
j10 = sns.jointplot(data=data,x = 'Age', y = 'Physical Activity Level',kind ='hex')
st.pyplot(j10.figure)

# joinplot 12:Histogram
st.subheader('Relation between Age and Physical Activity Level')
j11 = sns.jointplot(data=data,x = 'Age', y = 'Physical Activity Level',kind ='hist')
st.pyplot(j11.figure)

# joinplot 13: scatterplot with kind = 'reside'
st.subheader('Relation between Age and Physical Activity Level')
j12 = sns.jointplot(data=data,x = 'Age', y = 'Physical Activity Level',kind ='resid')
st.pyplot(j12.figure)

# Barplot
st.subheader('Bar plot of Age vs Physical Activity level')
b = sns.barplot(data=data, x = 'Age', y = 'Physical Activity Level')
st.pyplot(b.figure)

# Hexabian
st.subheader('Hexabian plot of Age vs Daily Steps')
h = plt.hexbin(data['Age'], data['Daily Steps'], gridsize=30, cmap='Blues')
plt.colorbar(label="Count in bin")
plt.xlabel("Age")
plt.ylabel("Daily Steps")
plt.title("Hexbin plot of Age vs Daily Steps")
st.pyplot(h.figure)

st.subheader('Distribution of Daily Steps')
h1 = plt.hist(data['Daily Steps'], bins=30, color='skyblue')
plt.xlabel("Daily Steps")
plt.ylabel("Frequency")
plt.title("Distribution of Daily Steps")
st.pyplot(fig)

# compair gender of people with Sleep Duration
st.subheader('compair gender of people with Sleep Duration')
h2 = plt.hist([data[data['Gender'] == 'Male']['Sleep Duration'],
    data[data['Gender'] == 'Female']['Sleep Duration']],bins=10,stacked=True,label=['Male','Female'])
plt.xlabel("Sleep Duration")
plt.ylabel("Frequency")
plt.title("Sleep Duration by Gender")
plt.legend()
st.pyplot(fig)

# compair gender of people with Daily Steps
st.subheader('Distribution of Daily Steps by gender')
n3 = plt.hist([data[data['Gender'] == 'Male']['Daily Steps'],
               data[data['Gender'] == 'Female']['Daily Steps']],bins = 10,label = ['Male','Female'],stacked=True)
plt.legend()
plt.xlabel('Dally Steps')
plt.ylabel('No of people')
plt.title("Distribution of Daily Steps by Gender")
st.pyplot(fig)

# Distribution of heart rate by gender
st.subheader('Distribution of heart rate by gender')
n4 = plt.hist([data[data['Gender'] == 'Male']['Heart Rate'],
               data[data['Gender'] == 'Female']['Heart Rate']],bins = 10,label = ['Male','Female'],stacked=True)
plt.legend()
plt.xlabel('Heart rate of people')
plt.ylabel('no of people')
plt.title('Distribution of heart rate by gender')
st.pyplot(fig)

# distribution of stress levele by gender
st.subheader('distribution of stress levele by gender')
n5 = plt.hist([data[data['Gender'] == 'Male']['Stress Level'],
               data[data['Gender'] == 'Female']['Stress Level']],bins = 10,label = ['Male','Female'],stacked=True)
plt.legend()
plt.xlabel('Stress Level')
plt.ylabel('No of people')
plt.legend()
plt.title('Distribution of Stress levele by Gender')
st.pyplot(fig)

# Distribution of blood presser by gender
st.subheader('Distribution of blood presser by gender')
n6 = plt.hist([data[data['Gender'] == 'Male']['Blood Pressure'],
               data[data['Gender'] == 'Female']['Blood Pressure']],bins = 10,label = ['Male','Female'],stacked=True)
values = [4, 69, 5, 0, 31, 45, 33, 0] 
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()  
plt.xlabel('Blood Presser')
plt.ylabel('No of pepole')
plt.title('Distribution of Blood presser by Gender')
plt.legend()
st.pyplot(fig)

# distribution of occopation by gender
st.subheader('distribution of occopation by gender')
n7 = plt.hist([data[data['Gender'] == 'Male']['Occupation'],
               data[data['Gender'] == 'Female']['Occupation']],bins = 10,label = ['Male','Female'],stacked=True)
values = [4, 69, 5, 0, 31, 45, 33, 0] 
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()  
plt.xlabel('Occopation of people')
plt.ylabel('No of people')
plt.title('Distribution of occopation by grnder')
plt.legend()
st.pyplot(fig)

# Distribution of sleep Disorder by gender
st.subheader('Distribution of sleep Disorder by gender')
plt.hist([data[data['Gender']=='Male']['Sleep Duration'],
          data[data['Gender']=='Female']['Sleep Duration']],
         bins=10, label=['Male','Female'], stacked=True)

plt.xlabel("Sleep Duration (hours)")
plt.ylabel("Count")
plt.title("Distribution of Sleep Duration by Gender")
plt.legend()
plt.show()
st.pyplot(fig) 
# st.pyplot(fig) if i do not write this the above code donot show the graph

# Distribution of BMI Category by gender
st.subheader('Distribution of BMI Category by gender')
plt.hist([data[data['Gender']=='Male']['BMI Category'],
          data[data['Gender']=='Female']['BMI Category']],
         bins=10, label=['Male','Female'], stacked=True)
plt.xlabel('BMI Category')
plt.ylabel('No of people')
plt.title('Distribution of BMI Category by gender')
st.pyplot(fig)

# distribution of Age by gender
st.subheader('distribution of Age by gender')
plt.hist([data[data['Gender']=='Male']['Age'],
          data[data['Gender']=='Female']['Age']],
         bins=10, label=['Male','Female'], stacked=True)
plt.xlabel('Age')
plt.ylabel('No of people')
plt.title('Distribution of Age by gender')
st.pyplot(fig)
#LMPLOT
# Relation between sleep duration and age
st.subheader('Relation between sleep duration and age')
vis1 = sns.lmplot(data=data, x = 'Sleep Duration', y ='Age',fit_reg=False )
st.pyplot(vis1.figure)

# Relation between sleep duration and age when fit_reg = True
st.subheader(' Relation between sleep duration and age when fit_reg = True')
vis2 = sns.lmplot(data=data, x = 'Sleep Duration', y ='Age',fit_reg=True)
st.pyplot(vis2.figure)

#  Relation between sleep duration and age when fit_reg = False and hue = 'Occopation'
st.subheader('Relation between sleep duration and age when fit_reg = False and hue = Occopation')
vis3 = sns.lmplot(data=data, x = 'Age', y ='Sleep Duration',fit_reg=False,hue ='Occupation')
st.pyplot(vis3.figure)

#  Relation between sleep duration and Physical Activity Level when fit_reg = False and hue = 'Occopation'
st.subheader('Relation between ageand Physical Activity Level when fit_reg = False and hue = Occopation')
vis4 = sns.lmplot(data=data, x = 'Age', y ='Physical Activity Level',fit_reg=False,hue ='Occupation')
st.pyplot(vis4.figure)

# Relation between Stress level and heart rate
st.subheader('Relation between Stress level and heart rate')
vis5 = sns.lmplot(data=data, x = 'Stress Level', y ='Heart Rate',fit_reg=False,hue ='Occupation')
st.pyplot(vis5.figure)

# Relation between Heart rate and Daily steps
st.subheader(' Relation between Heart rate and Daily steps')
vis6 = sns.lmplot(data=data, x = 'Heart Rate', y ='Daily Steps',fit_reg=False,hue ='Occupation')
st.pyplot(vis6.figure)

#  Relation between sleep duration and Physical Activity Level when fit_reg = False and hue = 'BMI Category',height = 10,aspect = 1
st.subheader('Relation between ageand Physical Activity Level when fit_reg = False and hue = BMI Category')
vis7 = sns.lmplot(data=data, x = 'Age', y ='Physical Activity Level',fit_reg=False,hue ='BMI Category',height= 10,aspect=1)
st.pyplot(vis7.figure)

#KDE PLOT
# KDE plot of Age
st.subheader('KDE plot of Age')
k = sns.kdeplot(data=data, x = 'Age')
st.pyplot()

# KDE plot of sleep duration
st.subheader('KDE plot of sleep duration')
k2 = sns.kdeplot(data= data,x = 'Sleep Duration')
st.pyplot()

#KDE plot of sleep duration
st.subheader('KDE plot of Quality sleep')
k3 = sns.kdeplot(data=data,x= 'Quality of Sleep')
st.pyplot()

#KDE plot of Daily steps
st.subheader('KDE plot of Daily Steps')
k4 = sns.kdeplot(data=data ,x = 'Daily Steps')
st.pyplot()

# Distribution of sleep duration by gender
st.subheader(' Distribution of sleep duration by gender')
k5 = sns.kdeplot(x='Sleep Duration', data=data, hue='Gender', fill=True)
st.pyplot()

# Distribution of Quality sleep by gender
st.subheader('Distribution of Quality sleep by gender')
k6 = sns.kdeplot(data=data, x = 'Quality of Sleep',hue='Gender',fill=True)
plt.title('Quality of Sleep by Gender')
st.pyplot()

# Distribution of Physical activity level by gender
st.subheader('Distribution of Physical activity level by gender')
k7 = sns.kdeplot(data=data, x = 'Physical Activity Level',hue='Gender',fill=True)
plt.title('Physical Activity Level by Gender')
st.pyplot()

# Distribution of Stress level by gender
st.subheader('Distribution of Stress level by gender')
k8 = sns.kdeplot(data=data, x = 'Stress Level',hue='Gender',fill=True)
plt.title('Stress Level by Gender')
st.pyplot()

# Distribution of Quality of sleep with Sleep disorder
st.subheader('Distribution of Quality of sleep with Sleep disorder')
k9 = sns.kdeplot(data=data, x = 'Quality of Sleep',hue='Sleep Disorder',fill=True)
plt.title('Quality Sleep by people with Sleep Disorder')
st.pyplot()

# Distribution of stress level of people with occopation
st.subheader('Distribution of stress level of people with occopation')
k10 = sns.kdeplot(data=data, x = 'Stress Level',hue='Occupation',fill=True)
plt.title('Stress levele of people with occopation')
st.pyplot()

#Distribution of Daily steps of people with occopation
st.subheader('Distribution of Daily steps of people with occopation')
k11 = sns.kdeplot(data=data, x = 'Daily Steps',hue='Occupation',fill=True)
plt.title('Daily Steps of people with occopation')
st.pyplot()

# Distribution of Physical Activity Level of people with occopation
st.subheader(' Distribution of Physical Activity Level of people with occopation')
k12 = sns.kdeplot(data=data, x = 'Physical Activity Level',hue='Occupation',fill=True)
plt.title('Physical Activity Level of people with occopation')
st.pyplot()

# Relation between sleep duration and quality of sleep
st.subheader('Relation between sleep duration and quality of sleep')
k13 = sns.kdeplot(data=data,x = 'Sleep Duration',y ='Quality of Sleep')
st.pyplot()

# when cmap = 'Reds'
st.subheader('Relation between sleep duration and quality of sleep')
k14 = sns.kdeplot(data=data,x = 'Sleep Duration',y ='Quality of Sleep',shade = True,shade_lowest = False,cmap = 'Reds')
st.pyplot()

# Relation betweeen Age and Physical Activity Level
st.subheader('Relation betweeen Age and Physical Activity Level')
k15 = sns.kdeplot(data=data,x = 'Age', y = 'Physical Activity Level',hade = True,shade_lowest = False,cmap = 'Reds' )
st.pyplot()

# Relation between Heart rate and Physical activity levels
st.subheader('Relation between Heart rate and Physical activity levels')
k16 = sns.kdeplot(data=data, x='Heart Rate', y='Physical Activity Level', fill=True, cmap='Reds')
st.pyplot()

# Relation between heart rate with daily sleep
st.subheader('Relation between heart rate with daily sleep')
k17 = sns.kdeplot(data=data, x='Heart Rate', y='Daily Steps', fill=True, cmap='Reds')
st.pyplot()

# Relation between Heart rate with Stress level
st.subheader('Relation between Heart rate with Stress level')
k18 = sns.kdeplot(data=data, x='Heart Rate', y='Stress Level', fill=True, cmap='Reds')
st.pyplot()

# BOX PLOT
# Relation between occopation and stress level
st.subheader('Relation between occopation and stress level')
w = sns.boxplot(data=data,x = 'Occupation', y = 'Stress Level',ax = ax)
st.pyplot(fig)

# Relation between sleep duration and quality of sleep
st.subheader('Relation between sleep duration and quality of sleep')
w1 = sns.boxplot(data=data,x = 'Sleep Duration', y = 'Quality of Sleep',ax = ax)
st.pyplot(fig)

# VIOLINE PLOT
# Relation between occopation with stress level
st.subheader('Relation between occopation with stress level')
v= sns.violinplot(data=data,x = 'Occupation', y = 'Stress Level',ax = ax)
st.pyplot(fig)

# Relation between Heart rate with stress level
st.subheader('Relation between Heart rate with stress level')
v1 = sns.violinplot(data=data,x = 'Heart Rate', y = 'Stress Level',ax=ax)
st.pyplot(fig)

#Relation between Heart rate with Daily steps
st.subheader('Relation between Heart rate with Daily steps')
v2 = sns.violinplot(data=data,x = 'Heart Rate', y = 'Daily Steps',ax=ax)
st.pyplot(fig)

# Relation between Heart rate and BMI category
st.subheader('Relation between Heart rate and BMI category')
v3 =  sns.violinplot(data=data,y = 'Heart Rate', x= 'BMI Category',ax=ax)
st.pyplot(fig)

# Relation between Occopation and stress level
st.subheader('Relation between Occopation and stress level')
v4 =  sns.violinplot(data=data,x= 'Occupation', y= 'Stress Level',ax=ax)
st.pyplot(fig)

# Relation between sleep disorder and stress level
st.subheader(' Relation between sleep disorder and stress level')
v5 = sns.violinplot(data=data,x= 'Sleep Disorder', y= 'Stress Level',ax=ax)
st.pyplot(fig)

# Relation between sleep disorder and daily steps
st.subheader('Relation between sleep disorder and daily step')
v6 = sns.violinplot(data=data,x= 'Sleep Disorder', y= 'Daily Steps',ax=ax)
st.pyplot(fig)

# Relation between sleep disprdor and Blood presser
st.subheader('Relation between sleep disprdor and Blood presser')
v7 = sns.violinplot(data=data,x= 'Sleep Disorder', y= 'Blood Pressure',ax=ax)
st.pyplot(fig)

# Relation between sleep disorder and quality of sleep
st.subheader('Relation between sleep disorder and quality of sleep')
v8 = sns.violinplot(data=data,x= 'Sleep Disorder', y= 'Quality of Sleep',ax=ax)
st.pyplot(fig)

# Relation between sleep disorder and sleep duration
st.subheader('Relation between sleep disorder and sleep duration')
v9 = sns.violinplot(data=data,x= 'Sleep Disorder', y= 'Sleep Duration',ax=ax)
st.pyplot(fig)

# docters stress level
st.subheader('docters stress level')
z = sns.violinplot(data=data[data.Occupation == 'Doctor'],x = 'Occupation', y = 'Stress Level',ax = ax)
st.pyplot(fig)



