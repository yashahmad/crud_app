from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)


@app.route('/viewall')
def view():
	con=sqlite3.connect("credit.db")
	con.row_factory=sqlite3.Row	
	cur=con.cursor()
	cur.execute("SELECT * from info")
	rows=cur.fetchall();
	return render_template("list.html",rows=rows)


@app.route('/select')
def choose():
	return render_template("choose.html")

@app.route('/select',methods=["POST"])
def search_one():
	if request.method=="POST":
		user_name=request.form["user_name"]
		con=sqlite3.connect("credit.db")
		cur=con.cursor()
		cur.execute("SELECT * FROM info WHERE name=?",[user_name])
		sel=cur.fetchall()
		con.close()
		return render_template("choose.html",sel=sel)
	
					
@app.route('/')
def index():
	return render_template("index.html")


if __name__ == "__main__":
	app.run(port=5000, debug=True)
