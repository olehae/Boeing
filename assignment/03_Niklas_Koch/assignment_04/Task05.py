import logging
import urllib.request
from Task04 import open_url


def init_log(file_name, file_mode, level, format, date_format):
    logging.basicConfig(filename=file_name,
                        format=f'%({date_format})s %({format})s',
                        filemode=file_mode)

    inner_logger = logging.getLogger()

    match level:
        case "DEBUG":
            inner_logger.setLevel(logging.DEBUG)
        case "INFO":
            inner_logger.setLevel(logging.INFO)
        case "WARNING":
            inner_logger.setLevel(logging.WARNING)
        case "ERROR":
            inner_logger.setLevel(logging.ERROR)
        case "CRITICAL":
            inner_logger.setLevel(logging.CRITICAL)
    return inner_logger

if __name__ == "__main__":
    logger = init_log("mylog.txt", "w", "DEBUG", "message", "asctime")
    open_url(input("Enter an URL: "))
