from gql.places.model import Places
from ariadne import gql, QueryType, MutationType, make_executable_schema

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
