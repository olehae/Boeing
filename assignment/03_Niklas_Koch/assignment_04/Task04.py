import urllib.request

def open_url(url):
    try:
        request_url = urllib.request.urlopen(url)
        content = request_url.read()
        string = content.decode('utf-8')
        print(string[:200])
    except Exception as e:
        print(f"Exception: {e}")
        print(f"URL: {url}")

open_url(input("Enter a URL: "))
