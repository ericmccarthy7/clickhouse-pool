# ClickHouse Pool for Python

[![PyPI](https://img.shields.io/pypi/v/clickhouse-pool?style=for-the-badge)](https://pypi.org/project/clickhouse-pool/)
[![PyPI - License](https://img.shields.io/pypi/l/clickhouse-pool?style=for-the-badge)](https://pypi.org/project/clickhouse-pool/)
[![Read the Docs](https://img.shields.io/badge/docs-gh--pages-success?style=for-the-badge)](https://ericmccarthy7.github.io/clickhouse-pool/)

A thread-safe connection pool for ClickHouse. Inspired by `psycopg2` and using
[`clickhouse-driver`](https://github.com/mymarilyn/clickhouse-driver) for
connections.

## Installation

```sh
pip install clickhouse-pool
```

## Quick Start

```python
from clickhouse_pool import ChPool

# find available settings at https://clickhouse-driver.readthedocs.io/en/latest/api.html#clickhouse_driver.Client
pool = ChPool(host="localhost")

with pool.get_client() as client:
    # execute sql and print the result
    result = client.execute("SELECT * FROM system.numbers LIMIT 5")
    print(result)

# always close all connections in the pool once you're done with it
pool.cleanup()
```

## Connection Pool Size

To change the connection pool size,

```python
pool = ChPool(connections_min=20, connections_max=40)

with pool.get_client() as client:
    result = client.execute("SELECT * FROM system.numbers LIMIT 5")
    print(result)

# always close all connections in the pool once you're done with it
pool.cleanup()
```

## Testing Locally

To run tests locally ensure you have an instance of clickhouse-server running on
localhost. The easiest way is to use docker:

```sh
docker run -d -p 9000:9000 yandex/clickhouse-server
poetry run pytest
```

## Building Docs

```sh
poetry run sphinx-build -M html docs/source docs/_build
```
