from base import Base
import pymongo
import os
from dotenv import load_dotenv


class ToMongo(Base):
    '''
    Designed as a class to transport the data from our Base class to a MongoDB instance.
    Initializes an instance of the inherited class.
    
    Defined methods are as follows:
    upload_one_by_one: Upload pieces of information to a database one by one over an iterable structure.
    upload_collection: Uploads an entire collection of documents to MongoDB.
    delete_collection: Drops an entire collection of data from the database.
    '''

    def __init__(self):
        # initializing the class
        Base.__init__(self)
        load_dotenv()
        self.__mongo_url = os.getenv('MONGO_URL')

        # Connect to pymongo
        self.client = pymongo.MongoClient(self.__mongo_url)
        # Create/Connect to the database and collection
        self.db = self.client.db
        self.student_info = self.db.student_info
        
        # Set the dataframe index to the student_id column
        # self.df.set_index('id', inplace=True)

    def upload_one_by_one(self):
        for student_id, row in self.combined_df.iterrows():
            self.student_info.insert_one(row.to_dict())

    def upload_collection(self):
        """Upload entire data set. There is a maximum size you can upload at once"""
        self.student_info.insert_many(self.combined_df.to_dict(orient='records'))

    def drop_collection(self):
        """Drops data set"""
        self.db.drop_collection('student_info')

if __name__ == '__main__':
    csv_file_paths = [r'C:\Users\jjs61\OneDrive\Desktop\Student_performance\src\data\student-mat.csv', r'C:\Users\jjs61\OneDrive\Desktop\Student_performance\src\data\student-por.csv']
    base_instance = Base(csv_file_paths)
    
    # Access the combined and formatted DataFrame from Base class
    combined_df = base_instance.dfs['combined']

    to_mongo_instance = ToMongo()

    print('Successful Connection to Client Object')
    to_mongo_instance.drop_collection()
    print('Dropped the collection')
    to_mongo_instance.upload_collection()
    print('Successfully uploaded all data')




    