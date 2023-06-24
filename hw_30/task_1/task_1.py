import requests


def save(url: str, filename: str) -> None:
    response = requests.get(url + "/robots.txt")

    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
        print(f"File saved.")
    else:
        print(f"Error loading the file. Error code: {response.status_code}.")


save("https://www.wikipedia.org", "wikipedia_robots.txt")
save("https://www.twitter.com", "twitter_robots.txt")
save("https://dou.ua", "dou_robots.txt")
