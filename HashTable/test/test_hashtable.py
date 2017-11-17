from src.hashtable import Hashtable


class TestHashTable:
    def test_put(self):
        ht = Hashtable(15)
        ht["a"] = "Panda Bear"

        hash_value = ord("a") % 15

        assert ht._data[hash_value] == "Panda Bear"

    def test_get(self):
        ht = Hashtable(15)
        ht["Cake"] = "Panda Bear"

        assert ht["Cake"] == "Panda Bear"

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
