from flask import request
from flask import jsonify
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to your icanteen!!!"

@app.route("/insertmenu")
def insertmenu():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    file = open('menu.csv', 'r')
    list_of_menu = []
    for line in file:
            menu = line.split(',')
            m = {'item':menu[0], 'store':int(menu[4]), 'cal':int(menu[2]), 'filter':menu[1], 'price':int(menu[3]), 'pic':menu[4]}
            list_of_menu.append(m)
    db.menus.delete_many({})
    result = db.menus.insert_many(list_of_menu, ordered=False)
    return "upload done"

@app.route("/showmenu")
def showmenu():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    getstore = request.args.get('store')
    docs = db.menus.find({'store':int(getstore)})
    r = dict()
    r['data'] = []
    for doc in docs:
            ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
            r['data'].append(ret)
    return jsonify(r)

@app.route("/choosefilterc")
def choosefilterc():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    docs = db.menus.find({})
    result = []
    for doc in docs:
            if "#carb" in doc["filter"]:
                    ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
                    result.append(ret)
    return jsonify(result)

@app.route("/choosefilterv")
def choosefilterv():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    docs = db.menus.find({})
    result = []
    for doc in docs:
            if "#vegetable" in doc["filter"]:
                    ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
                    result.append(ret)
    return jsonify(result)

@app.route("/choosefilterf")
def choosefilterf():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    docs = db.menus.find({})
    result = []
    for doc in docs:
            if "#fried" in doc["filter"]:
                    ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
                    result.append(ret)
    return jsonify(result)

@app.route("/choosefilterh")
def choosefilterh():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    docs = db.menus.find({})
    result = []
    for doc in docs:
            if "#healthy" in doc["filter"]:
                    ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
                    result.append(ret)
    return jsonify(result)

@app.route("/highcal")
def highcal():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    docs = db.menus.find( {"cal": { "$gt": 600 } })
    r = []
    for doc in docs:
            ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
            r.append(ret)
    return jsonify(r)

@app.route("/lowcal")
def lowcal():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    docs = db.menus.find( {"cal": { "$lt": 300 } })
    r = []
    for doc in docs:
            ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
            r.append(ret)
    return jsonify(r)

@app.route("/midcal")
def midcal():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    docs = db.menus.find({"$and":[{"cal": { "$gt": 300 } },{"cal": { "$lt": 600 } }]})
    r = []
    for doc in docs:
            ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
            r.append(ret)
    return jsonify(r)

@app.route("/allmenu")
def allmenu():
    client = MongoClient("mongodb+srv://6131866021:1234@cluster0-3xijp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.student_scores
    docs = db.menus.find({})
    r = []
    for doc in docs:
            ret = {'item':doc['item'], 'store':doc['store'], 'cal':doc['cal'], 'filter':doc['filter'], 'price':doc['price'], 'pic':doc['pic']}
            r.append(ret)
    return jsonify(r)
