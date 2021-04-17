from dotmap import DotMap
import aiohttp


# Fetches Json


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
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
        Returns result object with 'limit' number of result which you can use access dot notation.

    torrent(query="tenet"):
        Returns result object which you can use access dot notation.

    saavn(query="attention"):
        Returns result object with 4-5 results which you can access with dot notation.

    youtube(query="carry minati"):
        Returns result object which you can access with dot notation.

    wall(query="cyberpunk"):
        Returns result object which you can access with dot notation.

    reddit(subreddit="linux"):
        Returns result object with 1 result which you can access with dot notation.

    urbandict(query="hoe"):
        Returns result object which you can access with dot notation.

    prunhub(query="step sis in alabama"):
        Returns result object which you can access with dot notation.

    phdl(link="https://pornhubvideolinklol.com"):
        Returns result object with a link which you can access with dot notation

    luna(query="hello luna"):
        Returns result object with a response of lunachatbot which you can access with dot notation.

    drive(query="iron man")
        Returns result object which you can access with dot notation.
    """

    def __init__(self, ARQ_API):
        self.ARQ_API = ARQ_API

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
        data = await fetch(api)
        for i in range(len(data)):
            results[i] = DotMap(data[i])
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
        data = await fetch(api)
        for i in range(len(data)):
            results[i] = DotMap(data[i])
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
        data = await fetch(api)
        for i in range(len(data)):
            results[i] = DotMap(data[i])
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
        data = await fetch(api)
        for i in range(len(data)):
            results[i] = DotMap(data[i])
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
        data = await fetch(api)
        data = data["wallpapers"]
        for i in range(len(data)):
            results[i] = DotMap(data[i])
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
        data = await fetch(api)
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
        data = (await fetch(api))["list"]
        for i in range(len(data)):
            results[i] = DotMap(data[i])
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
        data = await fetch(api)
        for i in range(len(data)):
            results[i] = DotMap(data[i])
        return results

    async def phdl(self, link: str):
        """
        Returns An Object.

                Parameters:
                        link (str): Link To Fetch
                Returns:
                        result object (str): Result which you can access with dot notation, Ex - result.video_url

                        result.requested_url | .video_url
        """
        results = DotMap()
        api = f"{self.ARQ_API}/phdl?query={link}"
        data = await fetch(api)
        results = DotMap(data)
        return results

    async def luna(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to compute
                Returns:
                        result object (str): Result which you can access with dot notation, Ex - result.response

                        result.query | .response
        """
        results = DotMap()
        api = f"{self.ARQ_API}/luna?query={query}"
        data = await fetch(api)
        results = DotMap(data)
        return results


    async def drive(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].url

                        result[result_number].type | .name | .size | .url
        """
        results = DotMap()
        api = f"{self.ARQ_API}/drive?query={query}"
        data = await fetch(api)
        for i in range(len(data)):
            results[i] = DotMap(data[i])
        return results
