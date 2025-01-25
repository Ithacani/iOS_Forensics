import plistlib
from pprint import pprint
import sys

# Check if the input file is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python script.py <input_plist_file>")
    sys.exit(1)

# Input file path from command line argument
input_file = sys.argv[1]

# Read the plist file
with open(input_file, "rb") as file:
    plist_data = plistlib.load(file)

# Prettify and print the contents of the plist file
print("Contents of the plist file:")
pprint(plist_data)

# Modify the plist data if needed
plist_data['new_key'] = 'new_value'

# Optionally, print the modified data
print("\nModified plist data:")
pprint(plist_data)