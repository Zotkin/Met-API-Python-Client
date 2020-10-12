import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="met_api", # Replace with your own username
    version="0.0.1",
    author="Yevhenii Zotkin",
    author_email="yevhenii.zotkin@protonmail.com",
    description="An unofficial async MET API client.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zotkin/met_api_async_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU v3",
        "Operating System :: Linux",
    ],
    python_requires='>=3.8',
)