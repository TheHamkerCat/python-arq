from urllib.parse import urlencode

import aiohttp
from dotmap import DotMap


class ARQ:
    """
    Arq class to access all the endpoints of api.

    ...

    Parameters
    ___________
        ARQ_API (``str``):
            Pass ARQ_API_BASE_URL as argument

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

    luna(query="hello luna"):
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

    ocr(url="https://someurl.cum/a.jpg")
        Do OCR on an image.
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
    """

    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url[:-1] if api_url.endswith("/") else api_url
        self.api_key = api_key

    async def _fetch(self, route, params={}):
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

    async def deezer(self, query: str, count: int):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
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
        return await self._fetch("id", {"query": query})

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
        return await self._fetch("ph", {"query": query, "page": page, "thumbsize": thumbsize})

    async def phdl(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): URL To Fetch
                Returns:
                        result object (str): Result
        """
        return await self._fetch("phdl", {"url": url})

    async def luna(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to compute
                Returns:
                        result object (str): Result
        """
        return await self._fetch("luna", {"query": query})

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

    async def ocr(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to perform ocr
                Returns:
                        Result object (str): Results which you can access with dot notation

                        results.ocr
        """
        return await self._fetch("ocr", {"url": url})

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
                        min (min): Minimum limit
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
