
'''
process_clean_files_to_csv(columns, clean_directory_path, results_directory_path)

    make new csv file: "results_csv" in results_path directory
    
    write the list "columns" given as the function arguement to the first row of "results_csv"

    for each text file: "file" in clean_directory_path, make a row in the csv placing the numeric value behind the ":" in the corresponding column, ignoring all characters except the numeric value.
              

'''
import os
import re
import csv
from datetime import datetime
import config  

def process_clean_files_to_csv(columns, clean_directory_path, results_directory_path):
    # Create the results directory if it doesn't exist
    os.makedirs(results_directory_path, exist_ok=True)

    # Create a CSV file for the results
    csv_file_path = os.path.join(results_directory_path, "results.csv")

    # Write the list of columns to the first row of the CSV
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)

    # Define a function to extract values
    def extract_value(line, column) -> None:
        if column in config.use_raw_column_data:
            return line.split(':')[1].strip()


        match = re.search(r'(\d+/\d+/\d+|\d+:\d+:\d+\s[APap][Mm]|\d+\.\d+|\d+)(?!\^)', line)
        # # Break it down into separate patterns
        # date_pattern = r'\d+/\d+/\d+'
        # time_pattern = r'\d+:\d+:\d+\s[APap][Mm]'
        # float_pattern = r'\d+\.\d+'
        # integer_pattern = r'\d+'
        # match = re.search((date_pattern|time_pattern|float_pattern|integer_pattern)(?!\^)', line)

        if match:
            extracted_value = match.group()
            if ":" in extracted_value:
                try:
                    time_obj = datetime.strptime(extracted_value, '%I:%M:%S %p')
                    return time_obj.strftime('%H:%M:%S')
                except ValueError:
                    pass
            elif "/" in extracted_value:
                try:
                    date_obj = datetime.strptime(extracted_value, '%m/%d/%Y')
                    return date_obj.strftime('%m/%d/%Y')
                except ValueError:
                    pass

        non_numeric_match = re.search(r'(?<=:)\s*(\S.*)', line)
        if non_numeric_match:
            return non_numeric_match.group(1)

        return None

    # Iterate through text files in the clean data directory
    for file_name in os.listdir(clean_directory_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(clean_directory_path, file_name)
            values = []

            with open(file_path, 'r') as file:
                lines = file.readlines()

            for column in columns:
                extracted_value = None
                for line in lines:
                    if column in line:
                        extracted_value = extract_value(line, column)
                        if extracted_value is not None:
                            break

                values.append(extracted_value)

            # Append the extracted values to the CSV
            with open(csv_file_path, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(values)
