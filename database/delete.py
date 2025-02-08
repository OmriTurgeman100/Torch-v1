from database import get_database_connection


def insert_root():
    try: 
        postgres = get_database_connection()
        cursor = postgres.cursor()

        tabels = ["nodes", "reports", "report_rules", "node_rules"]

        for table in tabels:

            delete_query = f"delete from {table}"

            cursor.execute(delete_query)
            postgres.commit()
            response = cursor.fetchall()  

            print(response)

    except Exception as e:
        print(e)

insert_root()