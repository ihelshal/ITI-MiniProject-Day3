# In[1]: Import Packages

import pandas as pd

from Connector2SQLite import SQLite

# In[2]:

# obj_db = SQLite(database_name='/Users/ihelshal/Kaggle/ITI/PythonDS/ITI-MiniProject-Day3/netfilx')
# df = obj_db.get_tables("SELECT * FROM NetFlix;")
# obj_db.terminate_connection()

# df.to_csv('netfilx.csv', index=False)


df = pd.read_csv("final_ouput.csv")
db_Obj = SQLite(
    database_name="/Users/ihelshal/Kaggle/ITI/PythonDS/ITI-MiniProject-Day3/OutputTable"
)
db_Obj.create_table(df, "OutputTable")
db_Obj.insert("OutputTable", df)
