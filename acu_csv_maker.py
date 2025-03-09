import csv
import sys
import os

# Check if an input file was provided
if len(sys.argv) < 2:
    print('Usage: python program.py <input file>')
    sys.exit(1)

# Get the name of the input file from the command line
input_file = sys.argv[1]

# Construct the output file names
base_name = os.path.splitext(input_file)[0]

# Read the input file
with open(input_file, 'r') as f:
    addresses = f.read().splitlines()

# Split and write addresses in chunks of 500
chunk_size = 500
num_chunks = (len(addresses) + chunk_size - 1) // chunk_size

for i in range(num_chunks):
    chunk = addresses[i * chunk_size:(i + 1) * chunk_size]
    output_file = f"{base_name}_part{i + 1}.csv"
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for address in chunk:
            writer.writerow([address, ''])
    
    print(f'Written {len(chunk)} lines to {output_file}')
