import requests
import json
from concurrent.futures import ThreadPoolExecutor

url = "https://rickandmortyapi.com/api/character"


def main_request(url: str, page: int) -> dict:
    r = requests.get(url + f"?page={page}")
    return r.json()


def get_pages(response: dict) -> str:
    pages = response["info"]["pages"]
    return pages


def parse_json(response: dict) -> dict:
    char_episodes = {}

    for item in response["results"]:
        name = item["name"]
        episode_urls = item["episode"]
        character_episodes = list()

        for episode_url in episode_urls:
            episode_response = requests.get(episode_url)

            if episode_response.status_code == 200:
                episode_response_json = episode_response.json()
                character_episodes.append(episode_response_json["name"])

        char_episodes[name] = character_episodes

    return char_episodes


def process_page(page: int) -> tuple:
    response = main_request(url, page)
    return f"page {page}", parse_json(response)


char_episodes_dict = {}
data = main_request(url, 1)
pages = get_pages(data)

num_threads = 5
executor = ThreadPoolExecutor(max_workers=num_threads)

futures = []

for page in range(1, pages + 1):
    future = executor.submit(process_page, page)
    futures.append(future)

for future in futures:
    result = future.result()
    char_episodes_dict[result[0]] = result[1]

executor.shutdown()

with open("character_episodes.json", "w") as json_file:
    json.dump(char_episodes_dict, json_file, indent=4)
