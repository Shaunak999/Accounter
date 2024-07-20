import pandas as pd 
import csv
from datetime import datetime

class CSV:
    csv_file = 'financial_data.csv'
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.csv_file, index=False)

CSV.initialize_csv()
