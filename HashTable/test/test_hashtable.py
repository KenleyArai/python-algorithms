from src.hashtable import Hashtable


class TestHashTable:
    def test_put(self):
        ht = Hashtable(15)
        ht[0] = "Panda Bear"

        assert ht._data[0] == "Panda Bear"

    def test_get(self):
        ht = Hashtable(15)
        ht[12] = "Panda Bear"

        assert ht[12] == "Panda Bear"

    def test_len(self):
        ht = Hashtable(15)
        ht[7] = "Holder"
        ht[2] = "Candy Cane"
        ht[12] = "Panda Bear"

        assert len(ht) == 3

    def test_del(self):
        ht = Hashtable(15)
        ht[0] = "Panda Bear"
        del ht[0]
        assert ht._data[0] != "Panda Bear"

    def test_in(self):
        ht = Hashtable(15)
        ht[7] = "Holder"
        ht[2] = "Candy Cane"
        ht[12] = "Panda Bear"

        assert "Panda Bear" in ht
