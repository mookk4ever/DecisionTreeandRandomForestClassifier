import pandas as pd

# Load the dataset
df = pd.read_csv('./Trainingsetpcap.csv')

# Remove leading and trailing whitespaces from all string columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Strip any whitespace from the column names
df.columns = df.columns.str.strip()

# Copy 'Destination Port' to a new column 'Destination Port 1'
df['Destination Port 1'] = df['Destination Port']

# Filter rows where Protocol is TCP
df = df[df['Protocol'] == 6]

# Remove the 'Protocol' column
df.drop(columns=['Protocol'], inplace=True)

# Map the destination ports 53, 80, and 443 to their corresponding names
port_mapping = {53: 'DNS', 80: 'HTTP', 443: 'TLSv1.2'}
df['Protocol'] = df['Destination Port'].map(port_mapping)

# Calculate 'Length' as the sum of forward and backward packet lengths
df['Length'] = df['Total Length of Fwd Packets'] + df['Total Length of Bwd Packets']

# Construct the 'Info' column
df['Info'] = df['Source Port'].astype(str) + " > " + df['Destination Port 1'].astype(str) + " Len=" + df['Length'].astype(str)

# Remove rows where 'Protocol' is empty (NaN after the mapping)
df = df.dropna(subset=['Protocol'])

# Label 'Normal' traffic as 0, all others as 1
df['Label'] = df['Label'].apply(lambda x: 0 if x.lower() == 'benign' else 1)

# Add an ID column starting from 1
df.insert(0, 'ID', range(1, 1 + len(df)))

# Remove the 'Destination Port' column now that we have 'Protocol' and 'Destination Port 1'
df.drop(columns=['Destination Port'], inplace=True)

# Select and rename the necessary columns to match the test set
final_columns = ['ID', 'Source IP', 'Destination IP', 'Protocol', 'Length', 'Info', 'Label']
df_final = df[final_columns]
df_final.columns = ['ID', 'Source', 'Destination', 'Protocol', 'Length', 'Info', 'Label']

# Export the final DataFrame to a new CSV file without an index
df_final.to_csv('processed_browsing_dataset.csv', index=False)

print("\nScript finished, processed data saved to 'processed_browsing_dataset.csv'")
