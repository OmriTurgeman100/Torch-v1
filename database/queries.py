import psycopg2  
from creds import DB_HOST, DB_NAME, DB_USER, DB_PASS

def get_database_connection(): # * config
    try:
        postgres = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return postgres
    
    except Exception as e:
        print(e)

def insert_root():
    try: 
        postgres = get_database_connection()
        cursor = postgres.cursor()

        root_nodes = [
            {
                "title": "ubuntu",
                "description": "ubuntu machine",
                "status": "up",
            },
            {
                "title": "kubernetes",
                "description": "kubernetes data",
                "status": "expired",
            }    
        ]

        for root_node in root_nodes:
            title = root_node["title"]
            description = root_node["description"]
            status = root_node["status"]

            print(title, description, status)

        cursor.execute("insert into nodes (title, description, status) values (%s, %s, %s)", (title, description, status))
        postgres.commit()
        
    except Exception as e:
        print(e)

insert_root()