
import config
import pdf_scrape
import clean_raw
import dataframe_builder
import parser

# Check if the script is being run as the main program
if __name__ == "__main__":

    pdf_scrape.pdf_scrape(pdf_directory=config.pdf_directory,
                          raw_output_directory=config.raw_output_directory)

    # Call the function to make deletions and replacements
    clean_raw.clean_up_output(dirty_directory_path=config.raw_output_directory,
                              clean_directory_path=config.clean_directory_path,
                              replacements=config.replacements)
    
    # parse test device line                          
    parser.run_parser(clean_directory_path=config.clean_directory_path)
    
    # build CSV from cleaned data
    dataframe_builder.process_clean_files_to_csv(columns=config.columns,
                                                 clean_directory_path=config.clean_directory_path,
                                                 results_directory_path=config.results_directory_path)
