import csv
from datetime import datetime

# Open the input file
with open('dataset_7.csv', mode='r') as infile:
    reader = csv.DictReader((line.replace('\0', '') for line in infile), delimiter=',')

    actual_fieldnames = reader.fieldnames
    fieldname_mapping = {f.strip(): f for f in actual_fieldnames}

    fieldnames = ['Timestamp', 'Source IP', 'Source Port', 'Destination IP', 'Destination Port', 'TCP Length', 'Label']

    with open('Testsetgood.csv', mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Parse the existing timestamp and reformat it
            timestamp = datetime.strptime(row[fieldname_mapping['Timestamp']].strip(), '%m/%d/%Y %H:%M')
            formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

            output_row = {
                'Timestamp': formatted_timestamp,
                'Source IP': row[fieldname_mapping['Source IP']].strip(),
                'Source Port': row[fieldname_mapping['Source Port']].strip(),
                'Destination IP': row[fieldname_mapping['Destination IP']].strip(),
                'Destination Port': row[fieldname_mapping['Destination Port']].strip(),
                'TCP Length': row[fieldname_mapping['Total Length of Fwd Packets']].strip(),
                'Label': 1 if row[fieldname_mapping['Label']].strip() == 'PortScan' else 0
            }

            writer.writerow(output_row)
