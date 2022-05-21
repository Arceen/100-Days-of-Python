from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
        

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/all")
def all():
    all_cafes = db.session.query(Cafe).all()
    cafes = []
    for c in all_cafes:
        cafe = c.__dict__
        del cafe['_sa_instance_state']
        cafes.append(cafe)
        
    return jsonify(cafe=cafes)
@app.route("/random")
def random():
    all_cafes = db.session.query(Cafe).all()
    index = randint(0, len(all_cafes)-1)
    random_cafe = all_cafes[index]
    print(random_cafe.__dict__)
    c = random_cafe.__dict__
    del c['_sa_instance_state']
    return jsonify(
        cafe = c
    )

@app.route("/search")
def search():
    loc = request.args.get("loc")
    all_cafes = db.session.query(Cafe).filter(Cafe.location ==loc).all()
    cafes = []
    for c in all_cafes:
        cafe = c.__dict__
        del cafe['_sa_instance_state']
        cafes.append(cafe)
    if cafes == []:
        cafes = {
            "error":{
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        } 
    return jsonify(cafe=cafes)
## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    cafe = request.form
    new_cafe = Cafe(
    name = cafe['name'],
    map_url = cafe['map_url'],
    img_url = cafe['img_url'],
    location = cafe['location'],
    seats = cafe['seats'],
    has_toilet = bool(cafe['has_toilet']),
    has_wifi = bool(cafe['has_wifi']),
    has_sockets = bool(cafe['has_sockets']),
    can_take_calls = bool(cafe['can_take_calls']),
    coffee_price = cafe['coffee_price'],
    )
    
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {
        "success": "Successfully added the new cafe."
    })



## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe == None:
        return jsonify(response = {
            "error": "Sorry a cafe with that id was not found in the database."
        }), 404
    else:
        cafe.coffee_price=request.args.get("new_price");
        db.session.commit()
        return jsonify(response = {
            "success": "Successfully updated the price."
        })
## HTTP DELETE - Delete Record
@app.route("/delete/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    print(request.args.get("api_key"))
    if request.args.get("api_key") != 'super_secret_api_key':
        return jsonify(response = {
            "error": "Require API Key for this operation."
        }), 404
    elif cafe == None:
        return jsonify(response = {
            "error": "Sorry a cafe with that id was not found in the database."
        }), 404
    else:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response = {
            "success": "Successfully deleted the cafe"
        })


if __name__ == '__main__':
    app.run(debug=True)
