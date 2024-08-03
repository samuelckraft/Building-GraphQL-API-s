from flask import Flask
from flask_graphql import GraphQLView
import graphene
from schema import Query, Mutation
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:654U7jsv@localhost/bakery_db'
db.init_app(app)

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


# Add product query
# mutation {
#   createProduct(name:"Snickerdoodle", price:5, category:"Cookie", quantity:2) {
#     product{
#       id
#       name
#       price
#       category
#       quantity
#     }
#   }
# }

# query {
#   products{
#     name
#     category
#   }
# }



# Update product query
# mutation {
#   updateProduct(id: 1, name:"Chocolate Chip", price:5, quantity:2, category:"Cookie"){
#     product{
#     id
#     name
#     price
#     quantity
#     category
#   }
#   }
# }



# Delete product query
# mutation {
#   deleteProduct(id:1){
#     product{
#       id
#       name
#       price
#       quantity
#       category
#     }
#   }
# }