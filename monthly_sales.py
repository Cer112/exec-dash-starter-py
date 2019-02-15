# monthly_sales.py

import operator
import os
import pandas
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

unique_product_names = product_names.unique() 

unique_product_names = unique_product_names.tolist() 

top_sellers=[]

for product_name in unique_product_names:
    matching_rows = csv_data[csv_data["product"] == product_name]
    product_monthly_sales = matching_rows["sales price"].sum()
    top_sellers.append({"name": product_name, "monthly_sales": product_monthly_sales})

#sort the list
top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)




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

sorted_products.reverse()
sorted_sales.reverse()

fig, ax = plt.subplots() 
usd_formatter = ticker.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(usd_formatter)

plt.barh(sorted_products, sorted_sales)
plt.title(chart_title)
plt.ylabel("Product")
plt.xlabel("Monthly Sales (USD)")

plt.tight_layout()
plt.show()


#Code used from Professor Rosetti exec-dash-starter-py