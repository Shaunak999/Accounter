import pandas as pd 
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    csv_file = 'financial_data.csv'
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%y"
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.csv_file, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description 
        }        

        with open(cls.csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

def get_transections(cls,start_date,end_date):
    df = pd.read_csv(cla.CSV_FILE)
    df["date"] = pd.to_datetime(df["date"],format=CSV.FORMAT)
    start_date = datetime.strptime(start_date,CSV.FORMAT)
    end_date = datetime.strptime(end_date,CSV.FORMAT)

    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    filtered_df = df.loc[mask]

    if filtered_df.empty:
        print("no transections found in ths timeframe")
    else:
        print(f"transections from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")    


def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy): ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(date, amount, category, description)

add()
