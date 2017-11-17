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
        ht["Pie"] = "Holder"
        ht["Xmas"] = "Candy Cane"
        ht["Kenley"] = "Panda Bear"

        assert len(ht) == 15

    def test_del(self):
        ht = Hashtable(15)
        ht["a"] = "Panda Bear"
        del ht["a"]
        assert ht["a"] != "Panda Bear"

    def test_in(self):
        ht = Hashtable(15)
        ht["Pie"] = "Holder"
        ht["Xmas"] = "Candy Cane"
        ht["Kenley"] = "Panda Bear"

        assert "Panda Bear" in ht
