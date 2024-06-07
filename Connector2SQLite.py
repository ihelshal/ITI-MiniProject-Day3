# In[1]: Import Packages

import sqlite3
from sqlite3 import Error

import pandas as pd

# In[2]: Create Class for SQLite3 with Multiple Methods [Create Table - Get Tables - SQL Connection - Insert in Tables]


class SQLite:
    def __init__(self, database_name: str = None) -> None:
        """
        Init Connection to Datbase
        """
        self._connection = sqlite3.connect(database_name)

    def get_tables(self, query: str, bach_size: int = 100000) -> pd.DataFrame:
        try:
            cur = self._connection.cursor()
            cur.execute(query)

            rows = []
            while True:
                batch = cur.fetchmany(bach_size)
                if not batch:
                    break
                rows.extend(batch)

            columns = [col[0] for col in cur.description]
            df = pd.DataFrame(rows, columns=columns)

            if df.empty:
                print("Tables exist but is empty.")
                return None
            else:
                return df
        except sqlite3.Error as e:
            print("Error executing SQL Query.")

    def create_table(self, df: pd.DataFrame, table_name: str = None) -> None:
        try:
            df.to_sql(table_name, self._connection, if_exists="fail", index=False)
            print(table_name, "is created.")
        except Error:
            print(Error)
        return None

    def insert(self, table_name, df):
        try:
            cur = self._connection.cursor()
            for i in range(len(df)):
                cur.execute(
                    "insert into {} values (?,?,?,?)".format(table_name),
                    (
                        str(df["type"][i]),
                        str(df["country"][i]),
                        str(df["target_ages"][i]),
                        str(df["year_added"][i]),
                    ),
                )
                self._connection.commit()
        except:
            self._connection.rollback()
            raise Exception("Error")

    def terminate_connection(self) -> None:
        self._connection.close()
