import codecs
import os

def change_file_encoding(filename, in_encoding, out_encoding, keep_backup=True):
    """
    Change file encoding, override or keep a backup
    """
    print 'Preparing file', filename
    try:
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
            
    except Exception, e:
        print e


def get_files_list(root_dir, filters):
    """
    Collect files in directory by filter
    """
    file_list = []
    # walk recursively
    for root, subFolders, files in os.walk(root_dir):
        for filename in files:
            correct = True
            full_path = os.path.join(root, filename)

            # check each file with each filter
            for filter_func in filters:
                correct = correct and filter_func(full_path)

            # add file if it's correct
            if correct:
                file_list.append(full_path)

    return file_list
