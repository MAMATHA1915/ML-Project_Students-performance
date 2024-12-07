import sys
from logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Constructs a detailed error message with information about the error location and message.

    Args:
        error (Exception): The error instance.
        error_detail (sys): The sys module to extract traceback information.

    Returns:
        str: A detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error occurred in Python script [{file_name}] "
        f"at line number [{line_number}]: {str(error)}"
    )
    return error_message

class CustomException(Exception):
    """
    Custom exception class to handle and log detailed error messages.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.error("Division by zero error occurred.")
        raise CustomException(e, sys)
