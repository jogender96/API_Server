# app.py
from flask import Flask
from flask_graphql import GraphQLView
from models import Base, Bank, Branch
from schema import schema
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///banks.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

# GraphQL endpoint
app.add_url_rule(
    '/gql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run(debug=True)
