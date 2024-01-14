import json

INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE) as file:
        data = json.load(file)

    values_prod = [item["score"] * item["weight"] for item in data]
    return round(sum(values_prod), 3)


print(task())
