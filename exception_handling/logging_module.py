import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum log level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S',  # Date format
    filename='app.log',  # Log file name
    filemode='w'  # Overwrite the log file each time (use 'a' to append)
)

# Creating a logger object
logger = logging.getLogger()

def divide(a, b):
    try:
        logger.info(f"Attempting to divide {a} by {b}")
        result = a / b
        logger.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        raise
    except Exception as e:
        logger.exception("An unexpected error occurred: %s", e)
        raise

if __name__ == "__main__":
    logger.info("Starting the application")

    try:
        divide(10, 5)
        divide(10, 0)  # This will trigger an exception
    except Exception as e:
        logger.warning(f"Exception caught in main: {e}")

    logger.info("Application finished")
