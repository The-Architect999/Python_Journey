from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    # Rule 1: If the request is for a known static file type, ignore it
    # This prevents the route from trying to 'render' JS or CSS
    if page_name.endswith(('.js', '.css', '.png', '.jpg', '.ico')):
        return '', 204  # Tell the browser 'No Content' so it doesn't crash the server

    # Rule 2: Ensure it ends with .html for the templates folder
    if not page_name.endswith(".html"):
        page_name += ".html"
        
    return render_template(page_name)


def write_to_csv(data):
    with open("database.csv", mode='a', newline='', encoding='UTF-8') as database:
        email = data['email']
        message = data['message']
        subject = data['subject']
        csv_writer = csv.writer(database, delimiter="|", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #converts data to dict
            write_to_csv(data)
            print("new information acquired!")
            return redirect("/thankyou.html")
        except:
            return "did not save to Database!"
    else:
        return "something went worng, Try again!"



if __name__ == "__main__":
    app.run(debug=True)