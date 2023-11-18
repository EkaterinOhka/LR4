import json


# TODO решите задачу
def task() -> float:
    filename = 'input.json'
    with open(filename, "r") as f:
        data = json.load(f)
        summ = sum([item["score"] * item["weight"] for item in data])
    return round(summ, 3)


if __name__ == '__main__':
    print(task())
