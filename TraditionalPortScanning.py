import pandas as pd

# Load the dataset
df = pd.read_csv('./KaggleLabelledData.csv')

# Filter for TCP protocol (assuming '6' indicates TCP)
tcp_df = df[df['Protocol'] == 6]

# Define criteria for port scanning:
# High number of forward packets and low number of backward packets (spkts and dpkts columns)
# For this example, let's assume that a port scan attempt would have more than 5 forward packets and less than 2 backward packets
suspected_port_scans = tcp_df[(tcp_df['Total.Fwd.Packets'] > 5) & (tcp_df['Total.Backward.Packets'] < 2)]

# Optional: Consider adding more criteria such as:
# - Short flow duration
# - High rate of packet sending
# - Specific TCP flags set (e.g., only SYN set without ACK)

# Save the suspected port scans to a new CSV file
suspected_port_scans.to_csv('suspected_port_scans2.csv', index=False)
