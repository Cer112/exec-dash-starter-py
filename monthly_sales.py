# monthly_sales.py

import operator
import os
import pandas
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#file_name = input("Please type the name of the file that you would like to input: ")
#csv_filename = file_name

path = os.path.join("data")
directory = os.listdir(path)

#used slack channel 
chosen_file = []
while True:
    file_name = input("Please type the name of the file that you would like to input: ")
    if file_name in directory:
        chosen_file.append(file_name)
        break
    else:
        print("Sorry this file name was not found, please enter a new file name")
        continue


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
#Inputs
#


csv_filename = file_name
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

csv_data = pandas.read_csv(csv_filepath)



#
#Calculations
#

#adapted from https://github.com/s2t2/exec-dash-starter-py/commits/master/monthly_sales_alt.py

monthly_total = csv_data["sales price"].sum()

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
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

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
#adapted from https://github.com/s2t2/exec-dash-starter-py/commits/master/monthly_sales_alt.py

def month_lookup(month):
	year_month={'01':'January','02':'February','03':'March','04':'April',
	'05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
	'11':'November', '12':'December'}
	return year_month[month]

month = month_lookup(csv_filename[-6:-4])
year = int(csv_filename[6:10])

chart_title = ("Top Selling Products (")+ str(month) + (" ") + str(year) + (")")

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


