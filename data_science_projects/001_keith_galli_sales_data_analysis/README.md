# Electronics Store Sales Data Analysis for 2019

## Dataset Information

This dataset contains hundreds of thousands of electronics store purchases broken down by month, product type, cost, purchase address, etc. as 12 *.csv files, 1 for each month of 2019.

## Data Preparation:

We prepare our data for analysis by:
- Handling missing values in the dataframe
- Removing duplicated column header at multiple locations in the dataframe (.astype(), .to_datetime())
- Setting data types for each column, including setting datetime format for the date column
- Combining 12 months of sales data into one master dataframe

## Data Analysis & Questions Answered

Once we have cleaned the data up, we move the data analysis section, where we answer 5 high level business questions related to our data:
- Question 1: What was the best month for sales? How much was earned that month?
- Question 2: What city had the highest sales in 2019?
- Question 3: At what time of the day should we display advertisements to maximize the likelihood of customers buying our products?
- Question 4: Which (two) products are most often sold together?
- Question 5: What product sold in the highest quantity? Why do you think this product had the highest quantity sold?

To answer these questions we walk through many different pandas & matplotlib methods. They include:
- Concatenating multiple csvs together to create a new DataFrame (pd.concat)
- Adding columns
- Parsing cells as strings to make new columns (.str)
- Using the .apply() method
- Using groupby to perform aggregate analysis
- Plotting bar charts and lines graphs to visualize our results
- Labeling our graphs

## Visualizations Used:

To answer the questions above we have created the following visualizations:
- Bar plots
- Histograms
- Scatter plots (annotated)

## Tools/Libraries Used:

Python3 and Jupyter Notebook have been used for the code of this project.

The libraries used are:
- pandas
- matplotlib
- os
- itertools
- collections
