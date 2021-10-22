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
    pass


def get_all_animals():
    pass


@app.route("/")
def index():
    animals = get_all_animals()
    return render_template("main.html", animals=animals)


@app.route("/add_animal")
def add_animal():
    # This is how you can get form arguments
    name = request.args["name"]
    animal_type = request.args["animal_type"]
    age = request.args["age"]
    price = request.args["price"]
    # Your solution here

    # bring us back to the page we started from after adding the animal
    return index


# Delete an animal based on some criteria you want, for example the name. If multiple animals with the same criteria exist it is ok to delete all of them
@app.route("/delete_animal")
def delete_animal():

    # bring us back to the page we started from after deleting the animal
    return index


# Taking an input, the query so far, the to_filter list and a name for the query, make a query and add the required parameters to the to_filter list
# such that you can pass in price={"gt": 60, “lte”: 100} and it will give you the correct sql query and to_filter parameters
def range_filter(input, query, to_filter, name):
    pass


# return the available columns and their datatype. This can serve as useful documentation for somebody using the API
@app.route("/api/v1/resources/animals/columns")
def get_columns():
    pass


# return all animals if no query parameter was filled otherwise filter based on the query parameters present
@app.route("/api/v1/resources/animals")
def get_animals():
    pass


def main():
    con = create_table_if_doesnt_exist()
    app.run(debug=True, host="0.0.0.0", port=80)
    con.close()


if __name__ == '__main__':
    main()
