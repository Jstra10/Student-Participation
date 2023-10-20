import pandas as pd
from pathlib import Path
from base import Base
from to_mongo import ToMongo
import re 
# import spacy 
# from sklearn.pipeline import make_pipeline
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors
# import pickle


# Set folder directory
folder_dir = f'{Path(__file__).parents[0]}\\data'

# create csv file from dataframe we created in the base class

Base().combined_df.to_csv(f'{folder_dir}\\student_data.csv', index=False)
print('Saved New student data file to CSV')


# # Update the database
# ToMongo().drop_collection_dynamic()
# print('Successfully dropped all items')
# ToMongo().upload_one_by_one()
# print('Successfully updated the collection')
# # Read in the dataframe from the CSV
# df = pd.read_csv(f'{folder_dir}\\studant_data.csv', low_memory=False)
# print('Created the Dataframe object')

# # drop all null values and any empty strings
# df.dropna(subset=['oracle_text'], axis=0, inplace=True)
# df.drop(df.index[df['oracle_text']==''],inplace=True)
# print('Dropped all values that were either null or empty')



 