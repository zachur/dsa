import sqlite3

# Accept user input and store it in a variable
db_name = input("Enter file name of database (blank for default): ")

# Check if user input is empty (blank)
if not db_name:
    db_name = 'example.db'  # Set the default value

# Connect to the SQLite database
conn = sqlite3.connect(db_name)

# Create a cursor object
cursor = conn.cursor()

# Define the table name
table_name = input("Enter table name (blank for default): ")
if not table_name:
    table_name = 'mytable'

# Check if the table exists in the database
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
result = cursor.fetchone()

if result:
    # Table exists, fetch the schema (column headers)
    cursor.execute(f"PRAGMA table_info({table_name})")
    schema = cursor.fetchall()
    
    # Print column headers (schema)
    if schema:
        column_headers = [row[1] for row in schema]
        print("Column Headers (Schema): " + ", ".join(column_headers))
    else:
        print(f"The table '{table_name}' exists, but it has no columns.")
    
    # Fetch and display table contents
    cursor.execute(f"SELECT * FROM {table_name}")
    table_contents = cursor.fetchall()
    
else:
    print(f"The table '{table_name}' does not exist in the database.")

# Define the column name
column_name = input("Enter column name (blank for default): ")
if not column_name:
    column_name = 'Number_of_Stars'  # Set the default value

# Define the SQL query to select the specified column
sql_query = f'SELECT {column_name} FROM {table_name}'

# Execute the SQL query and fetch the results
cursor.execute(sql_query)
column_data = cursor.fetchall()

# Close the database connection
conn.close()

# Specify the output file name
output_file = 'output.txt'

# Open the text file in write mode
with open(output_file, 'w') as text_file:
    # Iterate through the column data and write each value as a line/row
    for row in column_data:
        text_file.write(str(row[0]) + '\n')

print(f"Data from '{column_name}' column written to '{output_file}'")

# Close the database connection
conn.close()

# Convert "k" suffixes to integers
if column_name == 'Number_of_Stars':
    # Function to convert a string value with "k" to an integer
    def convert_to_int(value):
        if value.endswith('k'):
            return int(float(value[:-1]) * 1000)  # Remove 'k', convert to float, and multiply by 1000
        else:
            return int(value)  # No 'k', directly convert to integer

    # Read data from the 'output.txt' file and convert it to integers
    converted_data = []
    with open('output.txt', 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespaces and newlines
            converted_data.append(str(convert_to_int(line)))  # Convert to int and then back to str

    # Write the converted values to 'output.txt' file
    with open('output.txt', 'w') as output_file:
        output_file.write('\n'.join(converted_data))

    def remove_duplicates_and_sort(input_file_path, output_file_path):
        unique_values = set()

        # Read the input file and collect unique values
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                try:
                    value = int(line.strip())
                    unique_values.add(value)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

        # Sort the unique values
        sorted_values = sorted(unique_values)

        # Write the sorted values to the output file
        with open(output_file_path, 'w') as output_file:
            for value in sorted_values:
                output_file.write(f"{value}\n")

    input_file_path = 'output.txt'
    output_file_path = 'output.txt'

    remove_duplicates_and_sort(input_file_path, output_file_path)

    print("Duplicates removed and sorted values saved to the output file.")

