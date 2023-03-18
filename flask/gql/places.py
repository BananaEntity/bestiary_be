from flask_sqlalchemy import SQLAlchemy
from ariadne import gql, QueryType, MutationType, make_executable_schema

db = SQLAlchemy()

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

# Define type definitions (schema) using SDL
type_defs = gql(
    """
    type Query {
        places: [Place]
    }


    type Place {
        name: String!
        description: String!
        country: String!
    }
    
    type Mutation{add_place(name: String!, description: String!, country: String!): Place}
    """
)

# Initialize query
query = QueryType()

# Initialize mutation
mutation = MutationType()

# Define resolvers
# places resolver (return places )
@query.field("places")
def places(*_):
    return [place.to_json() for place in Places.query.all()]

# place resolver (add new  place)
@mutation.field("add_place")
def add_place(_, info, name, description, country):
    place = Places(name=name, description=description, country=country)
    place.save()

    return place.to_json()


# Create executable schema
schema = make_executable_schema(type_defs, [query, mutation])
