import sqlite3

def search_user(username):
    conn = sqlite3.connect('example.db')
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
