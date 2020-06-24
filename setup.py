import codecs
import os.path
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

name = "clickhouse-pool"
version = get_version("clickhouse_pool/__init__.py")

setuptools.setup(
    name=name,
    version=version,
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
