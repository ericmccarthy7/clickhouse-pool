Introduction
============

A thread-safe connection pool for ClickHouse. Inspired by `psycopg2` and using
`clickhouse-driver` for connections.

Requirements
------------

`clickhouse-pool` works with Windows and Unix based systems. The package
requires Python 3.8 and above due to typing.

Installation
------------

You can install `clickhouse-pool` with from PyPi with `pip` or your favorite package manager::

    pip install clickhouse-pool

Add the ``-U`` switch to update to the current version, if `clickhouse-pool` is already installed.

Quick Start
-----------

Simple initializing a pool and running a query::

    from clickhouse_pool import ChPool

    pool = ChPool()

    with pool.get_client() as client:
        # execute sql and print the result
        result = client.execute("SELECT * FROM system.numbers LIMIT 5")
        print(result)

    # always close all connections in the pool once you're done with it
    pool.cleanup()
