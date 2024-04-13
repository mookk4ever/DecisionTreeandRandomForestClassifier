import pandas as pd
from collections import defaultdict

# Function to calculate suspected port scanning activity
def detect_port_scanning(data, packet_threshold=100, unique_ip_threshold=5):
    # Initialize dictionaries to store packet counts and unique destination IPs for each source IP
    packet_counts = defaultdict(int)
    unique_ips = defaultdict(set)
    suspected_ips = set()

    # Iterate over each row in the dataframe
    for index, row in data.iterrows():
        # Extract relevant information
        source_ip = row['Source IP']
        destination_ip = row['Destination IP']

        # Update packet counts and unique destination IPs for the source IP
        packet_counts[source_ip] += 1
        unique_ips[source_ip].add(destination_ip)

    # Check if the packet count or unique destination IP count exceeds the threshold for each source IP
    for source_ip in packet_counts:
        if packet_counts[source_ip] > packet_threshold or len(unique_ips[source_ip]) > unique_ip_threshold:
            suspected_ips.add(source_ip)

    # Add a new column to indicate suspected port scanning activity
    data['Suspected Port Scanning'] = data['Source IP'].apply(lambda x: 1 if x in suspected_ips else 0)

    return data

# Read your dataset CSV file
data = pd.read_csv('/Users/jerry/Documents/Assignment/Dados_Deolindo/Testsetgood.csv')

# Call the function to detect suspected port scanning activity
data_with_detection = detect_port_scanning(data)

# Calculate the percentage of suspected port scanning activity in the dataset
percent_suspected = (data_with_detection['Suspected Port Scanning'].sum() / len(data_with_detection)) * 100

# Print the percentage of suspected port scanning activity
print("Percentage of Suspected Port Scanning Activity: {:.2f}%".format(percent_suspected))
