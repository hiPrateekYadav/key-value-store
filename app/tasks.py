from huey import RedisHuey
from utils import getData, writeData

huey = RedisHuey("key_value_store", host="localhost", port=6379)

@huey.task()
def add_to_store(key: str, value: str):
    try:
        key_value_store = getData()
        key_value_store[key] = value
        writeData(key_value_store)
    except Exception as e:
        print(f"Error adding to store: {e}")

@huey.task()
def remove_from_store(key: str):
    try:
        key_value_store = getData()
        key_value_store.pop(key, None)
        writeData(key_value_store)
    except Exception as e:
        print(f"Error removing from store: {e}")
