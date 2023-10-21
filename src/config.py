# Define the dictionary of word replacements
replacements = {
    "Performance Observations": "PERFORMANCE OBSERVATIONS",
    "Was the Breaker Tripped after the test?": "breaker_tripped: ",
    "Could the Breaker be Reset?": "breaker_reset: ",
    "Did it have continuity in all poles?": "breaker_continuity: ",
    "Was the Enclosure Fuse Opened?": "enclosure_fuse_open: ",
    "NoANALYSIS RESULTS TABLE": "No\n\nANALYSIS RESULTS TABLE",
    "Closing Angle": "closing_angle: ",
    "Closing time  (V0)+": "closing_time: ",
    "Peak Current (Ip)": "peak_current: ",
    "Time to Ip": "time_to_peak_current: ",
    "I2T": "I_sqared_t: ",
    "I Duration": "I_duration: ",
    "Sample No.:": "\nsample: ",
    "Oscillogram No.:":"\noscillogram: ",
    "  Time of Test:": "\ntime_of_test: ",
    " Comment Section": "\nCOMMENT SECTION",
    "  Calibration Date:": "\ncalibration_ate:",
    "2OCV =": "\nOCV:",
    " Rms Sym Current =": "\nrms_sym_current: ",
    "Power Factor =": "\npower_factor:",
    "   OCV = 244 V":"",
    "AVAILABLE CIRCUIT CHARACTERISTICS:":"\nAVAILABLE CIRCUIT CHARACTERISTICS",
    "OSC. NO.:":"",
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
                                
                                ]
                                
# Specify the directory path where the text files are located
directory_path = r"C:\Users\ecountrywood\dev\tools\pdf_tools\replace_dir\output"
