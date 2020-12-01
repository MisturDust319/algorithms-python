"""
Based on:
https://www.educative.io/m/boggle
"Given a N×N grid of characters and a dictionary,
find all words which can be made from the characters in the grid and are present in the given dictionary."
Words can start or end on any character, and words may be horizontal, vertical, or diagonal
Characters must be adjacent

Code largely borrowed from:
https://github.com/macallmcqueen/boggle-solver-using-trie/blob/master/boggle_solver.py
"""
from collections import deque


class VocabularyTrieNode:
    """
    A node for a vocabulary trie
    """
    def __init__(self):
        #
        self.children = {}
        self.value = None


class VocabularyTrie:
    def __init__(self, vocabulary):
        """
        Initialize the vocabulary object
        It requires an iterable of strings
        """
        # create a root node
        self.root = VocabularyTrieNode()

        # we need to add each word in the vocabulary into the trie
        for word in vocabulary:
            # we need a cursor node to track our position in the trie
            # first, we initialize it to the root node of the trie
            current_node = self.root

            # we need to add each letter of the word to the trie
            for letter in word:
                # if the current letter is not a child of the current node,
                # add it
                if letter not in current_node.children:
                    current_node.children[letter] = VocabularyTrieNode()
                # set the new current node
                current_node = current_node.children[letter]

            # if it is the final node for this vocabulary word,
            # set it's value to the current word
            # this signals a complete string in the tree, while minimizing
            # the amount of storage used
            current_node.value = word


def find_all_strings(board, dictionary):
    """
    """
    # we need the board length and width
    board_length = len(board)
    board_width = len(board[0])

    # create a trie from the dictionary
    vocab = VocabularyTrie(dictionary)

    # this set is our solutions
    solutions = set()

    # we want to visit each position in our board...
    for i in range(board_length):
        for j in range(board_width):
            # ...and find all the possible strings that can be found from that
            # position
            solutions.update(_search_from_position(i, j, vocab, board))

    return solutions


def _search_from_position(i, j, vocabulary, board):
    """
    Find all boggle strings starting at (i, j),
    given a vocabulary and a board
    """
    # this search process uses DFS
    # so, we need a stack object
    # each value in the stack is a 4-tuple:
    # - i, j are the first two values which represent a coordinate
    # (initially the position this function is called with)
    # - a node in the vocabulary trie
    # (initially the root)
    # - a copy of the board
    # (initially the board as it is when the function is called)
    stack = deque([(i, j, vocabulary.root, board)])

    # while there are still values in our stack
    while stack:
        # isolate each tuple value
        x, y, current_node, current_board = stack.pop()

        # we have the state of the board from the stack
        # now we must check all the neighboring characters in the boggle board
        for neighbor in _find_neighbors(board, x, y):
            # get the neighbor's coordinates
            neighbor_x, neighbor_y = neighbor
            # get the actual character stored in this neighbor
            current_character = current_board[neighbor_x][neighbor_y]

            # any further actions require that the character from this neighbor
            # is a child of the current node in the trie
            # that is, we can form further strings with this character
            if current_character in current_node.children:
                # first, get the actual child node
                child_node = current_node.children[current_character]

                # next, we check whether the path to this neighbor node
                # represents a valid term in our vocabulary
                # if the child node has a value, we have found a valid term
                if child_node.value is not None:
                    # so we yield that string
                    yield child_node.value

                # lastly, because the neighbor character is in the trie,
                # we need to continue our search from there
                # we'll need a copy of the current board
                board_copy = [[i for i in j] for j in current_board]
                # set the current position in the board copy to None
                # this marks the current position as visited in future searches
                # and prevents backtracking to the current node
                board_copy[x][y] = None

                stack.append((neighbor_x, neighbor_y, child_node, board_copy))


def _find_neighbors(board, x, y):
    board_length = len(board)
    board_width = len(board[0])

    # use max and min to set our bounds
    # clever, Macall, I never thought of this.
    # I shall use this in future code...
    row_lower_bound = max(0, x-1)
    row_upper_bound = min(board_width-1, x+1)
    col_lower_bound = max(0, y-1)
    col_upper_bound = min(board_length-1, y+1)

    for i in range(row_lower_bound, row_upper_bound+1):
        for j in range(col_lower_bound, col_upper_bound+1):
            # we yield every valid value in this range outside of (x, y)
            # (we don't want to constantly revisit our start position)
            if i != x or j != y:
                yield i, j
