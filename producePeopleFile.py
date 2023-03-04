import pandas as pd

# making data frame 
data = pd.read_csv("https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv") 
    
# calling head() method  
# storing in new variable 
data_top = data.head() 
    
print(data_top)
# display 
data_top 