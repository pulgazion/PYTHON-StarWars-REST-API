from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite = db.relationship('Favorite', back_populates="users")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorite": self.favorite
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender =db.Column(db.String(120), unique=False, nullable=False)
    eye_color =db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return 'chatacter %r' %self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year
        }

class Planet(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    population =db.Column(db.String(120), unique=False, nullable=False)
    diameter = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return 'planet %r' %self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population,
            "diameter": self.diameter
            
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id'))  
    users = db.relationship('User', back_populates="favorite")
    fav = db.Column(db.String(120), unique=False, nullable=False)
    fav_id = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return 'favorite %r' %self.id
    
    def serialize(self):
        return{
            "id": self.id,
            "user_id":self.user_id,
            "user": self.user,      
            "fav" : self.fav,
            "fav_id": self.fav_id   
        }