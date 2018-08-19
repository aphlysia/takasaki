import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="takasaki",
    version="0.0.1",
    author="Kenji Aoki",
    author_email="aokikenjinn@gmail.com",
    description="An viewer of machine learning experiments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aphlysia/takasaki",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
