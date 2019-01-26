from Datastructures import LinkedList


class TestLinkedList:

    def test_init(self):
        ll = LinkedList()

        assert ll.head.val is None
        assert ll.head.next is None

    def test_insert(self):
        ll = LinkedList()

        ll.insert(5)
        ll.insert("a")
        ll.insert(-200)

        ptr = ll.head.next
        assert ptr.val == -200

        ptr = ptr.next
        assert ptr.val == "a"

        ptr = ptr.next
        assert ptr.val == 5

    def test_search(self):

        ll = LinkedList()

        ll.insert(5)
        ll.insert(25)
        ll.insert("k")
        ll.insert(98)
        ll.insert("String")

        test_node = ll.search("k")

        assert test_node.val == "k"

        test_node = ll.search("Not there")

        assert test_node is None

    def test_delete_node(self):

        ll = LinkedList()

        ll.insert(25)
        ll.insert(98)
        ll.insert(105)

        ll.delete_node(25)

        test_node = ll.search(25)

        assert test_node is None
