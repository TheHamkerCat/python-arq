# Python_ARQ

Asyncronous Python Wrapper For A.R.Q API.

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![Github](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/)


## Requirements

- Python 3.8 or higher.
- ARQ_API url, Get it from [here](https://t.me/patheticprogrammers)

## Installation

- `pip3 install -U python-arq`

## Usage

For Example, to get a song link from deezer, you can do this

<h3>
    
```python
​
from Python_ARQ import ARQ

arq = ARQ(Api_Url)

song = await arq.deezer(query="Never gonna give you up", limit=1)

song_link = song[0].url

print(song_link)

>> Output:
https://e-cdns-proxy-3.dzcdn.net/api/1/f1fb0b260a55f594c20d4592c752708460c4864fb97de0be8b459c3b63ff69817d97eddffd60bfbf9f6de5a89d0dbf8864c3f107173b1bfa601b4442aee694e4e67427534a7c8b1a145d2a931fd3429e
​
```
</h3>

The link above is a direct link to that song.


## Documentation

There is no documentation as of now, however, you can take help from the docstrings this way.

<h3>
    
```python
​
from Python_ARQ import ARQ

print(help(ARQ.deezer))
​
```
</h3>

## Features as of now [List of APIs]

1. Deezer
2. Jiosaavn
3. Youtube
4. PronHub
5. Reddit
6. Urban Dictionary
7. Torrent
8. Wallpapers
9. AI Chatbot

## Note
1. I'll add more features soon.
2. If you're stucked somewhere, [Pathetic Programmers](https://t.me/PatheticProgrammers) are there to help.
