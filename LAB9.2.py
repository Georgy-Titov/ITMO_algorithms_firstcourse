class KeyValueStorage:
    def __init__(self):
        self.storage = {}

    def find(self, key):
        return self.storage.get(key, None)

    def add(self, key, value):
        if self.find(key) is None:
            self.storage[key] = value
            return True
        else:
            return None

    def remove(self, key):
        if self.find(key) is not None:
            del self.storage[key]
            return True
        else:
            return None


def algorithm(data):
    kv_storage = KeyValueStorage()
    result = []

    for operation in range(len(data)):
        op, key_value = data[operation].split(" ", 1)
        if op not in "-?":
            key, value = key_value.split()
            if kv_storage.add(key, value) is not None:
                result.append(f"Operation №{operation + 1} successfully added")
            else:
                result.append(f"Operation №{operation + 1} already added")
        else:
            key = key_value
            if op == "-":
                if kv_storage.remove(key) is not None:
                    result.append(f"Operation №{operation + 1} successfully removed")
                else:
                    result.append(f"Operation №{operation + 1}  nothing to remove")
            else:
                if kv_storage.find(key) is not None:
                    result.append(kv_storage.find(key))
                else:
                    result.append("Not found")

    return result


# Примеры использования:
operations = ["+ key1 value1", "+ key2 value2", "- key1", "? key2", "? key3"]
print(*algorithm(operations), sep="\n")
print()
operations = ["+ key1 value1", "+ key2 value2", "+ key3 value3", "? key1", "? key2", "? key3"]
print(*algorithm(operations), sep="\n")
