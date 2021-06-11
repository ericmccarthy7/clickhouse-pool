import os

import pytest
from clickhouse_pool.pool import ChPool, TooManyConnections


@pytest.fixture(scope="session")
def clickhouse_host():
    return os.getenv("TEST_CLICKHOUSE_HOST", "localhost")


def test_context(clickhouse_host):
    pool = ChPool(host=clickhouse_host)
    with pool.get_client() as client:
        result = client.execute("SELECT * FROM system.numbers LIMIT 5;")
        assert result == [(0,), (1,), (2,), (3,), (4,)]
        assert len(pool._used) == 1
    assert len(pool._used) == 0
    pool.cleanup()


def test_connections_min(clickhouse_host):
    pool = ChPool(host=clickhouse_host, connections_min=5, connections_max=10)
    clients = []
    for i in range(1, 6):
        clients.append(pool.pull())
        assert len(pool._used) == i
    clients.append(pool.pull())
    assert len(pool._pool) == 0
    assert len(pool._used) == 6
    for client in clients:
        client.execute("SELECT * FROM system.numbers LIMIT 5;")
        pool.push(client=client)
    assert len(pool._pool) == 5
    pool.cleanup()


def test_connections_max(clickhouse_host):
    pool = ChPool(host=clickhouse_host, connections_min=1, connections_max=3)
    clients = []
    for i in range(3):
        clients.append(pool.pull())
        assert len(pool._used) == i + 1
    with pytest.raises(TooManyConnections):
        clients.append(pool.pull())
    for client in clients:
        client.execute("SELECT * FROM system.numbers LIMIT 5;")
        pool.push(client=client)
    pool.cleanup()


def test_connection_released_on_error(clickhouse_host):
    pool = ChPool(host=clickhouse_host)
    try:
        with pool.get_client() as client:
            client.execute("some_invalid_sql")
    except:
        pass
    assert len(pool._used) == 0
    pool.cleanup()
