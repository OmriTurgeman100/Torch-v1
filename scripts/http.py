import psycopg2
import random
from constants import DB_HOST, DB_NAME, DB_USER, DB_PASS

# Database connection parameters
DB_CONFIG = {
    "dbname": DB_NAME,
    "user": DB_USER,
    "password": DB_PASS,
    "host": DB_HOST,
    "port": 5432
}

# Possible statuses
STATUSES = ['critical', 'expired', 'up', 'down']

# Function to insert nodes
def insert_nodes(num_nodes):
    try:
        # Connect to the database
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        for i in range(1, num_nodes + 1):
            title = f"Node {i}"
            description = f"Description for Node {i}"
            status = random.choice(STATUSES)  # Select a random status
            
            # Insert query
            insert_query = """
                INSERT INTO nodes (parent, title, description, status)
                VALUES (NULL, %s, %s, %s)
            """
            cursor.execute(insert_query, (title, description, status))

        # Commit changes
        conn.commit()
        print(f"{num_nodes} nodes inserted successfully.")
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    
    finally:
        # Close the connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Insert 10 nodes
if __name__ == "__main__":
    insert_nodes(10)
