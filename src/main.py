
import config
import clean_raw
import dataframe_builder

# Check if the script is being run as the main program
if __name__ == "__main__":

    # Call the function to make deletions and replacements
    clean_raw.clean_up_output(dirty_directory_path=config.dirty_directory_path,
                              clean_directory_path=config.clean_directory_path,
                              replacements=config.replacements)

    # build CSV from cleaned data
    dataframe_builder.process_clean_files_to_csv(columns=config.columns,
                                                 clean_directory_path=config.clean_directory_path,
                                                 results_directory_path=config.results_directory_path)
