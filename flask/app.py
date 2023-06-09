import flask_cors

from flask import Flask, request, jsonify
from ariadne import graphql_sync
from common.database import db
from gql.places.queries import schema
from config import databse

# initialize flask app
app = Flask(__name__)
flask_cors.CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = databse.POSTGRE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/cache-me')
def cache():
	return "nginx will cache this response"

@app.route('/flask-health-check')
def flask_health_check():
	return "success"

# Create a GraphQL endpoint for executing GraphQL queries
@app.route("/countries", methods=["POST"])
def graphql_server():
   data = request.get_json()
   success, result = graphql_sync(schema, data, context_value={"request": request})
   status_code = 200 if success else 400
   return jsonify(result), status_code