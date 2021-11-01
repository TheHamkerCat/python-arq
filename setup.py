from setuptools import setup, find_packages


def long_description(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf8") as readme:
            return readme.read()
    else:
        return ""


def requires(file="requirements.txt"):
    if os.path.isfile(file):
        with open(file, encoding="utf8") as requirements:
            return requirements.read().splitlines(keepends=False)
    else:
        return []


setup(
    name="python_arq",
    packages=find_packages(),
    version="6.0.3",
    license="MIT",
    description="Asynchronous Python Wrapper For A.R.Q API.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="TheHamkerCat",
    author_email="thehamkercat@gmail.com",
    url="https://github.com/thehamkercat/Python_ARQ",
    keywords=["API", "ARQ_API", "Python-ARQ", "ARQ", "A.R.Q"],
    install_requires=requires(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
