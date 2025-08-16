from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    review = db.Column(db.Text, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)

    def __repr__(self):
        return f"Review('{self.user_name}', '{self.review}')"

class Artists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(20), unique=False, nullable=False)
    genres = db.Column(db.String(30), unique=False, nullable=False)
    origin = db.Column(db.String(25), unique=False, nullable=False)
    band_members = db.Column(db.String(70), unique=False, nullable=True)
    years_active = db.Column(db.String(15), unique=False, nullable=False)
    awards = db.Column(db.String(70), unique=False, nullable=True)
    top_3_albums = db.Column(db.String(40), unique=False, nullable=True)
    top_3_songs = db.Column(db.String(40), unique=False, nullable=False)
    biography = db.Column(db.String(290), unique=False, nullable=False)
    image_file_path = db.Column(db.String(30),unique=False, nullable=True)

    def __str__(self):
        return self.artist_name
