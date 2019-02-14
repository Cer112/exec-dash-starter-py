# monthly_sales.py

import os
import pandas
import matplotlib.pyplot as plt

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
#Inputs
#

csv_filename = "sales-201803.csv"

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

csv_data = pandas.read_csv(csv_filepath)

#
#Calculations
#

monthly_total = csv_data["sales price"].sum()

product_totals = csv_data.groupby(["product"]).sum()



product_totals = product_totals.sort_values("sales price", ascending=False)



top_sellers = []


#breakpoint()
# (Pdb) print(type(csv_data)) #> <class 'pandas.core.frame.DataFrame'>
#
# (Pdb) csv_data.head(3)
#>          date            product  unit price  units sold  sales price
#> 0  2018-03-01  Button-Down Shirt       65.05           2       130.10
#> 1  2018-03-01   Vintage Logo Tee       15.95           1        15.95
#> 2  2018-03-01       Sticker Pack        4.50           1         4.50
#
# Get unique products
#
product_names = csv_data["product"]
# ... what kind of datatype is this?
# (Pdb) print(type(product_names)) #> <class 'pandas.core.series.Series'>
# ... google search for "pandas.core.series.Series unique values" yields: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html
unique_product_names = product_names.unique() # :-D
# (Pdb) print(unique_product_names) #> ['Button-Down Shirt' 'Vintage Logo Tee' 'Sticker Pack' 'Super Soft Hoodie' 'Baseball Cap' 'Khaki Pants' 'Brown Boots']
# ... looks like a list, but what kind of datatype is this?
# (Pdb) print(type(unique_product_names)) #> <class 'numpy.ndarray'>
# ... numpy.ndarray WAT? let's try to convert it to a list, if possible, so we can be working with familiar datatypes...
# ... google search for "how to convert numpy.ndarray to list" yields:
#  + https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.ndarray.tolist.html
#  + https://stackoverflow.com/questions/1966207/converting-numpy-array-into-python-list-structure
unique_product_names = unique_product_names.tolist() # convert numpy.ndarray to list

top_sellers=[]

#breakpoint()



print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

rank = 1
for d in top_sellers:
    print(" " + str(rank) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank + 1

print("-----------------------")
print("VISUALIZING THE DATA...")


#
#Data Visualization
#

chart_title = "Top Selling Products (March 2018)"

sorted_products = []
sorted_sales = []

for d in top_sellers:
    sorted_products.append(d["name"])
    sorted_sales.append(d["monthly_sales"])

plt.bar(sorted_products, sorted_sales)
plt.title(chart_title)
plt.xlabel("Product")
plt.ylabel("Monthly Sales (USD)")
plt.show()
