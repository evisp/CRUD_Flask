from flask import Flask, render_template, request
from models import db
from models.film_model import Film
from models.actor_model import Actor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/sakila'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
db.init_app(app)

# Import models
from models.film_model import Film
from models.actor_model import Actor


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'POST':
        search_term = request.form.get('search_term', '')
        films = Film.query.filter(Film.title.ilike(f"%{search_term}%")).all()
    else:
        films = Film.query.all()

    return render_template('movies.html', films=films)

@app.route('/film/<int:film_id>')
def film_detail(film_id):
    film = Film.query.get(film_id)
    return render_template('film_detail.html', film=film)

@app.route('/actors')
def show_actors():
    actors = Actor.query.all()
    return render_template('actors.html', actors=actors)

if __name__ == '__main__':
    app.run(debug=True)
