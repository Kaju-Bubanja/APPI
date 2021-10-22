import urllib.parse

from flask import Flask, render_template, request, jsonify
import sqlite3
import json
app = Flask(__name__)


db_name = "animals.db"


# return dictionary instead of tuple
def dict_factory(cursor, row):
    d = {}
    for idx, description in enumerate(cursor.description):
        # 0 is the column name
        d[description[0]] = row[idx]
    return d


def create_table_if_doesnt_exist():
    try:
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS animals (name text NOT NULL, type text, age real, price real NOT NULL)''')
        con.commit()
        print("Created table")
    except Exception as e:
        print(e)
    return con


def get_all_animals():
    con = sqlite3.connect(db_name)
    # The db returns a tuple which is unnamed, to make the template more readable we parse it into a dict
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("SELECT * FROM animals")
    animals = cur.fetchall()
    return animals


@app.route("/")
def index():
    animals = get_all_animals()
    return render_template("main.html", animals=animals)


@app.route("/add_animal")
def add_animal():
    name = request.args["name"]
    animal_type = request.args["animal_type"]
    age = request.args["age"]
    price = request.args["price"]
    con = sqlite3.connect(db_name)
    # prevent sql injection with ????
    con.execute("INSERT INTO animals (name, type, age, price) VALUES(?, ?, ?, ?)", (name, animal_type, age, price))
    con.commit()
    return index()


@app.route("/delete_animal")
def delete_animal():
    query_parameters = request.args
    name = query_parameters.get('name')
    if not name:
        return "Please call method with a name query parameter like /delete_animals?name=foo"
    con = sqlite3.connect(db_name)
    # prevent sql injection with ????
    con.execute("DELETE FROM animals WHERE name = ?", (name, ))
    con.commit()
    return index()


def range_filter(input, query, to_filter, name):
    if "lt" in input:
        query += f" {name} < ? AND"
        to_filter.append(input["lt"])
    if "lte" in input:
        query += f" {name} <= ? AND"
        to_filter.append(input["lte"])
    if "gt" in input:
        query += f" {name} > ? AND"
        to_filter.append(input["gt"])
    if "gte" in input:
        query += f" {name} >= ? AND"
        to_filter.append(input["gte"])
    if "eq" in input:
        query += f" {name} = ? AND"
        to_filter.append(input["eq"])
    return query


# return the available columns and their datatype. This can serve as useful documentation for somebody using the API
@app.route("/api/v1/resources/animals/columns")
def get_columns():
    return jsonify({"name": "str", "type": "str", "age": "float", "price": "float"})


# return all animals if no query parameter was filled otherwise filter based on the query parameters present
@app.route("/api/v1/resources/animals")
def get_animals():
    query_parameters = request.args

    name = query_parameters.get('name')
    animal_type = query_parameters.get('type')
    age = query_parameters.get('age')
    if age:
        age = query_parameters.get('age')
        age = age.replace("\'", "\"")
        age = json.loads(age)
    price = query_parameters.get('price')
    if price:
        price = query_parameters.get('price')
        price = price.replace("\'", "\"")
        price = json.loads(price)

    query = "SELECT * FROM animals WHERE"
    to_filter = []

    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if animal_type:
        query += ' type=? AND'
        to_filter.append(animal_type)
    if age:
        query = range_filter(age, query, to_filter, "age")
    if price:
        query = range_filter(price, query, to_filter, "price")
    if not (name or animal_type or age or price):
        return jsonify(get_all_animals())

    # cut off the last and
    query = query[:-4] + ';'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


def main():
    con = create_table_if_doesnt_exist()
    app.run(debug=True, host="0.0.0.0", port=80)
    con.close()


if __name__ == '__main__':
    main()
