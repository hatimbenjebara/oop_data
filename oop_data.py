import pandas as pd

class DataFrameregular:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
    
    def get_dataframe(self):
        return self.df
    def info_data(self):
        print(self.df.head())
        print(self.df.dtypes)
        print(self.df.describe().transpose()) 
        print(self.df.tail()) #show bottom 5 records of the dataset
        a1=self.df.shape
        print(a1) # show the number of rows and columns 
        print(self.df.size) #show number of total values in the dataset
        print(self.df.columns) #show each column name 
    def duplicate_data(self):
        # find duplicate record in this dataset and if there's any one remove it 
        print(self.df.duplicated()) # check every row wise nd detect the duplicate rows
        print(self.df[self.df.duplicated()]) # show duplicated rows
        self.df.drop_duplicates(inplace = True)# remove the duplicate rows permanently and inplace = True to make a changes
    def null_data(self):
        #check if there s any null values in our data
        a1=self.df.shape
        print(self.df.isnull())# to show where null value is present if is null then true if not then its false 
        print(self.df.isnull().sum()) #show the count of null values in each column
        a2=self.df.shape
        print(a2)
        if a1==a2 :
            print("there's no duplicate in data")
        else:
            print("we had a duplicate and we had removed it ")
    def select_columns(self,name1,name2,col1):
        print(self.df[self.df[name1].isin([name2])])
        a = self.df[self.df[name1].isin([name2])]
    def add_column(self, name, values):
        self.df[name] = values
    def drop_column(self, name):
        self.df.drop(columns=[name], inplace=True)  
    def filter_rows(self, condition):
        self.df = self.df[condition]
data = pd.read_csv('Uber.csv')
regular = DataFrameregular(data)
print(regular.info_data())
print(regular.duplicate_data())
print(regular.null_data())
regular.drop_column('STOP*')
print(regular.get_dataframe())
regular.filter_rows(regular.get_dataframe()['MILES*'] != '5.1')
print(regular.get_dataframe())
