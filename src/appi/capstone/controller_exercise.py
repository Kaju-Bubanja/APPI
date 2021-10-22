import urllib
import requests
from appi.debugging.log_handling import setup_logger, close_log_handlers


class APIController:
    # Specify following parameters when creating an api controller object, to be able to use it for different apis
    # Show the user what columns there are, so that he can enter his data correctly
    def __init__(self, base_url, table_name, log_filename):
        pass

    def __del__(self):
        pass

    def get_columns(self):
        pass

    # Implement a method that allows you to query on both APIs, the books and the animals APIs
    # The input data should be a dictionary with the right fields and values. For numeric queries a dict key can also hold another dict with e.g. gt, lt keys
    def query_data(self, filter):
        pass

    # Since we only can add data on our api, it's ok if this is not generic, watch out that this api endpoint doesn't return json
    def add_data(self, data):
        pass

    # Since we only can delete data on our api, it's ok if this is not generic, watch out that this api endpoint doesn't return json
    def delete_data(self, name):
        pass

    # Make a convenience method so that you can pass it what to call and optional data and it handles common logic to all requests and logs what is happening
    # Add your own list of parameters
    def make_and_log_http_call(self):
        pass


def main():
    # Create two API Controllers one for the animals API the other for the books API
    # Add some data to the animals API, query it and delete some data
    pass

    # Query some data from the books API


if __name__ == '__main__':
    main()
