import codecs
import os


def change_file_encoding(filename, in_encoding, out_encoding, keep_backup=True):
    """
    Change file encoding, override or keep a backup
    """
    # open and read file with defined encoding
    sf = codecs.open(filename, 'r', in_encoding)
    try:
        content = sf.read()
    finally:
        sf.close()

    # backup the file if it's necessary
    if keep_backup:
        os.rename(filename, filename + '.back')

    # open and write file with new encoding
    df = codecs.open(filename, 'w', out_encoding)
    try:
        df.write(content)
    finally:
        df.close()


def get_files_list(root_dir):
    """
    Collect files in directory
    """
    file_list = []
    # walk recursively
    for root, subFolders, files in os.walk(root_dir):
        for filename in files:
            full_path = os.path.join(root, filename)
            file_list.append(full_path)
    return file_list
