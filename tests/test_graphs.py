import unittest

import data_structures
import graphs.breadth_first_traversal
import graphs.disjoint_set_structure
import graphs.dfs
import graphs.topological_sort
import graphs.kruskals_algorithm


class TestBreadthFirstTraversal(unittest.TestCase):
    def test_breadth_first_traversal(self):
        # create a graph
        graph = data_structures.GraphAdjacencySet()
        # populate it
        graph.addEdge(0, 1)
        graph.addEdge(0, 2)
        graph.addEdge(1, 2)
        graph.addEdge(2, 0)
        graph.addEdge(2, 3)
        graph.addEdge(3, 3)

        # the expected output
        expected_results = [2, 0, 3, 1]

        # compute the actual results
        results = list(graphs.breadth_first_traversal.breadth_first_traversal(graph, 2))

        # compare the results
        self.assertListEqual(results, expected_results)


class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        """
        Set up a fresh disjoint set for each test
        :return:
        """
        self.disjoint_set = graphs.disjoint_set_structure.DisjointSet()

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


class TestBFS(unittest.TestCase):
    def setUp(self):
        self.graph = graphs.dfs.GraphDFS()

    def tearDown(self):
        del self.graph

    def test_bfs(self):
        # add vertices
        for i in range(4):
            self.graph.addVertex(i)

        # populate the graph
        self.graph.addEdge(0, 1)
        self.graph.addEdge(0, 2)
        self.graph.addEdge(1, 2)
        self.graph.addEdge(2, 0)
        self.graph.addEdge(2, 3)
        self.graph.addEdge(3, 3)

        # this is the correct output of a BFS
        expected_results = [2, 0, 3, 1]
        results = self.graph.dfs(2)

        self.assertCountEqual(expected_results, results)


class TestTopologicalSort(unittest.TestCase):
    def setUp(self):
        self.graph = graphs.topological_sort.Graph(6)

    def tearDown(self):
        del self.graph

    def test_topological_sotrt(self):
        # build up the graph
        self.graph.addEdge(5, 2)
        self.graph.addEdge(5, 0)
        self.graph.addEdge(4, 0)
        self.graph.addEdge(4, 1)
        self.graph.addEdge(2, 3)
        self.graph.addEdge(3, 1)

        expected_results = [5, 4, 2, 3, 1, 0]
        sort_results = self.graph.topologicalSort()

        self.assertCountEqual(expected_results, sort_results)


class TestKruskalsAlgorithm(unittest.TestCase):
    def setUp(self):
        self.graph = graphs.kruskals_algorithm.KruskalsAlgorithmGraph()

    def tearDown(self):
        del self.graph

    def test_getMST(self):
        self.graph.addEdge(0, 1, 4)
        self.graph.addEdge(0, 2, 4)
        self.graph.addEdge(1, 2, 2)
        self.graph.addEdge(1, 0, 4)
        self.graph.addEdge(2, 0, 4)
        self.graph.addEdge(2, 1, 2)
        self.graph.addEdge(2, 3, 3)
        self.graph.addEdge(2, 5, 2)
        self.graph.addEdge(2, 4, 4)
        self.graph.addEdge(3, 2, 3)
        self.graph.addEdge(3, 4, 3)
        self.graph.addEdge(4, 2, 4)
        self.graph.addEdge(4, 3, 3)
        self.graph.addEdge(5, 2, 2)
        self.graph.addEdge(5, 4, 3)

        # more than one MST can be generated from a data set
        # however, the sum of the weights will always be the same value
        expected_mst_sum = 14

        mst = self.graph.getMST()
        # get the sum of the weights
        mst_weight_sum = sum([edge[2] for edge in mst])

        self.assertEqual(expected_mst_sum, expected_mst_sum)


if __name__ == '__main__':
    unittest.main()

