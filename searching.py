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


def main():
    file = read_data('sequential.json', 'dna_sequence')
    print(file)


if __name__ == '__main__':
    main()