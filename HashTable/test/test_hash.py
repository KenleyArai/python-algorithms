from src.hash import Hash


class TestHash:

    def test_hash_diff(self):
        h1 = Hash.hash("123", 256)
        h2 = Hash.hash("456", 256)

        assert h1 != h2

    def test_hash_same(self):
        h1 = Hash.hash("123", 256)
        h2 = Hash.hash("123", 256)

        assert h1 == h2

    def test_encode_string(self):
        assert Hash.encode_string("123") == [ord("1"), ord("2"), ord("3")]
