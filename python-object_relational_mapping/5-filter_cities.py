import MySQLdb
import sys


def list_cities_by_state(username, password, db_name, state_name):
    try:
        # Connect to the MySQL server
        conn = MySQLdb.connect(host='localhost', port=3306,
                               user=username, passwd=password, db=db_name)
        cursor = conn.cursor()

        # Execute the query
        query = "SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ') FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s"
        cursor.execute(query, (state_name,))

        # Fetch and print the result
        result = cursor.fetchone()
        if result[0]:
            print(result[0])

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the connection
        if conn:
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <db_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, db_name, state_name)
