from flask import Flask, render_template, request, redirect
from models import db
from models.film_model import Film
from models.actor_model import Actor
from sqlalchemy.sql.expression import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/sakila_lightweight'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
db.init_app(app)

# Import models
from models.film_model import Film
from models.actor_model import Actor

"""
@app.route('/')
def index():
    trending_movies = Film.query.order_by(func.rand()).limit(10).all()    
    return render_template('index.html', trending_movies=trending_movies)
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    trending_movies = Film.query.order_by(func.rand()).limit(10).all()
    search_term = ""  

    if request.method == 'POST':
        search_term = request.form.get('search_term', '')
        # Query films that contain the search term in the title
        search_results = Film.query.filter(Film.title.ilike(f"%{search_term}%")).limit(5).all()
    else:
        search_results = []

    return render_template('index.html', trending_movies=trending_movies, search_results=search_results, search_term=search_term)

@app.route('/search_movies', methods=['POST'])
def search_movies():
    search_term = request.form.get('search_term', '')
    search_results = [...]  # Replace with your actual search query
    return render_template('search_results.html', search_results=search_results)

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
