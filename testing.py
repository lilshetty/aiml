import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv("PlayTennis.csv")
print("The first 5 lines of data : \n",data.head())

x=data.iloc[:,:-1]
print("The first 5 lines train data : \n",x.head())

y=data.iloc[:,-1]
print("The first 5 lines output data : \n",y.head())

le=LabelEncoder()

x.loc[:,'Outlook']=le.fit_transform(x['Outlook'])
x.loc[:,'Temperature']=le.fit_transform(x['Temperature'])
x.loc[:,'Humidity']=le.fit_transform(x['Humidity'])
x.loc[:,'Wind']=le.fit_transform(x['Wind'])
print("Now train data : \n",x.head())

y=le.fit_transform(y)
print("Now train output : \n",y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

classifier=GaussianNB()
classifier.fit(x_train,y_train)

print("Accuracy : ",accuracy_score(classifier.predict(x_test),y_test))