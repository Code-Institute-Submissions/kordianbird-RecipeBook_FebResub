# RecipeBook Project
This project is a website that let's users share their recipes for amazing
dishes and discover new tasty recipes to use at home. The site is available 
for everyone to use and users are free to share their passion for culinary arts.

[wireframes](https://github.com/kordianbird/RECIPEBOOK/tree/main/wireframes)

# UX

## User Stories
People are always cooking either for themselves or for their family. They are
always eager to try out something new or improve the recipes they already know.

My webiste aims to help people discover and improve their recipes for tastier meals.

As a User...

* I want to be able to search for new recipes

* I want to create recipes for other users to see

* I want this website to be responsive

* I want to be able to view all my recipes

* I want to be able to easily navigate through the website

* I want to be able to edit my recipe

* I want to be able to delete my recipe

* I want to be able to create an account

* I want to be able to sign out of my account

## Design

* the background image gives off a fun and inviting feel to the user

* profile page let's the user know that they are logged in and what their username is

* add_recipe page is plain and not cramped with content to not overwhelm the user

* user_recipes have delete and edit buttons that are easy to see

* the pink and cyan colors of navbar and buttons are bright to give the website a calm and nice feel

* recipes show if they are vegan or vegetarian using symbols

# Features

## Existing Features

* login/logout allows the user to enter/leave their profile

* the user is able to create their own recipe in add_recipe page

* the user can then edit/delete their previously published recipes

* the home page shows all recipes of all users

* expand button allows the recipe to be expanded to show more content

## Next Features

* a "like" button to create popularity among recipes

* function to change user's username or password

* access to more food categories

# Technologies Used

## Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML)
-I used html (HyperText Markup Language) as the markup language for this project

* [CSS3](https://en.wikipedia.org/wiki/CSS)
-I used css3 to style many aspects of the website

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-I used python to program my database

## Framework

* [Materialize](https://materializecss.com/)
-I used materialize as a framework for this project

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
-I used flask to help me build my website

## Libraries

* [werkzeug.security](https://werkzeug.palletsprojects.com/en/2.0.x/utils/?highlight=security#module-werkzeug.security)
-I used werkzeug to hash user's passwords for privacy

* [bson.objectid](https://docs.mongodb.com/manual/reference/method/ObjectId/)
-I used objectid to edit/delete recipes from database

* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
-I used flask-pymongo to connect to my database on MongoDB

* [JQuery](https://en.wikipedia.org/wiki/JQuery)
-I used jquery to add functionality to some html elements

## Programmes

* [Git](https://git-scm.com/)
 I used gitpod's terminal to commit my code and then to push it to GitHub

* [GitHub](https://github.com/)
 I used GitHub to store my project code

* [Mockplus](https://www.mockplus.com/)
 I used Mockplus to create my wireframes

# Testing

I used :

* [W3C Markup Validator](https://validator.w3.org/) to validate my html code

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my css code

* [JSHint](https://jshint.com/) to validate my JavaScript code

* [PEP8](http://pep8online.com/checkresult) to validate my Python code 

results:

* W3C Markup Validator: No errors or warnings 

* W3C CSS Validator: No errors or warnings

* JSHint: No errors or warnings

* PEP8: No errors or warnings

[Tests](https://github.com/kordianbird/RecipeBook/blob/main/static/tests/tests.PNG)


# Deployment

## Heroku

I deployed my app to Heroku using these steps...

1. Log in to Heroku and create a new app. Choose the region that is most suitable to where you are in the world.

2. You will need a Procfile in your repository if you do not have one already and add the following to it:
```
echo web: python app.py
```

3. Make sure that your ```requirements.txt``` file is up to date using:
```
pip3 freeze --local requirements.txt
```

4. Connect your Github account to your Heroku App so that your repository from Github automatically deploys to Heroku when you push your changes to Github

5. Once Github is connected, you will need to go to settings and go to "Reveal Config Vars" where you will be able to set up the configuration variables that you have in your env.py file:
``` python
import os

os.environ.["IP"] = 0.0.0.0
os.environ.["PORT"] = "5000"
os.environ["SECRET_KEY"] = "ENTER_YOUR_SECRET_KEY_HERE"
os.environ["DEBUG"] = "TRUE"
os.environ["MONGO_URI"] = "ENTER_YOUR_MONGO_URI_HERE"
os.environ["MONGO_DBNAME"] = "ENTER_YOUR_DBNAME_HERE"
```

6. Go back to the deploy tab and click on "Enable Automatic Deployement"

7. Click "Deploy Branch" to start the build

8. Open your Heroku app

## Forking the GitHub Repository

Forking the repository makes a copy of the original in your GitHub account to view/make changes without affecting the original.
These are steps you can use to fork the repository:

1. Log in to GitHub and navigate to the repository
2. find the 'Fork' button at the top of the repository below your profile picture 
3. You now have a copy of the repository in your account

## Local Clone

1. Log in to GitHub and find the repository
2. Under repository find and click on "Clone or Download"
3. You can clone the repository using HTTPS by copying the link under "Clone with HTTPS"
4. Open Git Bash 
5. Change directory to the location where you want to clone the new directory
6. Type `git clone` and paste the copied URL 
`$ git clone https://github.com/USERNAME/REPOSITORY`
7. Press enter

# Credits

## Code

* I found the registration form [here](https://codepen.io/vaskopetrov/pen/amxvrY?editors=1100)

## Content

* All content was written by me personally

* Some recipes that were used were found on google

* I used FontAwesome to aquire icons

## Media

* I found the background image on [google images](https://www.google.com/search?q=hd+food+wallpapers+27%22&tbm=isch&ved=2ahUKEwj475X9icryAhXMGcAKHfcgCZkQ2-cCegQIABAA&oq=hd+food+wallpapers+27%22&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BAgAEB46BggAEAUQHjoGCAAQCBAeUM2cDVi2pw1g_6sNaABwAHgAgAEziAG1AZIBATSYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=LB4lYfipCsyzgAb3waTICQ&bih=1329&biw=2560#imgrc=1qrb-TsJOxwMRM)