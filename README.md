# Python_ARQ

Python wrapper for the A.R.Q. API.

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![GitHub](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/)

## Requirements

- Python 3.8 or newer.
- API URL and KEY, from [here](https://t.me/PatheticProgrammers).

## Installation

```sh
$ pip install python-arq
```

## Usage

For Example, to get a song link from deezer, you can do this

```py
import asyncio
from Python_ARQ import ARQ

arq = ARQ(api_url, api_key)

async def func(query: str):
 song = await arq.deezer(query, 1)
 return song[0].url

async def main():
 output = await func("Never gonna give you up")
 print(output)

asyncio.run(main())
```

## Documentation

There is no documentation as of now, however, you can take help from the docstrings this way:

```py
from Python_ARQ import ARQ

print(help(ARQ.deezer))
```

## Features as of now [List of APIs]

1. Deezer
2. Jiosaavn
3. Youtube
4. PronHub
5. Reddit
6. Torrent
7. Wallpapers
8. Urban Dictionary
9. Luna AI Chatbot
10. Lyrics
11. Wikipedia
12. NSFW Image Classification
13. Optical Character Recognition (OCR)
14. Generate "Truly" Random Numbers Using Atmospheric Noise
15. Proxy Scraper
16. The Movie Database [TMDB]
17. Quotly [TELEGRAM]

## Note

1. I'll add more features soon.
2. If you're stucked somewhere, [Pathetic Programmers](https://t.me/PatheticProgrammers) are there to help.
