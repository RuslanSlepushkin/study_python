import asyncio
import aiohttp
import json
from typing import Optional

url = "https://rickandmortyapi.com/api/character"


async def main_request(session: aiohttp.ClientSession, url: str, page: int) -> dict:
    async with session.get(url + f"?page={page}") as response:
        return await response.json()


def get_pages(response: dict) -> str:
    pages = response["info"]["pages"]
    return pages


async def parse_episode(
    session: aiohttp.ClientSession, episode_url: str
) -> Optional[str]:
    async with session.get(episode_url) as response:
        if response.status == 200:
            episode_response_json = await response.json()

            return episode_response_json["name"]

        return None


async def parse_json(session: aiohttp.ClientSession, response: dict) -> dict:
    char_episodes = {}

    for item in response["results"]:
        name = item["name"]
        episode_urls = item["episode"]
        character_episodes = []

        tasks = []
        for episode_url in episode_urls:
            tasks.append(parse_episode(session, episode_url))

        character_episodes = await asyncio.gather(*tasks)
        character_episodes = [episode for episode in character_episodes if episode]

        char_episodes[name] = character_episodes

    return char_episodes


async def main() -> None:
    char_episodes_dict = {}
    async with aiohttp.ClientSession() as session:
        data = await main_request(session, url, 1)

        tasks = []
        for x in range(1, get_pages(data) + 1):
            tasks.append(parse_json(session, await main_request(session, url, x)))

        results = await asyncio.gather(*tasks)

        for x, result in enumerate(results):
            char_episodes_dict[f"page {x+1}"] = result

        with open("character_episodes.json", "w") as json_file:
            json.dump(char_episodes_dict, json_file, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
