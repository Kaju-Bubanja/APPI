import urllib
import requests
from appi.debugging.log_handling import setup_logger, close_log_handlers


class APIController:
    def __init__(self, base_url, table_name, log_filename):
        self.base_url = base_url
        self.table_name = table_name
        self.column_url = self.base_url + f"api/v1/resources/{self.table_name}/columns"
        self.add_url = self.base_url + "add_animal"
        self.filter_url = self.base_url + f"api/v1/resources/{self.table_name}"
        self.delete_url = self.base_url + f"delete_animal"
        self.log = setup_logger(log_filename)
        self.columns = self.get_columns()
        self.log.info(f"Available columns are {self.columns}")

    def __del__(self):
        close_log_handlers(self.log)

    def get_columns(self):
        columns, success = self.make_and_log_http_call(self.column_url, "Getting table columns")
        return columns

    def query_data(self, filter):
        payload = urllib.parse.urlencode(filter)
        data, success = self.make_and_log_http_call(self.filter_url, f"Getting data for {filter}", payload=payload)
        return data

    def add_data(self, data):
        self.make_and_log_http_call(self.add_url, f"Adding data: {data}", json=False, payload=data)

    def delete_data(self, name):
        self.make_and_log_http_call(self.delete_url, f"Deleting data: {name}", json=False, payload=name)

    def make_and_log_http_call(self, url, code_str, json=True, payload=None):
        self.log.info("Calling: " + str(url))
        try:
            if payload:
                response = requests.get(url, params=payload)
            else:
                response = requests.get(url)
            self.log.info(code_str + " code: " + str(response.status_code))
            self.log.debug(code_str + " text: " + response.text)
            if json:
                return response.json(), response.status_code == 200
            else:
                return response, response.status_code == 200
        except Exception as e:
            self.log.warning("Request failed")
            self.log.debug(str(e))
        return None, False


def main():
    animals_controller = APIController("http://localhost/", "animals", "animals_controller.log")
    data = {"name": "Bob", "animal_type": "Dog", "age": 1, "price": 30}
    animals_controller.add_data(data)
    data = {"name": "Lars", "animal_type": "Horse", "age": 2, "price": 10}
    animals_controller.add_data(data)
    data = {"name": "Helen", "animal_type": "Cat", "age": 3, "price": 20}
    animals_controller.add_data(data)
    data = {"name": "Max", "animal_type": "Fish", "age": 4, "price": 25}
    animals_controller.add_data(data)
    filter = {"price": {"gte": 20}}
    print(animals_controller.query_data(filter))
    filter = {"name": "Max", "price": {"gte": 20, "lt": 30}}
    print(animals_controller.query_data(filter))
    animals_controller.delete_data({"name": "Max"})
    print(animals_controller.query_data(filter))

    books_controller = APIController("http://localhost/", "books", "books_controller.log")
    filter = {"title": "Ancillary Justice"}
    print(books_controller.query_data(filter))


if __name__ == '__main__':
    main()
