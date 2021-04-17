from setuptools import setup
import requests

readme = requests.get("https://raw.githubusercontent.com/thehamkercat/Python_ARQ/master/README.md").text

requirements = requests.get("https://raw.githubusercontent.com/thehamkercat/Python_ARQ/master/requirements.txt").text

requires = requirements.splitlines()

setup(
  name = 'Python_ARQ',
  packages = ['Python_ARQ'],
  version = '1.7', 
  license='MIT',  
  description = 'Asynchronous Python Wrapper For A.R.Q API. ',
  long_description=readme,
  long_description_content_type="text/markdown",
  author = 'TheHamkerCat',
  author_email = 'thehamkercat@gmail.com',
  url = 'https://github.com/thehamkercat/Python_ARQ',
  download_url = '',
  keywords = ['API', 'ARQ_API', 'Universal API'],
  install_requires=requires,
  classifiers=[
    'Development Status :: 5 - Production/Stable', 
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
