#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import Path from pathlib and import csv
from pathlib import Path
import csv


# In[2]:


# set the file path using pathlib
budget_path = Path("Resources/budget_data.csv")


# In[3]:


# Your task is to create a Python script that analyzes the records to calculate:
# The total number of months included in the dataset.
# The net total amount of Profit/Losses over the entire period.
# The average of the changes in Profit/Losses over the entire period.
# The greatest increase in profits (date and amount) over the entire period.
# The greatest decrease in losses (date and amount) over the entire period.


# In[4]:


# initialize variables to be analyzed
total_months = 0
total_profit_loss = 0
max_profit = 0
max_loss = 0


# In[5]:


# inititalize dictionary for pnl analysis
pnl_analysis = {}
date_list = []
pnl_list = []


# In[6]:


# open the csv file as an object
with open (budget_path, "r") as csvfile:
    # pass the csv file to the csv.reader() function as comma delimited
    csvreader = csv.reader(csvfile, delimiter=",")
    # read the header row first
    budget_header = next(csvreader)
    # read the rows after the header
    for row in csvreader:
        # set the date and profit/losses variables
        # convert profit/losses to integer
        date = row[0]
        profit_loss = int(row[1])
        # create lists from csv file
        date_list.append(date)
        pnl_list.append(profit_loss)


# In[7]:


# create total amounts
for item in pnl_list:
    total_months += 1
    total_profit_loss += item


# In[8]:


# calculate the profit/loss change by month in pnl_list
pnl_list_change = [pnl_list[i+1]-pnl_list[i] for i in range(len(pnl_list)-1)]


# In[9]:


# initialize variables for new list
change_total = 0
count_total = 0


# In[10]:


# define max and min profit/loss change in list of changes
for value in pnl_list_change:
    # calculate the greatest profit and loss
    if max_loss == 0:
        max_loss = value
    elif value < max_loss:
        max_loss = value
    elif value > max_profit:
        max_profit = value
    # calculate total and count
    change_total += value
    count_total += 1


# In[11]:


# set variables to call the index of the date with greatest increase/decrease
max_profit_index = pnl_list_change.index(max_profit)+1
max_loss_index = pnl_list_change.index(max_loss)+1


# In[12]:


# create variables to show the month of greatest increase/decrease
max_profit_month = date_list[max_profit_index]
max_loss_month = date_list[max_loss_index]


# In[13]:


# calculate average profit/loss
average_profit_loss = round(change_total / count_total,2)


# In[14]:


# set output path for text file
output_path = "pybank_financial_analysis.txt"


# In[15]:


# create the output file with summary
with open(output_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_profit_loss}\n")
    file.write(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})\n")
    file.write(f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})")


# In[ ]:




