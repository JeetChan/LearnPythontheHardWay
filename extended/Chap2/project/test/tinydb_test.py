from tinydb import TinyDB, Query
import os


def main():
    inster_datas()
    query_by_type('apple')


tiny_db = TinyDB(os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), os.pardir, 'resource',
        'weather_info.json')))


def inster_datas():
    #tiny_db.insert({'type': 'apple', 'count': 7})
    #tiny_db.insert({'type': 'peach', 'count': 3})

    tiny_db.insert({'type': 'banana', 'count': 9})
    tiny_db.insert({'type': 'orange', 'count': 6})


def query_by_type(fruit_type):
    fruit = Query()
    result = tiny_db.search(fruit.type == fruit_type)
    print(result)


if __name__ == "__main__":
    main()
