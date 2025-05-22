import csv
from BTrees.OOBTree import OOBTree
import timeit


def load_data(file_path):
    data = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(
                {
                    "ID": int(row["ID"]),
                    "Name": row["Name"],
                    "Category": row["Category"],
                    "Price": float(row["Price"]),
                }
            )
    return data


def add_item_to_tree(tree, item):
    tree[item["ID"]] = item


def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item


def range_query_tree(tree, min_price, max_price):
    result = [
        item
        for _, item in tree.items(min_price, max_price)
        if min_price <= item["Price"] <= max_price
    ]
    return result


def range_query_dict(dictionary, min_price, max_price):
    result = [
        item for item in dictionary.values() if min_price <= item["Price"] <= max_price
    ]
    return result


def main():

    file_path = "generated_items_data.csv"
    data = load_data(file_path)

    tree = OOBTree()
    dictionary = {}

    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    min_price, max_price = 50, 150

    tree_time = timeit.timeit(
        lambda: range_query_tree(tree, min_price, max_price), number=100
    )

    dict_time = timeit.timeit(
        lambda: range_query_dict(dictionary, min_price, max_price), number=100
    )

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")


if __name__ == "__main__":
    main()
