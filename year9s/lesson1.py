import csv
import random
import os

def readfile(filename, fields=None):
    """
    :param filename (strings): name of the file to read
    :param fields (list of strings): column headers for the csv file or can be left None and
    they will be picked up based on the first line of the csv file
    """
    lines = []
    
    # https://docs.python.org/3/library/csv.html#csv.DictReader
    with open(filename, "r", encoding="utf-8") as csvFile:
        reader = csv.DictReader(csvFile, fields)
        for row in reader:
            lines.append(row)
    
    return lines


def write_to_csv(data, name, fields=None):
    """
    You can ignore this function for now. 
    :param data: a list of dictionaries (https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
    :param name: name of the file you want to save the data as
    :param fields: the column headers for the csv file
    """
    if len(data) >= 1:
        # we can automatically generate the headers of csv file if we assume that all
        # the dictionaries use the same headers
        if fields is None:
            field = list(data[0].keys())
        else:
            field = fields

        # python has a built in module/piece of code for handling reading and writing from csv files
        # https://docs.python.org/3/library/csv.html#csv.DictWriter
        with open("{}.csv".format(name), "a", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=field, quoting=csv.QUOTE_MINIMAL)

            writer.writeheader()
            for d in data:
                writer.writerow(d)

def generate_test_data(number_of_orders, name):
    """
    :param number_of_orders (int): is the number of orders to generate for the log test data
    @param name (string): is the file name that we save too
    """
    employees = ["joe", "bob", "molly", "sarah"]
    items = {"burger": 4.5, "drink":2.5, "ice cream": 3, "chicken burger":2}
    orders = []
    for i in range(number_of_orders):
        staff = random.choice(employees)
        for j in range(random.randint(1,5)):
            item = random.choice(list(items.keys()))
            # todo: https://stackoverflow.com/questions/26740227/create-random-time-stamp-list-in-python
            orders.append({"staff":staff, "item":item, "price": items.get(item), "time":1})

    write_to_csv(orders, name)
    
    

if __name__ == "__main__":
    new_name = "logs"
    if not os.path.exists("{}.csv".format(new_name)):
        generate_test_data(10, new_name)
    
    data = readfile("logs.csv")
    print("found {} lines in logs.csv file".format(len(data)))
    print("the varaible 'data' should be accessible so explore what data is in there")
    print("len(data) -> length\ndata[0] -> the first line\ndata[0]['staff'] -> who authorised that order")
    
