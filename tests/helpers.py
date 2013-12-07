def read_file(filename):
    """
    Read the whole filename
    """
    return open(filename, 'r').read()


def create_test_file(directory):
    """
    Create a test.txt file in directory
    """
    filename = directory + '/test.txt'
    with open(filename, 'w') as f:
        f.write('test')
    return filename