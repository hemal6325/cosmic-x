from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

app.secret_key = "123@123"

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login_signup")
def login_signup():
    return render_template('login_signup.html')

@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/moon.html")
def moon():
    return render_template('moon.html')

@app.route("/moon1.html")
def moon1():
    return render_template('moon1.html')

@app.route("/go_space.html")
def space():
    return render_template('go_space.html')

@app.route("/mars2.html")
def mars2():
    return render_template('mars2.html')
@app.route("/journey_moon.html")
def journey_moon():
    return render_template('journey_moon.html')

@app.route("/jupyter_journey.html")
def jupyter_journey():
    return render_template('jupyter_journey.html')

@app.route("/journey_mars.html")
def journey_mars():
    return render_template('journey_mars.html')

@app.route("/moon2.html")
def moon2():
    return render_template('moon2.html')
@app.route("/jupyter3.html")
def jupyter3():
    return render_template('jupyter3.html')

@app.route("/moon3.html")
def moon3():
    return render_template('moon3.html')

@app.route("/mars3.html")
def mars3():
    return render_template('mars3.html')

@app.route("/mars.html")
def mars():
    return render_template('mars.html')

@app.route("/mars1.html")
def mars1():
    return render_template('mars1.html')


@app.route("/jupyter.html")
def jupyter():
    return render_template('jupyter.html')

@app.route("/jupyter1.html")
def jupyter1():
    return render_template('jupyter1.html')

@app.route("/jupyter2.html")
def jupyter2():
    return render_template('jupyter2.html')

@app.route("/learn_more.html")
def learn_more():
    return render_template('learn_more.html')
@app.route("/learn_more.html")

@app.route("/mars2-18.html")
def mars2_18():
    return render_template('mars2-18.html')

@app.route("/moon-1-15.html")
def moon_1_15():
    return render_template('moon-1-15.html')

@app.route("/jupiter-1-17.html")
def jupiter_1_17():
    return render_template('jupiter-1-17.html')

@app.route("/profile.html")
def profile():
    return render_template('profile.html')

@app.route("/signup.html")
def signup():
    return render_template('signup.html')
@app.route("/signup_success", methods=["GET", "POST"])
def signup_success():
    if request.method == 'POST':
        return render_template('login.html')
    
@app.route("/login_success", methods=["GET", "POST"])
def login_success():
    if request.method == 'POST':
        email = request.form["email"]
        pass_word = request.form["password"]

        if email == 'cosmicx@gmail.com' and pass_word == "12345678":
            return render_template('home.html')
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')