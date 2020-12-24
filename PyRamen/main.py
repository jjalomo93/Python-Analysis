#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
from pathlib import Path
import csv


# In[2]:


# Read in `menu_data.csv` and set its contents to a separate list object.
# (This way, you can cross-reference your menu data with your sales data as you read in your sales data in the coming steps.)
# set the file path for menu_csv
menu_path = Path("Resources/menu_data.csv")


# In[3]:


# Initialize an empty `menu` list object to hold the contents of `menu_data.csv`.
menu = []


# In[4]:


# Use a `with` statement and open the `menu_data.csv` by using its file path.
with open(menu_path, "r") as csvfile:
    # Use the `reader` function from the `csv` library to begin reading `menu_data.csv`.
    menu_reader = csv.reader(csvfile, delimiter=",")
    # Use the `next` function to skip the header (first row of the CSV).
    menu_header = next(menu_reader)
    # Loop over the rest of the rows and append every row to the `menu` list object (the outcome will be a list of lists).
    for row in menu_reader:
        # add items to the menu list
        menu.append(row)


# In[5]:


# Set up the same process to read in `sales_data.csv`. However, instead append every row of the sales data to a new `sales` list object
# set the file path for sales_data
sales_path = Path("Resources/sales_data.csv")


# In[6]:


# Initialize an empty 'sales' list object to hold the contents of 'sales_data.csv'
sales = []


# In[7]:


# Use a `with` statement and open the `sales_data.csv` by using its file path.
with open(sales_path, "r") as csvfile:
    # Use the `reader` function from the `csv` library to begin reading `menu_data.csv`.
    sales_reader = csv.reader(csvfile, delimiter=",")
    # Use the `next` function to skip the header (first row of the CSV).
    sales_header = next(sales_reader)
    # Loop over the rest of the rows and append every row to the `menu` list object (the outcome will be a list of lists).
    for row in sales_reader:
        # add items to the menu list
        sales.append(row)


# In[8]:


# Initialize an empty `report` dictionary to hold the future aggregated per-product results.
# The `report` dictionary will eventually contain the following metrics:
# * `01-count`: the total quantity for each ramen type
# * `02-revenue`: the total revenue for each ramen type
# * `03-cogs`: the total cost of goods sold for each ramen type
# * `04-profit`: the total profit for each ramen type
report = {}


# In[9]:


# Then, loop through every row in the `sales` list object.
for sales_data in sales:
    # For each row of the `sales` data, set the following columns of the sales data to their own variables:
    # * Quantity
    # * Menu_Item
    quantity = int(sales_data[3])
    menu_item = sales_data[4]
    # define variable for the record
    record = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0,}
    # Perform a quick check if the `sales_item` is already included in the `report`.
    if menu_item not in report:
        # If not, initialize the key-value pairs for the particular `sales_item` in the report.
        # Then, set the `sales_item` as a new key to the `report` dictionary and the values as a nested dictionary containing the record
        report[menu_item] = record
    # set the elif to add the "quantity" data to the count
    if menu_item in report:
        report[menu_item]["01-count"] += quantity


# In[11]:


# Create a nested loop by looping through every record in 'menu'
for sales_data in sales:
    # set the values to compare against menu data
    quantity = int(sales_data[3])
    menu_item = sales_data[4]
    
    for menu_data in menu:
        # For each row of the `menu` data, set the following columns of the menu data to their own variables:
        item = menu_data[0]
        price = float(menu_data[3]) # float because there are decimals in price data
        cost = int(menu_data[4])
        # If the `sales_item` in sales is equal to the `item` in `menu`
        # capture the `quantity` from the sales data and the `price` and `cost` from the menu data to calculate the `profit` for each item.
        if menu_item == item:
            report[item]["02-revenue"] += (quantity * price)
            report[item]["03-cogs"] += (quantity * cost)
        # else:
            # print(f"{menu_item} does not equal {item}! NO MATCH!)


# In[14]:


# define and add the profit to the report (revenue - cogs)
# use nested for loop to calculate at the individual level
for menu_item, value_dict in report.items():
    for key in value_dict:
        # define the revenue, cogs, and profit variables
        revenue = report[menu_item]["02-revenue"]
        cogs = report[menu_item]["03-cogs"]
        profit = (revenue - cogs)
        
        # set the profit based on the "04-profit" key value
        if key == "04-profit":
            report[menu_item][key] = profit


# In[17]:


# print(report) to check values


# In[18]:


# set the output path for the text file
output_path = "pyramen_results.text"


# In[19]:


# write the text file
with open(output_path, "w") as file:
    for key in report:
        file.write(f"{key} {report[key]}\n")

