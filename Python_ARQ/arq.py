import aiohttp
from dotmap import DotMap

# Fetches Json


async def fetch(url: str, api_key: str):
    headers = {"X-API-KEY": api_key}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            data = await resp.json()
            if "detail" in data.keys():
                raise Exception(data['detail'])
                return
    return data


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

    prunhub(query="step sis in alabama"):
        Search for a prunhub video.
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

    def __init__(self, ARQ_API, API_KEY):
        self.ARQ_API = ARQ_API
        self.API_KEY = API_KEY

    async def deezer(self, query: str, limit: int):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Number of results to return
                Returns:
                        result object (str): Results which you can access with dot notation, Ex - results[result_number].url

                        result[result_number].title | .id | .source | .duration | .thumbnail | .artist | .url

        """
        results = DotMap()
        api = f"{self.ARQ_API}/deezer?query={query}&count={limit}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def torrent(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].magnet

                        result[result_number].name | .uploaded | .size | .seeds | .leechs | .magnet
        """
        results = DotMap()
        api = f"{self.ARQ_API}/torrent?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def saavn(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        result object (str): Results which you can access with dot notation, Ex - results[result_number].title

                        result[result_number].song | .album | .year | .singers | .image | .duration | .media_url
        """
        results = DotMap()
        api = f"{self.ARQ_API}/saavn?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

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
        results = DotMap()
        api = f"{self.ARQ_API}/youtube?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def wall(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].url_image

                        result[result_number].id | .width | .height | .file_type | .file_size | .url_image | .url_thumb | .url_page
        """
        results = DotMap()
        api = f"{self.ARQ_API}/wall?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def reddit(self, subreddit: str):
        """
        Returns An Object.

                Parameters:
                        subreddit (str): Subreddit to search
                Returns:
                        result object (str): Result which you can access with dot notation, Ex - result.postLink

                        result.postLink | .subreddit | .title | .url | .nsfw | .spoiler | .author | .ups | .preview
        """
        results = DotMap()
        api = f"{self.ARQ_API}/reddit?query={subreddit}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def urbandict(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].example

                        result[result_number].definition | .permalink | .thumbs_up | .sound_urls | .author | .word | .defid | .example | .thumbs_down
        """
        results = DotMap()
        api = f"{self.ARQ_API}/ud?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def prunhub(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].title

                        result[result_number].id | .title | .duration | .views | .rating | .url | .category | .thumbnails
        """
        results = DotMap()
        api = f"{self.ARQ_API}/ph?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def phdl(self, link: str):
        """
        Returns An Object.

                Parameters:
                        link (str): Link To Fetch
                Returns:
                        result object (str): Result
        """
        results = DotMap()
        api = f"{self.ARQ_API}/phdl?url={link}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def luna(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to compute
                Returns:
                        result object (str): Result
        """
        results = DotMap()
        api = f"{self.ARQ_API}/luna?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def lyrics(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.lyrics

                        results.lyrics
        """
        results = DotMap()
        api = f"{self.ARQ_API}/lyrics?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def wiki(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.title

                        results.title | .answer
        """
        results = DotMap()
        api = f"{self.ARQ_API}/wiki?query={query}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def nsfw_scan(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to scan
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.data

                        results.data | results.data.drawings | results.data.hentai | .neutral | .sexy | .porn | .is_nsfw
        """
        results = DotMap()
        api = f"{self.ARQ_API}/nsfw_scan?url={url}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def ocr(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to perform ocr
                Returns:
                        Result object (str): Results which you can access with dot notation

                        results.ocr
        """
        results = DotMap()
        api = f"{self.ARQ_API}/ocr?url={url}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def stats(self):
        """
        Returns An Object.

                Parameters:
                        None
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.uptime

                        results.uptime | .requests | .cpu | .memory.server | .memory.api | .disk | .platform | .python
        """
        results = DotMap()
        api = f"{self.ARQ_API}/stats"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def random(self, min: int, max: int):
        """
        Returns An Object.

                Parameters:
                        min (min): Minimum limit
                        max (int): Maximum limit
                Returns:
                        Result object (str): Result
        """
        results = DotMap()
        api = f"{self.ARQ_API}/random?min={min}&max={max}"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results

    async def proxy(self):
        """
        Returns An Object.

                Parameters:
                        None
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.uptime

                        results.location | .proxy
        """
        results = DotMap()
        api = f"{self.ARQ_API}/proxy"
        data = await fetch(api, self.API_KEY)
        results = DotMap(data)
        return results
