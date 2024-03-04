# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Alex" # write your name
    age = "12" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
http://127.0.0.1:5000

# define the route to mother webpage
http://127.0.0.1:5000

# define the route to friends webpage
http://127.0.0.1:5000

# add other routes, if you want
localhost:5000



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
