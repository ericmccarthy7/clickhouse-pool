from clickhouse_pool.pool import ChPool, ChPoolError, TooManyConnections
import unittest

class TestChPool(unittest.TestCase):
    def test_context(self):
        pool = ChPool()
        with pool.get_client() as client:
            result = client.execute("SELECT * FROM system.numbers LIMIT 5;")
            self.assertEqual(result, [(0,), (1,), (2,), (3,), (4,)])
            self.assertEqual(len(pool._used), 1)
        pool.cleanup()
    def test_connections_min(self):
        pool = ChPool(connections_min=5,connections_max=10)
        clients = []
        for i in range(1, 6):
            clients.append(pool.get_conn())
            self.assertEqual(len(pool._used), i)
        clients.append(pool.get_conn())
        self.assertEqual(len(pool._pool), 0)
        self.assertEqual(len(pool._used), 6)
        for client in clients:
            client.execute("SELECT * FROM system.numbers LIMIT 5;")
            pool.put_conn(conn=client)
        self.assertEqual(len(pool._pool), 5)
        pool.cleanup()
    def test_connections_max(self):
        pool = ChPool(connections_min=1,connections_max=3)
        clients = []
        for i in range(3):
            clients.append(pool.get_conn())
            self.assertEqual(len(pool._used), i+1)
        with self.assertRaises(TooManyConnections):
            clients.append(pool.get_conn())
        for client in clients:
            client.execute("SELECT * FROM system.numbers LIMIT 5;")
            pool.put_conn(conn=client)
        pool.cleanup()

if __name__ == '__main__':
    unittest.main()
