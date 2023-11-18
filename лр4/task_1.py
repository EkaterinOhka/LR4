# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task():
    input_data = []
    with open(INPUT_FILENAME, "r") as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            input_data.append(row)
    # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, "w") as output_file:
        json.dump(input_data, output_file, indent=4, ensure_ascii=True)

    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
