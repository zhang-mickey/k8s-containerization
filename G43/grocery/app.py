# import sqlite3
from flask_sqlalchemy import SQLALchemy

from flask_cors import CROS,cross_origin

import psycopg2

import random

from flask import Flask, session, render_template, g, request, redirect, url_for




app = Flask(__name__)

cors=CORS(app)

app.secret_key = "manbearpig_MUDMAN888"

app.config["SESSION_COOKIE_NAME"] = "myCOOKIE_monSTER528"
# os.env
app.config['SQLALCHEMY_DATABASE_URL']="postgresql://postgres:123456@postgres-service-1:5432/my_db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



@app.route("/", methods=["POST", "GET"])
@cross_origin()

def index():

    session["all_items"], session["shopping_items"] = get_db()

    return render_template("index.html", all_items=session["all_items"],

                                         shopping_items=session["shopping_items"])



@app.route("/add_items", methods=["post"])
@cross_origin()

def add_items():

    session["shopping_items"].append(request.form["select_items"])

    session.modified = True

    return render_template("index.html", all_items=session["all_items"],

                                         shopping_items=session["shopping_items"])



@app.route("/remove_items", methods=["post"])
@cross_origin()

def remove_items():

    checked_boxes = request.form.getlist("check")



    for item in checked_boxes:

        if item in session["shopping_items"]:

            idx = session["shopping_items"].index(item)

            session["shopping_items"].pop(idx)

            session.modified = True



    return render_template("index.html", all_items=session["all_items"],

                                         shopping_items=session["shopping_items"])



@app.route("/delete_items", methods=["POST"])
@cross_origin()

def delete_items():

    item_name = request.form["select_items"]  # 从表单获取项名称

    db = getattr(g, '_database', None)

    if db is None:

        conn_string = "host='10.0.2.15' port='30001' dbname='my_db' user='postgres' password ='123456'"

        db = g._database = psycopg2.connect(conn_string)

        cursor = db.cursor()

        cursor.execute("DELETE FROM groceries WHERE name = %s", (item_name,))

        db.commit()  # 提交事务以保存更改



    return redirect(url_for('index'))

# def get_db():

#     db = getattr(g, '_database', None)

#     if db is None:

#         db = g._database = sqlite3.connect('grocery_list.db')

#         cursor = db.cursor()

#         cursor.execute("select name from groceries")

#         all_data = cursor.fetchall()

#         all_data = [str(val[0]) for val in all_data]

#

#         shopping_list = all_data.copy()

#         random.shuffle(shopping_list)

#         shopping_list = shopping_list[:5]

#     return all_data, shopping_list



def get_db():

    db = getattr(g, '_database', None)

    if db is None:

        conn_string = "host='10.0.2.15' port='30001' dbname='my_db' user='postgres' password ='123456'"

        db = g._database = psycopg2.connect(conn_string)

        cursor = db.cursor()

        cursor.execute("SELECT name FROM groceries")

        all_data = cursor.fetchall()

        all_data = [str(val[0]) for val in all_data]



        shopping_list = all_data.copy()

        random.shuffle(shopping_list)

        shopping_list = shopping_list[:5]

    return all_data, shopping_list



@app.teardown_appcontext

def close_connection(exception):

    db = getattr(g, '_database', None)

    if db is not None:

        db.close()



if __name__ == '__main__':

    app.run(host="0.0.0.0", port =5000, debug=False)
