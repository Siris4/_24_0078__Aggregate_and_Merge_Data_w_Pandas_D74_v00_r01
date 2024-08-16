import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0078__Day74_Aggregate_and_Merge_Data_w_Pandas__240814\NewProject\r00-r09 START\r00_env_START\data\colors.csv'
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure of the data
print(df.head())

# Determine the total number of unique colors
unique_colors_count = df['name'].nunique()

# Filter the DataFrame for transparent colors
trans_colors = df[df['is_trans'] == 't']

# Count the number of transparent colors
count_trans_colors = len(trans_colors)

print("Number of transparent colors:", count_trans_colors)

# Display the result
print(f"The total number of unique colors is: {unique_colors_count}")
