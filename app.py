from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL connection URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/sakila'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable Flask-SQLAlchemy modification tracking

# Initialize SQLAlchemy instance
db = SQLAlchemy(app)

# Define the Actor model
class Actor(db.Model):
    __tablename__ = 'actor'

    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)

# Route to display all actors
@app.route('/actors')
def show_actors():
    # Query all actors from the 'actor' table
    actors = Actor.query.all()

    # Render the template with actor information
    return render_template('actors.html', actors=actors)

if __name__ == '__main__':
    app.run(debug=True)
