import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clickhouse-pool",
    version="0.1.0",
    author="Eric McCarthy",
    author_email="ericmccarthy7@gmail.com",
    description="A thread-safe connection pool for ClickHouse.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericmccarthy7/clickhouse-pool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "clickhouse-driver"
    ],
)
