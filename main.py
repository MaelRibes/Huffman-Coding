import file_managment
import frequences
import huffman
from node import Node

print('============================= Huffman compression =============================\n')
file_name = input('Input file name : ')
file = open('assets/'+file_name+'.txt', 'r')
text = file.read()
file.close()

freq = frequences.get_frequencies(text)
root = huffman.create_huffman_tree(freq)
coding = huffman.get_coding(root)

compressed_text = huffman.huffman_coding(text, coding)
text_bin = int(compressed_text, base=2).to_bytes((len(compressed_text) + 7) // 8, byteorder='big')

file_managment.bin_writer(file_name, text_bin)
file_managment.freq_writer(file_name, freq)

initial_size = file_managment.size('assets/'+file_name+'.txt')
final_size = file_managment.size('results/' + file_name + '_comp.bin')
compression_rate = 1 - (final_size/initial_size)

bits_avarage = huffman.bits_avarage(coding, freq)

print('Compression rate : ', compression_rate)
print('Avarage bit per char : ', bits_avarage)






















