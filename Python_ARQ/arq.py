from base64 import b64decode
from json import dumps
from re import match, sub

import aiofiles
from aiohttp import ClientSession
from dotmap import DotMap
from pyrogram.types import Message, User


# https://stackoverflow.com/a/55766564/13673785
def _format_url(url):
    if not match("(?:http|https)://", url):
        return "https://{}".format(url)
    return url


def _get_name(from_user: User) -> str:
    return f"{from_user.first_name} {from_user.last_name or ''}".rstrip()


class InvalidApiKey(Exception):
    pass


class GenericApiError(Exception):
    pass


class Arq:
    """
    Arq class to access all the endpoints of api.


    Parameters
    ___________

        ARQ(API_URL: str, API_KEY: str, AioHTTPSession)

    """

    def __init__(
        self, api_url: str, api_key: str, aiohttp_session: ClientSession
    ):
        self.api_url = _format_url(api_url.strip(" /"))
        self.api_key = api_key
        self.session = aiohttp_session

    async def _fetch(self, route, **params):
        async with self.session.get(
            f"{self.api_url}/{route}",
            headers={"X-API-KEY": self.api_key},
            params=params,
        ) as resp:
            if resp.status in (401, 403):
                raise InvalidApiKey(
                    "Invalid API key, Get an api key from @ARQRobot"
                )
            response = await resp.json()
        return DotMap(response)

    async def _post(self, route, params):
        async with self.session.post(
            f"{self.api_url}/{route}",
            headers={"X-API-KEY": self.api_key},
            params=params,
        ) as resp:
            if resp.status in (401, 403):
                raise InvalidApiKey(
                    "Invalid API key, Get an api key from @ARQRobot"
                )
            response = await resp.json()
        return DotMap(response)

    async def _post_data(self, route, data, header=None):
        headers = {"X-API-KEY": self.api_key}
        if header:
            for key, value in header.items():
                headers[key] = value
        async with self.session.post(
            f"{self.api_url}/{route}",
            headers=headers,
            data=data,
        ) as resp:
            if resp.status in (401, 403):
                raise InvalidApiKey(
                    "Invalid API key, Get an api key from @ARQRobot"
                )
            response = await resp.json()
        return DotMap(response)

    async def deezer(self, query: str, count: int = 1, format: int = 3):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        count (int): Number of results to return
                        format (int): Quality [Bitrate] of songs.
                                      Available formats:  1 - MP3 128kbit,
                                                          3 - MP3 320kbit,
                                                          9 - Lossless(FLAC),
                                      Defaults to 3, MP3 320Kbps.
                Returns:
                        results: Results which you can access with dot notation, Ex - results[result_number].url

                        result[result_number].title | .id | .source | .duration | .thumbnail | .thumbnailBig |.artist
                            .artistPictures | .url

        """
        return await self._fetch(
            "deezer", query=query, count=count, format=format
        )

    async def torrent(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].magnet

                        result[result_number].name | .uploaded | .size | .seeds | .leechs | .magnet
        """
        return await self._fetch("torrent", query=query)

    async def saavn(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        result object (str): Results which you can access with dot notation, Ex - results[result_number].title

                        result[result_number].song | .album | .year | .singers | .image | .duration | .media_url
        """
        return await self._fetch("saavn", query=query)

    async def splaylist(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): Saavn playlist url
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("splaylist", url=url)

    async def youtube(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].thumbnails

                        result[result_number].id | .thumbnails | .title | .long_desc | .channel | .duration | .views | .publish_time | .url_suffix
        """
        return await self._fetch("youtube", query=query)

    async def ytdl(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): Youtube video url
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].thumbnails

                        result[result_number].id | .thumbnail | .title | .video
        """
        return await self._fetch("ytdl", url=url)

    async def wall(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].url_image

                        result[result_number].id | .width | .height | .file_type | .file_size | .url_image | .url_thumb | .url_page
        """
        return await self._fetch("wall", query=query)

    async def reddit(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Subreddit to search
                Returns:
                        result object (str): Result which you can access with dot notation, Ex - result.postLink

                        result.postLink | .subreddit | .title | .url | .nsfw | .spoiler | .author | .ups | .preview
        """
        return await self._fetch("reddit", query=query)

    async def urbandict(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].example

                        result[result_number].definition | .permalink | .thumbs_up | .sound_urls | .author | .word | .defid | .example | .thumbs_down
        """
        return await self._fetch("ud", query=query)

    async def pornhub(
        self, query: str = "", page: int = 1, thumbsize: str = "small"
    ):
        """
        Returns An Object.

                Parameters:

                        - query: Search query, optional, defaults to "" [OPTIONAL]
                        - page: Page number, optional, defaults to 1 [OPTIONAL]
                        - thumbsize: Size of the thumbnail, optional,
                          defaults to "small", possible values are small, medium, large, small_hd, medium_hd, large_hd [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].title

                        result[result_number].id | .title | .duration | .views | .rating | .url | .category | .thumbnails
        """
        return await self._fetch(
            "ph",
            query=query,
            page=page,
            thumbsize=thumbsize,
        )

    async def phdl(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): URL To Fetch
                Returns:
                        result object (str): Result
        """
        return await self._fetch("phdl", url=url)

    async def luna(self, query: str, id: int = 0):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to compute
                        id (int): Unique user_id. [OPTIONAL]
                Returns:
                        result object (str): Result
        """
        return await self._fetch("luna", query=query, id=id)

    async def lyrics(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.lyrics

                        results.lyrics
        """
        return await self._fetch("lyrics", query=query)

    async def wiki(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.title

                        results.title | .answer
        """
        return await self._fetch("wiki", query=query)

    async def nlp(self, messages: list):
        if not isinstance(messages, list):
            messages = [messages]
        """
        Returns An Object.
                Parameters:
                        text (str): Text to process.
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.data

                        results.prediction | .spam | .ham
        """
        data = dumps({"messages": messages})
        return await self._post_data("nlp", data, {"Content-Type": "application/json"})

    async def nsfw_scan(self, url: str = None, file: str = None):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to scan (Optional)
                        file (str): File path of an image to scan. (Optional)
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.data

                        results.data | results.data.drawings | results.data.hentai | .neutral | .sexy | .porn | .is_nsfw
        """
        if not file and not url:
            raise Exception("PROVIDE FILE OR URL")
        if not file:
            return await self._fetch("nsfw_scan", url=url)
        async with aiofiles.open(file, mode="rb") as f:
            file = await f.read()
        return await self._post_data("nsfw_scan", data={"file": file})

    async def stats(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.uptime

                        results.uptime | .requests | .cpu | .memory.server | .memory.api | .disk | .platform | .python
        """
        return await self._fetch("stats")

    async def proxy(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results.uptime

                        results.location | .proxy
        """
        return await self._fetch("proxy")

    async def tmdb(self, query: str = "", tmdbID: int = 0):
        """
        Returns An Object.

                Parameters:
                        query (str): Name of series/movie [OPTIONAL]
                        tmdbID (int): TMDB ID of series/movie [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

                        results.id | .title | .overview | .rating | .releaseDate | .genre | .backdrop | .poster
        """
        return await self._fetch("tmdb", query=query, tmdbID=tmdbID)

    async def quotly(self, messages: [Message]):
        """
        Returns An Object.

                Parameters:
                        messages ([Message]): Generate quotly stickers.
                Returns:
                        Result object (str): Results which you can access with dot notation

                        results
        """
        if not isinstance(messages, list):
            messages = [messages]

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
                        "name": _get_name(message.from_user),
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
                        "name": _get_name(message.forward_from),
                    },
                    "text": message.text if message.text else "",
                    "replyMessage": (
                        {
                            "name": _get_name(
                                message.reply_to_message.from_user
                            ),
                            "text": message.reply_to_message.text,
                            "chatId": message.reply_to_message.from_user.id,
                        }
                        if message.reply_to_message
                        else {}
                    )
                    if len(messages) == 1
                    else {},
                }
                for message in messages
            ],
        }
        response = await self._post("quotly", params={"payload": str(payload)})
        if response.ok:
            response.result = b64decode(
                sub("data:image/png;base64", "", response.result)
            )
        return response

    async def translate(self, text: str, destLangCode: str = "en"):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to translate
                        destLangCode (str): Language code of destination language. [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].thumbnails

                        result[result_number].text | .src | .dest
        """
        return await self._fetch(
            "translate", text=text, destLangCode=destLangCode
        )

    async def pypi(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Exact package name.
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].thumbnails

                        result[result_number].name | .version | .license | .description | .size | .author | .authorEmail |  .homepage
                            .keywords | .requirements | .minPyVersion | .bugTrackURL | .docsURl | .pypiURL | .releaseURl | .projectURLS
        """
        return await self._fetch("pypi", query=query)

    async def image(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Search query.
                Returns:
                        Result object (str): Results which you can access with dot notation, Ex - results[result_number].thumbnails

                        result[result_number].title | .url
        """
        return await self._fetch("image", query=query)

    async def spellcheck(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Some text
                Returns:
                        result object (str): Results which you can access with dot notation, Ex - result.correct

                        result.corrected | .corrections (dict)
        """
        return await self._fetch("spellcheck", text=text)


# Backwards compatibility
ARQ = Arq
