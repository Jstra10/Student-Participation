import pandas as pd



class Base:
    """
    Handles data from CSV files.
    """

    def __init__(self, file_paths=[r'C:\Users\jjs61\OneDrive\Desktop\Student_performance\src\data\student-mat.csv', r'C:\Users\jjs61\OneDrive\Desktop\Student_performance\src\data\student-por.csv']):
        self.dfs = {}
        self.combined_df = self.combine_data_from_csv(file_paths)
        self.format_data(self.combined_df)
        self.dfs['combined'] = self.combined_df

    def combine_data_from_csv(self, file_paths):
        '''Combine data from multiple CSV files into a single DataFrame'''
        dataframes = [pd.read_csv(file_path, delimiter=';') for file_path in file_paths]
        self.combined_df = pd.concat(dataframes)
        return self.combined_df

    def format_data(self, df):
        '''Format the data by formatting column titles'''
        df.columns = df.columns.str.replace(' ', '_').str.strip().str.lower()


# csv_file_paths = [r'C:\Users\jjs61\OneDrive\Desktop\Student_performance\src\data\student-mat.csv', r'C:\Users\jjs61\OneDrive\Desktop\Student_performance\src\data\student-por.csv']

# Create an instance of the Base class and process the data
# base_instance = Base(csv_file_paths)







