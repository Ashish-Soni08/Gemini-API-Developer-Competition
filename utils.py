import requests

# load lottie file from url
def load_lottieurl(url: str):
    try:
        # Send a GET request to the url
        r = requests.get(url)
        # Check if the request was successful
        if r.status_code == 200:
            return r.json()
        else:
            return f"Failed to retrieve the lottie file {r.status_code}"
    except Exception as e:
        print(e)
        return f"Failed to retrieve the lottie file {e}"