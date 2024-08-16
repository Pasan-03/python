import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection settings
username = 'root'
password = ''
host = 'localhost'
database = 'blog_db'

# Create a database connection
cnx = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

cursor = cnx.cursor()

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify([{'id': user[0], 'username': user[1], 'email': user[2]} for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    cnx.commit()
    return jsonify({'message': 'User created successfully'})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify({'id': user[0], 'username': user[1], 'email': user[2]})
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    cursor.execute("UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s", (username, email, password, user_id))
    cnx.commit()
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    cnx.commit()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)