import os
import pandas as pd
import re

def create_dataframe_from_text_files(directory_path, column_names):
    data = {column: [] for column in column_names}
    
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, 'r') as file:
                event_data = {column: None for column in column_names}
                
                for line in file:
                    for column in column_names:
                        pattern = fr"{column}:\s+(.*)"  # Match the column name followed by a value
                        match = re.search(pattern, line)
                        
                        if match:
                            if column == "Date of Test":
                                # Extract the date in the format "mm/dd/yyyy" using regular expression
                                date_match = re.search(r'(\d{1,2}/\d{1,2}/\d{4})', match.group(1)).group(0)
                                if date_match:
                                    event_data[column] = date_match               
                            elif column == "Time of Test":
                                event_data[column] = re.search(r'(\d{1,2}:\d{1,2}:\d{1,2})', match.group(1)).group(0)
                            elif column == "Test Device":
                                # event_data[column] = re.search(r'\w+ \d{1,2}\w{2} \w+',match.group(1)).group(0)
                                event_data[column] = re.search(r'\s+',match.group(1)).group(0)
                            elif column == "Sample No.":
                                event_data[column] = re.search(r'\d+', match.group(1)).group(0)
                            elif column == "Oscillogram No.":
                                oscillogram_match = re.search(r'(\w+-\d+)', match.group(1))
                                if oscillogram_match:
                                    event_data[column] = oscillogram_match.group(1)
                            # else:
                            #     event_data[column] = match.group(1).strip()
                
                # Append the event data to the dataframe
                for column in column_names:
                    data[column].append(event_data[column])

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Define your column names
    column_names = ["Date ", "Time of Test", "Test Device", "Main Breaker", "Branch Breaker", "Sample No.", "Oscillogram No."]
    
    # Specify the directory path containing the text files
    directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\small_data"  # Use the provided directory path
    
    # Create the dataframe
    df = create_dataframe_from_text_files(directory_path, column_names)

    # Print the dataframe
    pd.set_option('display.max_colwidth', None)
    pd.options.display.colheader_justify = 'center'
    # print(df.iloc[0])
    print(df)
