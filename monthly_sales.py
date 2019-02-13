# monthly_sales.py

#
#loop through top sellers- last commit completed.
#




import os
import pandas

## ... adapted from: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f]".format(my_price)

csv_filename = "sales-201803.csv"

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

csv_data = pandas.read_csv(csv_filepath)


#print(type(csv_data))
#print(csv_data)
#print(list(csv_data.columns))



monthly_total = csv_data["sales price"].sum()

product_totals = csv_data.groupby(["product"]).sum()



product_totals = product_totals.sort_values("sales price", ascending=False)

print(product_totals)

rank = 1
top_sellers = []
product_names = product_totals.index.values.tolist()
for product_name in product_names:
    monthly_sales = 10
    top_sellers.append({"rank": rank, "name": product_name, "monthly_sales": monthly_sales})


#>                    unit price  units sold  sales price
#> product
#> Button-Down Shirt     1821.40         107      6960.35
#> Super Soft Hoodie     1350.00          25      1875.00
#> Khaki Pants           1157.00          18      1602.00
#> Vintage Logo Tee       398.75          59       941.05
#> Brown Boots            250.00           2       250.00
#> Sticker Pack           108.00          48       216.00
#> Baseball Cap           156.31           7       156.31




breakpoint()

top_sellers = [
    {"rank": 1, "name": "Button-Down Shirt", "monthly_sales": 6960.35},
    {"rank": 2, "name": "Super Soft Hoodie", "monthly_sales": 1875},
]

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
