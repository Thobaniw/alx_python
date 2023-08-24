
import MySQLdb
import sys


def search_state(username, password, database, state_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor
        cursor = db.cursor()

        # Format and execute the query to retrieve matching states
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(
            state_name)
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_state(username, password, database, state_name)