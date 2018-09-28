#Library imports
from __future__ import division
import pandas as pd
import math
import numpy

#reading the tennis dataset
tennis = pd.read_csv("/home/anand/Desktop/Tennis")

#Basic information about the dataset
print("Dataset Information is as follows")
tennis.info()

#storing the attributes of the dataset in a list
attributes = list(tennis.columns.values)

#removing the classification class from the list
attributes.remove('Play')

#Displaying the attribute list
print("The attributes are {}").format(attributes)

#Describing the dataset
print("Description of the dataset")
print(tennis.describe())


#The function to calculate entropy of the dataset

def entropy(unique_ele, attr):
    for i in unique_ele:
        #Filtering out all rows for a particular attribute attr
        tennis_attr = tennis[(tennis[attr] == i)]
                
        try:
            if 'yes' in tennis_attr.Play.unique().tolist():
                pos = tennis_attr.Play.value_counts().yes
            else:
		#If none of the filtered rows belong to class yes
                pos = 0
            
            if 'no' in tennis_attr.Play.unique().tolist():
                neg = tennis_attr.Play.value_counts().no
            else:
		#If none of the filtered rows belong to class no
                neg = 0
            

            if pos > 0:
		#If atleast one of the filtered rows belong to class yes, calc1 stores the entropy for yes class
                calc1 = (pos/tennis_attr.count()[0])*(math.log(pos/tennis_attr.count()[0],2))
            else:
		#If none of the filtered rows belong to class yes 
                calc1 = 0
            
            if neg > 0:
		#If atleast one of the filtered rows belong to class no, calc2 stores the entropy for no class
                calc2 = (neg/tennis_attr.count()[0])*(math.log(neg/tennis_attr.count()[0],2))
            else:
		#If none of the filtered rows belong to class no 
                calc2 = 0
            

            print("Entropy of {} given {} is {}").format(attr, i, -calc1-calc2)
        except Exception as e:
            print("The exception is ", e)



#main function definition to call the entropy function for each column

def main():
    for attr in attributes:
        unique_ele = tennis[attr].unique().tolist()
	print("Unique elements of {} attribute are").format(attr)
        print(unique_ele)
        entropy(unique_ele, attr)
        
if __name__== "__main__":
    main()
