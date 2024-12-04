from database import get_database_connection

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