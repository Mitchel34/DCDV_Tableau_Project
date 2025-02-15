import pandas as pd

# Load your dataset
df = pd.read_csv("./SofwareDeveloperIncomeExpensesperUSACity.csv")

# Create a new column 'city_no_state' by splitting the 'City' column
df['city_no_state'] = df['City'].apply(lambda x: x.split(',')[0])

# Save the updated CSV file (optional)
df.to_csv("Updated_Dataset.csv", index=False)

# Display the first few rows to verify
print(df.head())


