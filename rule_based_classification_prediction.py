'''Task 1: A gaming company wants to create level-based personas using some characteristics of its customers, create segments
based on these new customer personas, and estimate how much new customers can earn on average for the company based
on these segments.For example:We want to determine how much a 25-year-old male IOS user from Turkey can earn on
average.
The Persona.csv dataset contains the prices of products sold by an international gaming company and some
demographic information of the users who purchased these products. The dataset is made up of records from each sales
transaction. This means that the table is not deduplicated. In other words, a user with certain demographic
characteristics may have made more than one purchase.'''

'''Question 1: Read the persona.csv file and show the general information about the dataset.'''
import pandas as pd

df = pd.read_csv('persona.csv')
print(df.head())

''' Question 2: How many unique SOURCEs are there? What is their frequency?'''
df = df["SOURCE"].unique()
df = df["SOURCE"].value_counts()
print(df)
'''Question 3: How many unique PRICE are there?'''
df = df["PRICE"].nunique()
print(df)

''' Question 4: How many sales are there from PRICE?'''
df = df["PRICE"].value_counts()
print(df)

'''Question 5: How many sales were there from each country?'''

df = df["COUNTRY"].value_counts()
print(df)

'''Question 6: How much was earned from sales by country?'''
df = df.groupby("COUNTRY")["PRICE"].sum()
print(df)
df = df.groupby("COUNTRY").agg({"PRICE": "sum"})
print(df)

'''Question 7: What is the number of sales by SOURCE types?'''
df = df["SOURCE"].value_counts()
print(df)

'''Question 8: What are the PRICE averages by country?'''

df = df.groupby("COUNTRY")["PRICE"].mean()
print(df)

df = df.groupby("COUNTRY").agg({"PRICE": "mean"})
print(df)

'''Question 9: What is the average PRICE by SOURCE?'''
df = df.groupby("SOURCE")["PRICE"].mean()
print(df)

'''Question 10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?'''

df = df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})
print(df)

'''Task 2: What are the average earnings by COUNTRY, SOURCE, SEX, AGE?'''

df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})
print(df)

'''Task 3: Sort the output according to PRICE.- To see the output from the previous question better, 
apply the sort_values method in descending order according to PRICE.Save the output as agg_df.'''

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE",ascending=False)
print(agg_df.head())

'''Task 4: Convert the names in the index to variable names.- In the output of the third question, all variables 
except PRICE are index names. Convert these names to variable names.'''

agg_df = agg_df.reset_index()
print(agg_df)

'''Task 5: Convert age into a categorical variable and add it to agg_df. - Convert the numeric variable Age into a categorical variable.
- Construct the intervals in a convincing way.
- For example: '0_18', '19_23', '24_30', '31_40', '41_70' '''
#The pandas.cut() function is used to bin values into discrete intervals.

# We create a new column in the agg_df DataFrame called AGE_CAT.
agg_df["AGE"] = agg_df["AGE"].astype("category")

label = ["0_18", "19_23", "24_30", "31_40", "41_70"]
#We use the pd.cut() function to bin the values in the AGE column into six categories.
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0,18,23,30,40,70], labels=label)
print(agg_df.head())

# the x argument is the AGE column, the bins argument is a list of age ranges, and the labels argument is the list of
# labels that we defined in the previous line of code.


'''Task 6: Define new level-based customers (persona).
- Define new level-based customers (persona) and add them as a variable to the dataset.
- Name of the new variable: customers_level_based
- You need to create the variable customers_level_based by combining the observations in the output from the previous question.'''

agg_df["customer_level_based"] = [str(i[0]).upper() + "_" + str(i[1]).upper() + "_" + str(i[2]).upper() + "_" + str(i[5]).upper() for i in agg_df[agg_df.columns].values]
agg_df = agg_df.groupby("customer_level_based").agg({"PRICE": "mean"}).reset_index()
print(agg_df["customer_level_based"].value_counts())


'''Task 7: Segment new customers (personas).
- Divide new customers (Example: USA_ANDROID_MALE_0_18) into 4 segments according to PRICE.
- Add the segments to agg_df as a variable with SEGMENT naming.
- Describe the segments (group by segments and get price mean, max, sum).
'''
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})
print(agg_df)

'''Task 8: Categorize new customers and estimate how much revenue they can bring in.
- Which segment does a 33-year-old Turkish woman using ANDROID belong to and how much income is she expected to earn on average?
- Which segment does a 35-year-old French woman using IOS belong to and how much income is she expected to earn on average?'''

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df = agg_df[agg_df["customer_level_based"] == new_user]
print(agg_df)


new_user_two = "FRA_IOS_FEMALE_31_40"
agg_df = agg_df[agg_df["customer_level_based"] == new_user_two]
print(agg_df)




























