import os
import sqlite3

class DbHelper:
    """
    A simple Database helper class.
    
    The only thing you should need to change in this file is the name
    of your SQLite database file.
    """
    
    db = None
    filename = 'ISF_SQL.sqlite3'
    
    @classmethod
    def get_cursor(cls):
        """
            Other than changing the filename,
            you should not need to change this method.
        """
        db_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), # the folder the app is running from
            'data',     # The data folder, according to the example app structure
            cls.filename    # The filename (duh!), as set in the class variable
            )
        cls.db = sqlite3.connect(db_path, isolation_level=None)
            # isolation_level=None sets it to auto-commit DML statements
            # Without this, you'd need to call db.commit() after every CREATE, INSERT or DELETE
        cls.db.row_factory = sqlite3.Row # the default is to return rows as tuples, use Rows instead, which can be accessed by column name
        return cls.db.cursor()