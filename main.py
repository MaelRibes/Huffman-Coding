
def get_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def alpha_sort(f):
    freq = sorted(f.items(), key=lambda x: x[1])
    for k in range(len(freq)):
        for index in range(len(freq) - 1):
            freq1 = freq[index]
            freq2 = freq[index + 1]
            if freq1[1] == freq2[1]:
                if ord(freq1[0]) > ord(freq2[0]):
                    freq[index], freq[index + 1] = freq[index + 1], freq[index]
    res = tuplelist_to_dict(freq)
    return res


def tuplelist_to_dict(li):
    di = {}
    for tu in li:
        di[tu[0]] = tu[1]
    return di


class Node:
    def __init__(self, char, proba, left=None, right=None):
        self.char = char
        self.proba = proba
        self.left = left
        self.right = right
        self.code = None

    def __str__(self):
        return f'Node({self.char},{self.proba},{self.left},{self.right},{self.code})'

    def is_leaf(self):
        if(self.left is None)and(self.right is None):
            return True
        return False


def create_list_leaf(dict):
    list_node = []
    for k in dict.keys():
        proba = dict[k]
        list_node.append(Node(k,proba))
    return list_node


def insert_node(l_nodes, node):
    if len(l_nodes) == 0:
        l_nodes.append(node)
        return l_nodes
    for i in range(len(l_nodes)):
        if node.proba <= l_nodes[i].proba:
            l_nodes.insert(i, node)
            return l_nodes
        else:
            l_nodes.append(node)
            return l_nodes


def create_huffman_tree(dict_freq):
    nodes = create_list_leaf(dict_freq)
    while len(nodes) > 1:
        l_child = nodes[0]
        l_child.code = 0
        nodes.pop(0)
        r_child = nodes[0]
        r_child.code = 1
        nodes.pop(0)
        father = Node('\0', r_child.proba + l_child.proba, l_child, r_child)
        insert_node(nodes, father)
    return nodes[0]


def coding_char(node, p, cod):
    if node.is_leaf():
        str_path = ""
        for i in p:
            str_path += str(i)
        cod[node.char] = str_path
        return
    if node.left is not None:
        p.append(node.left.code)
        coding_char(node.left, p, cod)
        p.pop(len(p) - 1)
    if node.right is not None:
        p.append(node.right.code)
        coding_char(node.right, p, cod)
        p.pop(len(p) - 1)


def get_coding(root):
    path = []
    coding = {}
    coding_char(root, path, coding)
    return coding


def huffman_coding(text):
    frequencies_char = get_frequencies(text)
    freq_char_sorted = alpha_sort(frequencies_char)
    root = create_huffman_tree(freq_char_sorted)
    codage = get_coding(root)
    compressed_text = ""
    for char in text:
        compressed_text += codage[char]
    return compressed_text


def file_compression(file_name):
    file = open('donnees/'+file_name+'.txt', 'r')
    text = file.read()
    file.close()
    compressed_text = huffman_coding(text)
    text_bin = int(compressed_text, base=2).to_bytes((len(compressed_text) + 7) // 8, byteorder='big')
    compressed_file = open('results/'+file_name+'_comp.bin', 'wb')
    compressed_file.write(text_bin)
    compressed_file.close()

file_compression('extraitalice')














