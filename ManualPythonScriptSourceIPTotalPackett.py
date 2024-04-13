import pandas as pd

# Assuming your data is stored in a CSV file named 'data.csv'
file_path = '/Users/jerry/Documents/Assignment/Dados_Deolindo/dataset_7.csv'
data = pd.read_csv(file_path)

# Check if 'Label' column exists
if ' Label' in data.columns:
    # Count total entries under the 'Label' column
    total_entries = len(data)

    # Count the number of PortScan entries under the 'Label' column
    total_portscan = (data[' Label'] == 'PortScan').sum()

    # Calculate percentage
    percentage_portscan = (total_portscan / total_entries) * 100

    print("Percentage of PortScan to total under label: {:.2f}%".format(percentage_portscan))
else:
    print("The 'Label' column does not exist in the dataset.")
