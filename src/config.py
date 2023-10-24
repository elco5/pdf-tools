# Define the dictionary of word replacements
replacements = {
    "Was the Breaker Tripped after the test?": "breaker_tripped: ",
    "Could the Breaker be Reset?": "breaker_reset: ",
    "Did it have continuity in all poles?": "breaker_continuity: ",
    "Was the Enclosure Fuse Opened?": "enclosure_fuse_open: ",
    "Closing Angle": "closing_angle: ",
    "Closing time  (V0)+": "closing_time: ",
    "Peak Current (Ip)": "peak_current: ",
    "Time to Ip": "time_to_peak_current: ",
    "I2T": "i_2_t: ",
    "I Duration": "i_duration: ",
    "Sample No.:": "\nsample: ",
    "Oscillogram No.:":"\noscillogram: ",
    "Date of Test:": "test_date: ",
    "  Time of Test:": "\ntime_of_test: ",
    " Comment Section": "\nCOMMENT SECTION",
    "  Calibration Date:": "\ncalibration_date:",
    "2OCV =": "\nOCV:",
    " Rms Sym Current =": "\ngrid_rms_sym_current: ",
    "Power Factor =": "\npower_factor:",
    "  OCV = 244 V":"",
    "  OCV = 240 V":"",
    "AVAILABLE CIRCUIT CHARACTERISTICS:":"\nAVAILABLE CIRCUIT CHARACTERISTICS",
    "ANALYSIS RESULTS TABLE":"",
    "Osc. No:":"",
    " Comment Section":"\nComments: ",
    # Add more word replacements as needed
}

# remove lines beginning with these words / strings
line_removal_target_words = ["Voltage",
                                "Current",
                                "High",
                                " ",
                                "Sweep#",
                                "NOTE",
                                "Data",
                                "-",
                                "Cedar",
                                "INSTRUMENTATION",
                                "PERFORMANCE",
                                "Performance",
                                "ANALYSIS",
                                "AVAILABLE",
                                "GRID",
                                "INVESTIGATION",
                                "OSC",
                                
                                ]
                                
cols = [
    "test_date",
    "time_of_test",
    "rms_sym_current",
    "main_brand",
    "main_aisc_ka",
    "branch_brand",
    "branch_rating",
    "closing_time",
    "peak_current",
    "time_to_peak_current",
    "i_2_t",
    "closing_angle",
    "power_factor",
    "i_duration",
    "oscillogram",
    "sample",
    "breaker_tripped",
    "breaker_reset",
    "breaker_continuity",
    "enclosure_fuse_open",
    "calibration_date",
    "comments"
]
use_raw_column_data = [
    "oscillogram",
    "breaker_tripped",
    "breaker_reset",
    "breaker_continuity",
    "main_brand",
    "branch_brand",
    
]

clean_data_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\clean_outputs"
results_directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\data\results"
