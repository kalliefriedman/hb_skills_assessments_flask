from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def homepage():
    """serves the template index.html. Includes a link to application form."""
    return render_template("index.html")


@app.route('/application-form')
def applicationform():
    """serves the template application-form.html"""
    jobs = ["QA Engineer", "Product Manager", "Software Engineer"]
    return render_template("application-form.html", positions=jobs)


@app.route('/application-success', methods=["POST"])
def applicationresponse():
    """serves the template application-response.html"""
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    quantity = float(request.form.get("quantity"))
    job = request.form.get("position")
    print job
    return render_template("application-response.html", firstname=firstname, lastname=lastname, salary=quantity, position=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
