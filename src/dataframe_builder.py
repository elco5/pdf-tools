
'''
process_clean_files_to_csv(columns, clean_data_directory_path, results_directory_path)

    make new csv file: "results_csv" in results_path directory
    
    write the list "columns" given as the function arguement to the first row of "results_csv"

    for each text file: "file" in clean_data_directory_path, make a row in the csv placing the numeric value behind the ":" in the corresponding column, ignoring all characters except the numeric value.
              

'''
import os
import csv
import re
from datetime import datetime

import config




def process_clean_files_to_csv(columns, clean_data_directory_path, results_directory_path):
    # Create the results directory if it doesn't exist
    if not os.path.exists(results_directory_path):
        os.makedirs(results_directory_path)

    # Create a CSV file for the results
    csv_file_path = os.path.join(results_directory_path, "results_csv.csv")

    # Write the list of columns to the first row of the CSV
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)

    # Iterate through text files in the clean data directory
    for file_name in os.listdir(clean_data_directory_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(clean_data_directory_path, file_name)
            values = []

            with open(file_path, 'r') as file:
                lines = file.readlines()

            for column in columns:
                extracted_value = None
                for line in lines:
                    if column in line:
                        if column in config.use_raw_column_data:
                            extracted_value = line.split(':')[1].strip()
                            break
                        match = re.search(r'(\d+/\d+/\d+|\d+:\d+:\d+\s[APap][Mm]|\d+)', line)
                        if match:
                            extracted_value = match.group()
                            # Handle date and time format
                            if ":" in extracted_value:
                                try:
                                    time_obj = datetime.strptime(extracted_value, '%I:%M:%S %p')
                                    extracted_value = time_obj.strftime('%H:%M:%S')
                                except ValueError:
                                    pass  # Not a valid time format
                            elif "/" in extracted_value:
                                try:
                                    date_obj = datetime.strptime(extracted_value, '%m/%d/%Y')
                                    extracted_value = date_obj.strftime('%m/%d/%Y')
                                except ValueError:
                                    pass  # Not a valid date format
                            break
                if extracted_value is None:
                    # If no numeric value was found, populate the column with the non-numeric value found
                    for line in lines:
                        if column in line:
                            non_numeric_match = re.search(r'(?<=:)\s*(\S.*)', line)
                            if non_numeric_match:
                                extracted_value = non_numeric_match.group(1)
                            break
                values.append(extracted_value)

            # Append the extracted values to the CSV
            with open(csv_file_path, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(values)


# Example usage:
columns = config.cols
clean_data_directory_path = config.clean_data_directory_path
results_directory_path = config.results_directory_path

process_clean_files_to_csv(columns, clean_data_directory_path, results_directory_path)

