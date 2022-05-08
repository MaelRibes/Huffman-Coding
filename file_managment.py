import os

def bin_writer(file_name, text_bin):
    compressed_file = open('results/' + file_name + '_comp.bin', 'wb')
    compressed_file.write(text_bin)
    compressed_file.close()


def freq_writer(file_name, freq):
    frequencies_file = open('results/' + file_name + '_freq.txt', 'w')
    frequencies_file.write('Number of different characters : '+str(len(freq))+'\n\n')
    frequencies_file.write('Number of occurrences of each character : '+'\n')
    for char in freq:
        if char == '\n':
            frequencies_file.write("\\n " + str(freq[char]) + '\n')
        else:
            frequencies_file.write(char + " " + str(freq[char]) + '\n')
    frequencies_file.close()


def size(file_path):
    return os.path.getsize(file_path)