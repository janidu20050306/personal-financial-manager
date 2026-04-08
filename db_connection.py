"""
Database connection utilities using psycopg2
Use this module for direct database connections outside of Django ORM
"""

import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class DatabaseConnection:
    """Helper class for direct database connections"""
    
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Connect to PostgreSQL database"""
        try:
            database_url = os.getenv('DATABASE_URL')
            
            if not database_url or database_url.startswith('sqlite'):
                raise ValueError("Direct psycopg2 connection requires PostgreSQL DATABASE_URL")
            
            # Parse PostgreSQL URL: postgresql://user:password@host:port/dbname
            self.connection = psycopg2.connect(database_url)
            self.cursor = self.connection.cursor()
            print("✓ Database connected successfully")
            return True
        except Exception as e:
            print(f"✗ Database connection failed: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("✓ Database connection closed")
    
    def execute_query(self, query, params=None):
        """Execute a SELECT query"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Query error: {e}")
            return None
    
    def execute_update(self, query, params=None):
        """Execute INSERT, UPDATE, DELETE query"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print(f"✓ Query executed successfully")
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"✗ Query error: {e}")
            return False
    
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

# Example usage:
# if __name__ == '__main__':
#     db = DatabaseConnection()
#     db.connect()
#     
#     # Run a query
#     results = db.execute_query("SELECT * FROM home_expense LIMIT 5")
#     for row in results:
#         print(row)
#     
#     db.disconnect()
#     
#     # Or use with statement:
#     # with DatabaseConnection() as db:
#     #     results = db.execute_query("SELECT * FROM home_expense")
#     #     print(results)
