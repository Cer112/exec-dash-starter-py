# monthly_sales.py

# TODO: import some modules and packages here

# TODO: write some Python code here to produce the desired functionality...

import os
<<<<<<< HEAD
import pandas

## ... adapted from: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f]".format(my_price)

CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join(os.path.dirname(_file_), "data", csv_filename)

csv_data = pandas.read_csv(csv_filepath)


#print(type(csv_data))
#print(csv_data)
#print(list(csv_data.columns))



monthly_total = csv_data["sales price"].sum()

products_sold = csv_data["product"].unique()


for product_name in products_sold:
    print(product_name)


breakpoint()

top_sellers = [
    {"rank": 1, "name": "Button-Down Shirt", "monthly_sales": 6960.35},
    {"rank": 2, "name": "Super Soft Hoodie", "monthly_sales": 1875},
=======
import csv
import itertools
import operator import itemgetter

CSV_FILENAME = "sales-201803.csv"

csv_filepath = os.path.join("data", CSV_FILENAME)


with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for od in reader:
        rows.append(dict(od)) 

sales_price = [float(row["sales price"]) for row in rows] 
total_sales = sum(sales_pries)
>>>>>>> b416c9189fcbadfab316b74a26824e492ea5e232








print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")
