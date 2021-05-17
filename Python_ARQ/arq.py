from base64 import b64decode
from html import escape
from re import sub
from urllib.parse import urlencode

import aiohttp
from dotmap import DotMap
from pyrogram.types import Message


class ARQ:
    """
    Arq class to access all the endpoints of api.

    ...

    Parameters
    ___________
        ARQ_API (URL: str, API_KEY: str):
            Pass ARQ_API_BASE_URL and ARQ_API_KEY as argument

    Methods
    -------
    deezer(query="never gonna give you up", limit=1):
        Get songs from deezer.
            Returns result object with 'limit' number of result which you can use access dot notation.

    torrent(query="tenet"):
        Search for torrent across many websites.
            Returns result object which you can use access dot notation.

    saavn(query="attention"):
        Get songs from Saavn.
            Returns result object with 4-5 results which you can access with dot notation.

    youtube(query="carry minati"):
        Search on youtube.
            Returns result object which you can access with dot notation.

    wall(query="cyberpunk"):
        Returns result object which you can access with dot notation.

    reddit(subreddit="linux"):
        Search wallpapers.
            Returns result object with 1 result which you can access with dot notation.

    urbandict(query="hoe"):
        Search for a word on urban dictionary.
            Returns result object which you can access with dot notation.

    pornhub(query="step sis in alabama"):
        Search pornhub videos.
            Returns result object which you can access with dot notation.

    phdl(link="https://pornhubvideolinklol.com"):
        Download a prunhub video.
            Returns result object with a link which you can access with dot notation

    luna(query="hello luna", id=user_id):
        Communicate with an AI chatbot.
            Returns result object which you can access with dot notation.

    lyrics(query="So Far Away Martin Garrix")
        Search for song lyrics.
            Returns result object which you can access with dot notation.

    wiki(query="dog")
        Search for something on wikipedia.
            Returns result object which you can access with dot notation.

    nsfw_scan(url="https://someurl.cum/a.jpg")
        Scan and classify an image.
            Returns result object which you can access with dot notation.

    stats()
        Get statistics of ARQ server.
            Returns result object which you can access with dot notation.

    random(min=0, max=1000)
        Generate a true random number using atmospheric noise.
            Returns result object which you can access with dot notation.

    proxy()
        Generate a proxy, sock5.
            Returns result object which you can access with dot notation.

    tmdb(query: str = "")
        Search Something on TMDB
            Returns result object which you can access with dot notation.

    quotly(messages: [Message])
        Generate stickers from telegram message.
            Returns base64 of the image sticker.
    """

    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url[:-1] if api_url.endswith("/") else api_url
        self.api_key = api_key

    async def _fetch(self, route, params={}):
        if params:
            for param in params:
                params[param] = escape(str(params[param]))

        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.api_url}/{route}?{urlencode(params)}",
                headers={"X-API-KEY": self.api_key},
            ) as resp:
                if resp.status in (
                    401,
                    403,
                ):
                    raise Exception("Invalid API key")
                response = await resp.json()
        ok, result = response
        if ok:
            return DotMap(response)
        raise Exception(result)

    async def _post(self, route, payload={}):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.api_url}/{route}",
                headers={"X-API-KEY": self.api_key},
                params={"payload": str(payload)},
            ) as resp:
                if resp.status in (
                    401,
                    403,
                ):
                    raise Exception("Invalid API key")
                response = await resp.json()
        ok, result = response
        if ok:
            response["result"] = b64decode(
                sub("data:image/png;base64", "", response["result"])
            )
            return DotMap(response)
        raise Exception(result)

    async def deezer(self, query: str, count: int):
        """
        Returns An Object.

                Parameters:
                        query (int): Query to search
                        count (int): Number of results to return
                Returns:
                        result object (str): Results which you can access with dot notation, Ex - results[result_number].url

                        result[result_number].title | .id | .source | .duration | .thumbnail | .artist | .url

        """
        return await self._fetch("deezer", {"query": query, "count": count})

    async def torrent(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].magnet

                        result[result_number].name | .uploaded | .size | .seeds | .leechs | .magnet
        """
        return await self._fetch("torrent", {"query": query})

    async def saavn(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        result object (str): Results which you can access with dot notation, Ex - results[result_number].title

                        result[result_number].song | .album | .year | .singers | .image | .duration | .media_url
        """
        return await self._fetch("saavn", {"query": query})

    async def youtube(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Number of results to return
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].thumbnails

                        result[result_number].id | .thumbnails | .title | .long_desc | .channel | .duration | .views | .publish_time | .url_suffix
        """
        return await self._fetch("youtube", {"query": query})

    async def wall(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].url_image

                        result[result_number].id | .width | .height | .file_type | .file_size | .url_image | .url_thumb | .url_page
        """
        return await self._fetch("wall", {"query": query})

    async def reddit(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Subreddit to search
                Returns:
                        result object (str): Result which you can access with dot notation, Ex - result.postLink

                        result.postLink | .subreddit | .title | .url | .nsfw | .spoiler | .author | .ups | .preview
        """
        return await self._fetch("reddit", {"query": query})

    async def urbandict(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].example

                        result[result_number].definition | .permalink | .thumbs_up | .sound_urls | .author | .word | .defid | .example | .thumbs_down
        """
        return await self._fetch("ud", {"query": query})

    async def pornhub(self, query: str = "", page: int = 1, thumbsize: str = "small"):
        """
        Returns An Object.

                Parameters:

                        - query: Search query, optional, defaults to ""
                        - page: Page number, optional, defaults to 1
                        - thumbsize: Size of the thumbnail, optional,
                          defaults to "small", possible values are small, medium, large, small_hd, medium_hd, large_hd
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].title

                        result[result_number].id | .title | .duration | .views | .rating | .url | .category | .thumbnails
        """
        return await self._fetch(
            "ph",
            {
                "query": query,
                "page": page,
                "thumbsize": thumbsize,
            },
        )

    async def phdl(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): URL To Fetch
                Returns:
                        result object (str): Result
        """
        return await self._fetch("phdl", {"url": url})

    async def luna(self, query: str, id: int = 0):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to compute
                        id (int): Unique user_id.
                Returns:
                        result object (str): Result
        """
        return await self._fetch("luna", {"query": query, "id": id})

    async def lyrics(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.lyrics

                        results.lyrics
        """
        return await self._fetch("lyrics", {"query": query})

    async def wiki(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.title

                        results.title | .answer
        """
        return await self._fetch("wiki", {"query": query})

    async def nsfw_scan(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to scan
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.data

                        results.data | results.data.drawings | results.data.hentai | .neutral | .sexy | .porn | .is_nsfw
        """
        return await self._fetch("nsfw_scan", {"url": url})

    async def stats(self):
        """
        Returns An Object.

                Parameters:
                        None
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.uptime

                        results.uptime | .requests | .cpu | .memory.server | .memory.api | .disk | .platform | .python
        """
        return await self._fetch("stats")

    async def random(self, min: int, max: int):
        """
        Returns An Object.

                Parameters:
                        min (int): Minimum limit
                        max (int): Maximum limit
                Returns:
                        Result object (str): Result
        """
        return await self._fetch("random", {"min": min, "max": max})

    async def proxy(self):
        """
        Returns An Object.

                Parameters:
                        None
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.uptime

                        results.location | .proxy
        """
        return await self._fetch("proxy")

    async def tmdb(self, query: str = ""):
        """
        Returns An Object.

                Parameters:
                        query (str): Search something on TMDB
                Returns:
                        Result object (str): Results which you can access with dot notation

                        results.id | .title | .overview | .rating | .releaseDate | .genre | .backdrop | .poster
        """
        return await self._fetch("tmdb", {"query": query})

    async def quotly(self, messages: [Message]):
        """
        Returns An Object.

                Parameters:
                        messages ([Message]): Generate quotly stickers.
                Returns:
                        Result object (str): Results which you can access with dot notation

                        results
        """
        def getName(from_user):
            first_name = from_user.first_name
            last_name = from_user.last_name if from_user.last_name else ""
            name = first_name + last_name
            return name

        payload = {
            "type": "quote",
            "format": "png",
            "backgroundColor": "#1b1429",
            "messages": [
                {
                    "entities": [
                        {
                            "type": entity.type,
                            "offset": entity.offset,
                            "length": entity.length,
                        }
                        for entity in message.entities
                    ]
                    if message.entities
                    else [],
                    "chatId": message.forward_from.id
                    if message.forward_from
                    else message.from_user.id,
                    "avatar": True,
                    "from": {
                        "id": message.from_user.id,
                        "username": message.from_user.username
                        if message.from_user.username
                        else "",
                        "photo": {
                            "small_file_id": message.from_user.photo.small_file_id,
                            "small_photo_unique_id": message.from_user.photo.small_photo_unique_id,
                            "big_file_id": message.from_user.photo.big_file_id,
                            "big_photo_unique_id": message.from_user.photo.big_photo_unique_id,
                        }
                        if message.from_user.photo
                        else "",
                        "type": message.chat.type,
                        "name": getName(message.from_user),
                    }
                    if not message.forward_from
                    else {
                        "id": message.forward_from.id,
                        "username": message.forward_from.username
                        if message.forward_from.username
                        else "",
                        "photo": {
                            "small_file_id": message.forward_from.photo.small_file_id,
                            "small_photo_unique_id": message.forward_from.photo.small_photo_unique_id,
                            "big_file_id": message.forward_from.photo.big_file_id,
                            "big_photo_unique_id": message.forward_from.photo.big_photo_unique_id,
                        }
                        if message.forward_from.photo
                        else "",
                        "type": message.chat.type,
                        "name": getName(message.forward_from),
                    },
                    "text": message.text if message.text else "",
                    "replyMessage": ({
                        "name": getName(message.reply_to_message.from_user),
                        "text": message.reply_to_message.text,
                        "chatId": message.reply_to_message.from_user.id
                        } if message.reply_to_message else {}) if len(messages) == 1 else {},
                }
                for message in messages
            ],
        }

        return await self._post("quotly", payload)
