from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'alumni_tracking_system'
}

# Route to get all alumni
@app.route('/alumni', methods=['GET'])
def get_alumni():
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM alumni")
    alumni = cursor.fetchall()
    
    # Closing the connection
    cursor.close()
    conn.close()
    
    return jsonify(alumni)

# Route to add a new alumni record
@app.route('/alumni', methods=['POST'])
def add_alumni():
    data = request.json
    name = data.get("name")
    graduation_year = data.get("graduation_year")
    degree = data.get("degree")
    current_position = data.get("current_position")
    contact_info = data.get("contact_info")
    
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Insert the new alumni record
    cursor.execute("INSERT INTO alumni (name, graduation_year, degree, current_position, contact_info) VALUES (%s, %s, %s, %s, %s)",
                   (name, graduation_year, degree, current_position, contact_info))
    conn.commit()
    
    # Closing the connection
    cursor.close()
    conn.close()
    
    return jsonify({"status": "success", "message": "Alumni record added successfully!"})

# Route to get specific alumni details
@app.route('/alumni/<int:id>', methods=['GET'])
def get_alumni_details(id):
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM alumni WHERE id = %s", (id,))
    alumni = cursor.fetchone()
    
    # Closing the connection
    cursor.close()
    conn.close()
    
    if alumni:
        return jsonify(alumni)
    else:
        return jsonify({"status": "failure", "message": "Alumni not found."})

if __name__ == '__main__':
    app.run(debug=True)

