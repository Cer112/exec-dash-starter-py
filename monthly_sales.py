# monthly_sales.py

#
#loop through top sellers- last commit completed.
#




import os
import pandas
import plotly
from plotly import graph_objs

## ... adapted from: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
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


#>                    unit price  units sold  sales price
#> product
#> Button-Down Shirt     1821.40         107      6960.35
#> Super Soft Hoodie     1350.00          25      1875.00
#> Khaki Pants           1157.00          18      1602.00
#> Vintage Logo Tee       398.75          59       941.05
#> Brown Boots            250.00           2       250.00
#> Sticker Pack           108.00          48       216.00
#> Baseball Cap           156.31           7       156.31





print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print(" " + str(d["rank"]) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))


print("-----------------------")
print("VISUALIZING THE DATA...")


#
#Data Visualization
#

chart_filename = "top-sellers-201803.html" #not finding this filname in plotly
chart_filepath = os.path.join(os.path.dirname(__file__), "reports", chart_filename)

data = [
    graph_objs.Bar(
        x=sorted_products_sales,
        y=sorted_products_names,
        orientation = "h"
    )
]

chart_title = "Top Selling Products (March 2018)"

layout = graph_objs.Layout(
    title=chart_title,
    yaxis=dict(autorange="reversed")
)


chart_options = {"data": data,"layout": layout}




plotly.offline.plot(
    chart_options,
    filename=chart_filepath,
    auto_open=True
)
