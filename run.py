import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# home route
@app.route("/")
@app.route("/home")
def home():
    recipes = mongo.db.recipes.find()
    return render_template("home.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("home.html", recipes=recipes)


@app.route("/get_user_recipe")
def get_user_recipe():
    if session["user"]:
        user_recipes = mongo.db.recipes.find({"created_by": session["user"]})
        return render_template("user_recipes.html", recipes=user_recipes)


@app.route("/recipe_info/<recipe_id>")
def recipe_info(recipe_id):
    this_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    return render_template("recipe_info.html", recipes=this_recipe)


@app.route("/recipe_info_user/<recipe_id>")
def recipe_info_user(recipe_id):
    this_recipe = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})
    return render_template("recipe_info_user.html", recipes=this_recipe)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({
            "username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already taken", "username_flash")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(
                request.form.get("password")),
            "email": request.form.get("email")
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("You have successfully registered!", "register_flash")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get(
                    "username")), "welcome_flash")
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username or Password", "incorrect_flash")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username or Password", "incorrect_flash")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("you've been logged out", "logout_flash")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        is_vegan = "yes" if request.form.get("is_vegan") else "no"
        is_vegetarian = "yes" if request.form.get("is_vegetarian") else "no"
        recipe_img = request.form.get("recipe_img") if request.form.get(
         "recipe_img") else (
         "http://veraconsulting.it/wp-content/uploads/2014/04/placeholder4.png"
          )
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_img": recipe_img,
            "is_vegan": is_vegan,
            "is_vegetarian": is_vegetarian,
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("recipe added!", "add_flash")
        return redirect(url_for("add_recipe"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_vegan = "yes" if request.form.get("is_vegan") else "no"
        is_vegetarian = "yes" if request.form.get("is_vegetarian") else "no"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_img": request.form.get("recipe_img"),
            "is_vegan": is_vegan,
            "is_vegetarian": is_vegetarian,
            "created_by": session["user"]
        }
        mongo.db.recipes.replace_one({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Updated!", "update_flash")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("recipe deleted!", "delete_flash")
    return redirect(url_for("get_user_recipe"))


# update to debug=False prior to deployment!
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
