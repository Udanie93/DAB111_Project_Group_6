from flask import Flask, render_template
import sqlite3
import pathlib 

# Define the base path for the database file
base_path = pathlib.Path(r'C:\Users\udani\Documents\Final Project Python')

# Define the name of the database file
db_name = "heart_disease_prediction.db"

# Create the full path to the database file
db_path = base_path / db_name

# Print the path for debugging purposes
print(db_path)

# Initialize Flask app
app = Flask(__name__)

# Define route for the homepage
@app.route("/")
def index():
    return render_template("index.html") 

# Define route for the about page
@app.route("/about")
def about():
    return render_template("about.html")

# Define route for the group page
@app.route("/group")
def group():
    return render_template("group.html")

# Define route for the data page
@app.route("/data")
def data():
    # Connect to the SQLite database
    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    # Execute a query to fetch heart disease details (limiting to 10 rows for demonstration)
    heart_dis = cursor.execute("SELECT * FROM heart_disease_details LIMIT 10").fetchall()

    # Close the database connection
    con.close()

    # Render the data_table.html template with the fetched heart disease details
    return render_template("data_table.html", heart_dis=heart_dis)

# Run the Flask app if this script is executed directly
if __name__=="__main__":
    app.run(debug=True)
