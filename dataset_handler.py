import pandas as pd

class DatasetHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.filepath)
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data['Home/Away'] = self.data['Home/Away'].map({'Home': 1, 'Away': 0})
        self.data[['Home_Score', 'Away_Score']] = self.data['Score'].str.split('-', expand=True).astype(int)
        self.data.drop(columns=['Score'], inplace=True)

    def get_data(self):
        return self.data