from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
import os
from pathlib import Path
from models_app import db, Review, Artists
from forms import ReviewForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_BINDS'] = {
    'artists': 'sqlite:///artists.db',
    'reviews': 'sqlite:///reviews.db'
}
db.init_app(app)
app.config['UPLOAD_FOLDER'] = 'static/media/'
app.config['SECRET_KEY'] = 'cd2373d0c63c81b062651c4003778c8e'
ALLOWED_EXTENSION = {'png', 'jpg', 'jpeg'}
migrate_reviews = Migrate(app, db, directory='migrations_reviews')

def allowed_file(filename):
    return Path(filename).suffix.lower() in {f'.{ext}' for ext in ALLOWED_EXTENSION}

@app.route("/")
def homepage():
    artists = Artists.query.all()
    print(artists)
    return render_template("iHeartMusic_hp.html", artists=artists)


@app.route("/artist/<int:id>/", methods=['GET', 'POST'])
def artist_page(id):
    artist = Artists.query.get_or_404(id)
    reviews = Review.query.filter_by(artist_id=id).all()
    form = ReviewForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        review_content = form.review_content.data
        new_review = Review(user_name=user_name, review=review_content, artist_id=id)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('artist_page', id=id, reviews=reviews))

    return render_template("artist_page.html", artist=artist, form=form, reviews=reviews)

@app.route('/delete_artist/<int:artist_id>', methods=['POST'])
def delete_artist(artist_id):
    with app.app_context():
        artist = db.session.query(Artists).get(artist_id)
        if artist:
            db.session.delete(artist)
            db.session.commit()
    return redirect(url_for('homepage'))

@app.route('/submit_artist', methods=['POST'])
def submit_artist():
    if request.method == "POST":
        artist_name = request.form.get("Artist Name")
        genres = request.form.get("Genres")
        origin = request.form.get("Origin")
        band_members = request.form.get("Band members")
        years_active = request.form.get("Years active")
        awards = request.form.get("Awards")
        top_3_albums = request.form.get("Top 3 Albums")
        top_3_songs = request.form.get("Top 3 Songs")
        biography = request.form.get("Biography")
        artist_image = request.files.get("file")
        image_file_path = os.path.join('media/', artist_image.filename)

        new_artist = Artists(artist_name=artist_name, genres=genres, origin=origin, band_members=band_members,\
         years_active=years_active, awards=awards, top_3_albums=top_3_albums, top_3_songs=top_3_songs,\
         biography=biography, image_file_path=image_file_path)
        db.session.add(new_artist)
        db.session.commit()
        if artist_image and allowed_file(artist_image.filename):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], artist_image.filename)
            artist_image.save(file_path)
        return redirect(url_for('homepage'))
    else:
        return render_template("add_artist.html")

@app.route('/add_artist')
def add_artist():
    return render_template('add_artist.html')




if __name__ == "__main__":
    app.run(debug=True, port=5001)
