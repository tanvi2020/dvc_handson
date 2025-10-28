import pandas as pd 
import os 

data={'Name':['Tanvi','Riya','Priya'],
        'Age':[20,25,30],
        'City':['Pune','Mumbai','Nashik']}

df=pd.DataFrame(data)

data_dir='data' # Folder Name 
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")
