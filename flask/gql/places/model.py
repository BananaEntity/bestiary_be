from common.database import db

class Places(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   description = db.Column(db.String(255), nullable=False)
   country = db.Column(db.String(80), nullable=False)

   def to_json(self):
       return {
           "name": self.name,
           "description": self.description,
           "country": self.country,
       }

   def save(self):
       db.session.add(self)
       db.session.commit()