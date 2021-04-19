import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, 'r') as f:
        file = json.load(f)
    if field not in {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}:
        return None
    else:
        return file[field]

def linear_search(sequence, number=5):
    indices = []
    count = 0
    i = 0

    for i in range (0,len(sequence),1):
        if sequence[i] == number:
            indices.append(i)
            count += 1
    return {'positions': indices,'count': count}

def pattern_search(sequence, pattern):
    l = len(pattern)
    indices = []

    for i in range(0,(len(sequence)-3),1):
        if sequence[i:i+l] == pattern:
            indices.append(i)
    return indices

def main():
    file = read_data('sequential.json', 'unordered_numbers')
    print(file)
    number = int(input('Zadajte cislo: '))
    results = linear_search(file, number)
    print(results)
    seq = input('Zadajte hladanu sekvenciu:')
    pattern = pattern_search(read_data('sequential.json', 'dna_sequence'), seq)
    print(pattern)

if __name__ == '__main__':
    main()