import csv
import sqlite3

# Define the CSV file path
csv_file_path = 'gh_t980.csv'

# Initialize a counter for populated rows
populated_row_count = 0

# Open the CSV file in read mode
with open(csv_file_path, 'r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)
    # Skip the header row
    next(csv_reader, None)
    # Loop through the rows and count populated ones
    for row in csv_reader:
        if any(row):
            populated_row_count += 1

# Open the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Specify the table name
table_name = 'mytable'

# Open the CSV file in read mode
with open(csv_file_path, 'r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)
    
    # Read the headers and sanitize them for SQLite
    headers = next(csv_reader)
    sanitized_headers = [header.replace(" ", "_").replace("-", "_") for header in headers]
    
    # Define the SQL CREATE TABLE statement
    create_table_sql = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        {", ".join([f"{header} TEXT" for header in sanitized_headers])}
    )
    '''
    
    # Execute the CREATE TABLE statement
    cursor.execute(create_table_sql)
    
    # Initialize a counter to track the number of rows inserted
    num_rows_inserted = 0

    # Read and insert data
    for row in csv_reader:
        insert_sql = f'''
        INSERT INTO {table_name} ({", ".join(sanitized_headers)})
        VALUES ({", ".join(['?'] * len(sanitized_headers))})
        '''
        cursor.execute(insert_sql, row)
        
        num_rows_inserted += 1
        
        if num_rows_inserted >= populated_row_count:
            break  # Exit the loop
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
