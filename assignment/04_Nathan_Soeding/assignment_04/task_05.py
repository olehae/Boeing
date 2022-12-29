import logging
import urllib.request


def init_log(file_name, file_mode, level, format, date_format):
    # Create and configure logger
    logging.basicConfig(filename=file_name,
                        format=f'%({date_format})s %({format})s',
                        filemode=file_mode)

    # Creating an object
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


def open_url(url):
    try:
        request_url = urllib.request.urlopen(url)
        content = request_url.read()
        string = content.decode('utf-8')
        print(string[:200])
    except Exception as e:
        logger.error(e)
        print(f"Exception: {e}")
        print(f"URL: {url}")


if __name__ == "__main__":
    logger = init_log("mylog.txt", "w", "DEBUG", "message", "asctime")
    open_url(input("Input an URL: "))
