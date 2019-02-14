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
rank = 1
for i, row in product_totals.iterrows():
        d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
        top_sellers.append(d)
        rank = rank + 1

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
plt.xlabel("product")
plt.ylabel("Monthly Sales (USD)")
plt.show()
