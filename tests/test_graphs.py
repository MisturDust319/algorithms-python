import unittest

import graphs.union_find

class TestUnionFind(unittest.TestCase):
    def setUp(self):
        """
        Set up a fresh disjoint set for each test
        :return:
        """
        self.disjoint_set = graphs.union_find.DisjointSet()

    def tearDown(self):
        """
        Delete the disjoint set so that changes to it aren't carried between tests
        :return:
        """
        del self.disjoint_set
        self.disjoint_set = None

    def test_find(self):
        """
        test the find function
        the find function takes a numeric id for a node and returns the Node object that is the id
        """
        for i in range(4):
            self.disjoint_set.add(i)

        # manually set the parents of the parents of the nodes
        self.disjoint_set.tree[0].parent = self.disjoint_set.tree[1]
        self.disjoint_set.tree[1].parent = self.disjoint_set.tree[2]
        self.disjoint_set.tree[2].parent = self.disjoint_set.tree[3]

        search_result = self.disjoint_set.find(0)

        self.assertEqual(search_result.id, 3)

        # test the test side effects

        # if the find step doesn't skip a value, the node's parent should immediately follow (in this example)
        self.assertEqual(self.disjoint_set.tree[2].parent.id, self.disjoint_set.tree[3].id)
        # otherwise, it should skip
        for id, parent_id in {0: 2, 1: 2, 2: 3, 3: 3}.items():
            self.assertEqual(self.disjoint_set.tree[id].parent.id, parent_id)


    def test_union(self):
        """
        test that the union method is working
        :return:
        None
        """

        # add two items to the disjoint set
        self.disjoint_set.add(0)
        self.disjoint_set.add(1)

        # use union to join the two items into one component
        self.disjoint_set.union(0, 1)

        # after union, node 0's parent should be node 1
        self.assertEqual(self.disjoint_set.tree[0].parent.id, self.disjoint_set.tree[1].id)

        # when the combined nodes have the same rank, v's rank should increase
        self.assertEqual(self.disjoint_set.tree[1].rank, 1)
        self.assertEqual(self.disjoint_set.tree[0].rank, 0)

if __name__ == '__main__':
    unittest.main()

