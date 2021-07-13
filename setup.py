import setuptools

with open("README.md", encoding="utf8") as readme, open(
    "requirements.txt", encoding="utf8"
) as requirements:
    long_description = readme.read()
    requires = requirements.read().splitlines(keepends=False)

setuptools.setup(
    name="python_arq",
    packages=setuptools.find_packages(),
    version="5.4",
    license="MIT",
    description="Asynchronous Python Wrapper For A.R.Q API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="TheHamkerCat",
    author_email="thehamkercat@gmail.com",
    url="https://github.com/thehamkercat/Python_ARQ",
    keywords=["API", "ARQ_API", "Universal API", "Python-ARQ"],
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
