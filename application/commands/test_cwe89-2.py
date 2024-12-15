import mysql.connector

def search_user(username):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="example"
    )
    cursor = conn.cursor()
    
    # Vulnerable code: direct inclusion of user input in SQL query
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    
    results = cursor.fetchall()
    conn.close()
    
    return results

# Example usage
username = input("Enter username: ")
print(search_user(username))


