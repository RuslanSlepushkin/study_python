import requests
import json


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


char_episodes_dict = {}
data = main_request(url, 1)

for x in range(1, get_pages(data) + 1):
    char_episodes_dict[f"page {x}"] = parse_json(main_request(url, x))

with open("character_episodes.json", "w") as json_file:
    json.dump(char_episodes_dict, json_file, indent=4)
