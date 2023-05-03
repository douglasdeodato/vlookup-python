import pandas as pd

# Read the first Excel file and rename the columns
df1 = pd.read_excel('1.xlsx', names=['email', 'donor', 'name'])
print(df1)

# Read the second Excel file
df2 = pd.read_excel('2.xlsx')
print(df2)

# Remove leading spaces from names in df2
df2['name'] = df2['name'].str.strip()

# Merge the two dataframes based on the 'name' column
merged_df = pd.merge(df2, df1[['name', 'email']], on='name', how='left')

print(merged_df)
# Write the merged dataframe to a new Excel file
merged_df.to_excel('output.xlsx', index=False)

# Write the merged dataframe to a new JSON file
merged_df.to_json('output.json', orient='records')
