from task_05 import init_log
import urllib.request
import os


def download_file(url, path):
    try:
        if url[-4:] == ".txt":
            urllib.request.urlretrieve(url, path)
        else:
            logger.error("No text file found at given URL, download aborted!")
    except Exception as e:
        logger.error(e)
        print(f"Exception: {e}")
        print(f"URL: {url}")


if __name__ == "__main__":
    logger = init_log("mylog.txt", "w", "DEBUG", "message", "asctime")
    download_file("https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt", str(os.getcwd()))
