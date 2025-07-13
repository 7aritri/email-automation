from datetime import date
import pandas as pd
from send_email import  send_email
# SHEET_ID="1zjskYh6lsk2lKjDJLsSClM0NyL40v1GyrBZQBLnTR3c"
# SHEET_NAME="Sheet1"
# URL=f"hppts://docs.google.com/spreadsheets/d/{SHEET_ID}/givz/tq?tqx=out:csv&sheet={SHEET_NAME}"
#FOR  UNRESTRICTED GOOGLE SHEET

# Load the Excel file
file_path = "data111.xlsx"  
# data = pd.read_excel(file_path) #reading data from excel
 
# Display the first few rows of the data
# print(type(data.head()))
# c=data.columns.ravel()
# d={}
# for i in c:
#     d[i]=data[i].tolist()

def df_date_time(file_path):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    columns=["due_date","remainder_date"]
    # Convert specified columns to datetime
    for column in columns:
        df[column] = pd.to_datetime(df[column], errors='coerce')  # Coerce invalid dates to NaT
    
    return df
def query_data_and_send_emails(df):
    present=date.today()

    email_counter=0
    for  _,row in df.iterrows():
        
        if(present>=row["remainder_date"].date()) and row["has_paid"]=="no" :
            send_email(
                subject=f'[MEAW] Invoice: {row["invoice_no"]}',
                receiver_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%d, %b %Y"),  # example: 11, Aug 2022
                invoice_no=row["invoice_no"],
                amount=row["amount"],
                )
            email_counter+=1
    return f"Total number of emails sent: {email_counter}"
df=df_date_time(file_path)
print(query_data_and_send_emails(df))
