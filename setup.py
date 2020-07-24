import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tempfileatexit",
    version="0.0.2",
    author="Jachym Cepicky",
    author_email="jachym@cepicky.ch",
    description="Remove tempory files at program exit, combination of tempfile and atexit should be as simple as possible.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jachym/tempfileatexit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)

