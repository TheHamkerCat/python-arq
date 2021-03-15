from functions import fetch
from config import ARQ_API
from dotmap import DotMap
import asyncio


class arq:
    
    """
    Arq class to access all the endpoints of api.

    ...

    Methods
    -------
    deezer(query="never gonna give you up", limit=1):
        Returns result object with 'limit' number of result which you can use access dot notation.
    
    torrent(query="tenet", limit=1):
        Returns result object with 'limit' number of result which you can use access dot notation.

    saavn(query="attention"):
        Returns result object with 4-5 results which you can access with dot notation.
    
    youtube(query="carry minati", limit=1):
        Returns result object with 'limit' number of result which you can access with dot notation.
    
    wall(query="cyberpunk", limit=1):
        Returns result object with 'limit' number of result which you can access with dot notation.
    
    reddit(subreddit="linux"):
        Returns result object with 1 result which you can access with dot notation.
    
    urbandict(query="hoe", limit=1):
        Returns result object with 'limit' number of result which you can access with dot notation.
    
    prunhub(query="step sis in alabama", limit=1):
        Returns result object with 'limit' number of result which you can access with dot notation.
    
    phdl(link="https://pornhubvideolinklol.com"):
        Returns result object with a link which you can access with dot notation

    luna(query="hello luna"):
        Returns result object with a response of lunachatbot which you can access with dot notation.

    """

    async def deezer(self, query: str, limit: int):

        '''
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Number of results to return
                Returns:
                        result object (str): Results which you can access with dot notation, Ex - results[result_number].url
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/deezer?query={query}&count={limit}"
        data = await fetch(api)
        
        for i in range(len(data)):
            results[i] = DotMap(data[i])
        
        return results


    async def torrent(self, query: str, limit: int):

        '''
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Number of results to return
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].magnet
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/torrent?query={query}"
        data = await fetch(api)
        
        for i in range(limit):
            results[i] = DotMap(data[i])
        
        return results


    async def saavn(self, query: str):

        '''
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        result object (str): Results which you can access with dot notation, Ex - results[result_number].title
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/saavn?query={query}"
        data = await fetch(api)
        
        for i in range(len(data)):
            results[i] = DotMap(data[i])
        
        return results


    async def youtube(self, query: str, limit: str):

        '''
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Number of results to return
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].thumbnails
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/youtube?query={query}&count={limit}"
        data = await fetch(api)
        
        for i in range(len(data)):
            results[i] = DotMap(data[i])
        
        return results


    async def wall(self, query: str, limit: int):

        '''
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Number of results to return
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].url_image
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/wall?query={query}"
        data = await fetch(api)
        
        for i in range(limit):
            results[i] = DotMap(data['wallpapers'][i])
        
        return results


    async def reddit(self, subreddit: str):

        '''
        Returns An Object.

                Parameters:
                        subreddit (str): Subreddit to search
                Returns:
                        result object (str): Result which you can access with dot notation, Ex - result.postLink
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/reddit?query={subreddit}"
        data = await fetch(api)
        results = DotMap(data)
        
        return results


    async def urbandict(self, query: str, limit: int):

        '''
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Number of results to return
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].example
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/ud?query={query}"
        data = await fetch(api)
        
        for i in range(limit):
            results[i] = DotMap(data['list'][i])
        
        return results


    async def prunhub(self, query: str, limit: int):

        '''
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Number of results to return
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].title
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/ph?query={query}"
        data = await fetch(api)
        
        for i in range(limit):
            results[i] = DotMap(data[i])
        
        return results


    async def phdl(self, link: str):

        '''
        Returns An Object.

                Parameters:
                        link (str): Link To Fetch
                Returns:
                        result object (str): Result which you can access with dot notation, Ex - result.video_url
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/phdl?query={link}"
        data = await fetch(api)
        results = DotMap(data)
        
        return results


    async def luna(self, query: str):

        '''
        Returns An Object.

                Parameters:
                        query (str): Query to compute
                Returns:
                        result object (str): Result which you can access with dot notation, Ex - result.response
        '''

        results = DotMap()
        
        api = f"{ARQ_API}/luna?query={query}"
        data = await fetch(api)
        results = DotMap(data)
        
        return results


arq = arq()

async def hoe():
    songs = await arq.deezer("attention", 2)
    torrents = await arq.torrent("porn", 2)
    song = await arq.saavn("attention")
    print(song[0].media_url)
    print(songs[0].url)
    print(songs[1].url)
    print(torrents[0].magnet)
asyncio.run(hoe())


        
