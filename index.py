from flask import Flask , render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template('index.html')


#run server
if __name__ =="__main__":
    app.run(debug = False, host='0.0.0.0')