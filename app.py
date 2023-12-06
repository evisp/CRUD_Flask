from flask import Flask, render_template, request, redirect, url_for
from models.film_model import db, Film

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@zerotoone:3306/sakila'
db.init_app(app)

@app.route('/')
def index():
    films = Film.query.all()
    return render_template('index.html', films=films)

# Route to display details of a single film
@app.route('/film/<int:film_id>')
def film_detail(film_id):
    film = Film.query.get(film_id)
    return render_template('film_detail.html', film=film)

if __name__ == '__main__':
    app.run(debug=True)
