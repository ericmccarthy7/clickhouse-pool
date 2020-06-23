# ClickHouse Pool for Python

A thread-safe connection pool for ClickHouse. Inspired by `psycopg2` and using
[`clickhouse-driver`](https://github.com/mymarilyn/clickhouse-driver) for
connections.

## Installation

`pip install clickhouse-pool`

## Quick Start

```python
from clickhouse_pool.pool import ChPool

# create a pool
pool = ChPool(host='localhost')

# get a conn (clickhouse-driver client)
conn = pool.get_conn()

# execute sql and print the result
result = conn.execute("SELECT * FROM system.numbers LIMIT 5")
print(result)

# always put the connection back in the pool once you're done
pool.put_conn(conn=conn)
```
