#much of this code was provided. Where the YOUR CODE HERE TAGS are is of course where my code begins. 
#It ends at the end of that function scope usually
class Tree:
    def __init__(self, datum, *args):
        self.datum = datum
        self.children = []
        for tree in args:
            self.children.append(tree)
    def pretty_print(self, indent=''):
        """ Prints the tree.
        >>> t = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6)))
        >>> t.pretty_print()
        1
        |__2
        |  |__4
        |  |__5
        |__3
           |__6
           
        >>> Tree(0, Tree('hello'), Tree('world'), Tree('!')).pretty_print()
        0
        |__hello
        |__world
        |__!
        >>> Tree(0, Tree('hello', Tree('world')), Tree('Goodbye')).pretty_print()
        0
        |__hello
        |  |__world
        |__Goodbye

        """
        if not indent:
            print(self.datum)
        else:
            print(indent[:-3] + '|__' + str(self.datum))

        if self.children:
            for child in self.children[:-1]:
                child.pretty_print(indent + '|  ')
            self.children[-1].pretty_print(indent + '   ')


class HuffmanTree(Tree):
    def __init__(self, *children):
        letters = []
        for child in children:
            letters += child.datum
        Tree.__init__(self, letters, *children)
        while len(self.children) > 2:
            self.merge_two_smallest()

#Q1        "*** YOUR CODE HERE ***"
    def merge_two_smallest(self):
        smallest = min(self.children, key=lambda x: x.frequency)
        self.children.pop(self.children.index(smallest))
        next_smallest = min(self.children, key=lambda x: x.frequency)
        node = HuffmanTree(smallest, next smallest)
        self.children.append(node)
#END Q1

    @property
    def left_child(self):
        assert len(self.children) == 2
        return self.children[0]

    @property
    def right_child(self):
        assert len(self.children) == 2
        return self.children[1]

    @property
    def frequency(self):
        return sum([child.frequency for child in self.children])

    def encode_character(self, character):
        """ Returns a string representing the Huffman encoding of the
        character.

        >>> t = make_example_huffman_tree()
        >>> t.encode_character('E')
        '1100'
        >>> [t.encode_character(letter) for letter in t.datum]
        ['0', '100', '1010', '1011', '1100', '1101', '1110', '1111']
        """
        assert character in self.datum
        "*** YOUR CODE HERE ***"

    def encode(self, string):
        """ Returns a string representing the Huffman encoding of the
        character.

        >>> t = make_example_huffman_tree()
        >>> t.encode('BACADAEAFABBAAAGAH')
        '100010100101101100011010100100000111001111'
        """
        result = ''
        for character in string:
            result += self.encode_character(character)
        return result

    def decode_character(self, code):
        """ Decodes a single character from code.
        Returns the character, and the rest of the code (that has not
        been decoded yet).
        code is a Huffman encoding created from this HuffmanTree.

        >>> t = make_example_huffman_tree()
        >>> t.decode_character('0')
        ('A', '')
        >>> t.decode_character('10001010')
        ('B', '01010')
        """
        "*** YOUR CODE HERE ***"

    def decode(self, code):
        """ Decodes code to recover the original message.
        code is a Huffman encoding created from this HuffmanTree.

        >>> t = make_example_huffman_tree()
        >>> t.decode('100010100101101100011010100100000111001111')
        'BACADAEAFABBAAAGAH'
        """
        result = ''
        while code:
            character, code = self.decode_character(code)
            result += character
        return result

    # Utility method for making the Huffman tree canonical
    def sort_by_frequency(self):
        self.datum.sort()
        self.children.sort(key=lambda x: x.frequency, reverse=True)
        for child in self.children:
            child.sort_by_frequency()

class HuffmanLeaf(Tree):
    def __init__(self, letter, frequency):
        Tree.__init__(self, [ letter ])
        self.letter = letter
        self.frequency = frequency

    def encode_character(self, character):
        assert character == self.letter
        "*** YOUR CODE HERE ***"

    def decode_character(self, code):
        "*** YOUR CODE HERE ***"

    # Utility method for making the Huffman tree canonical
    def sort_by_frequency(self):
        pass
def make_huffman_tree(letters, frequencies):
    """ Generates a Huffman tree that gives the optimal
    variable-length prefix encoding for letters given the
    frequencies.

    >>> huff_tree = make_example_huffman_tree()
    >>> huff_tree.pretty_print()
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    |__['A']
    |__['B', 'C', 'D', 'E', 'F', 'G', 'H']
       |__['B', 'C', 'D']
       |  |__['B']
       |  |__['C', 'D']
       |     |__['C']
       |     |__['D']
       |__['E', 'F', 'G', 'H']
          |__['E', 'F']
          |  |__['E']
          |  |__['F']
          |__['G', 'H']
             |__['G']
             |__['H']
    """
    assert len(letters) == len(frequencies)
    children = []
    for i in range(len(letters)):
        children.append(HuffmanLeaf(letters[i], frequencies[i]))
    return HuffmanTree(*children)


# Utility function for use in doctests
def make_example_huffman_tree():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    frequencies = [1000, 300, 105, 104, 103, 102, 101, 100]
    tree = make_huffman_tree(letters, frequencies)
    tree.sort_by_frequency()
    return tree
