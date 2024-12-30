import logging

# Configure logging
log_file = 'minh_test.log'  # Name of your log file
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,  # Log level (INFO, DEBUG, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  # Append mode
)

# Example log messages
logging.info("This is an informational message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
