import lib.files
import lib.filters
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Convert file encodings.')

# the target - file or directory
parser.add_argument('--target', '-t', action='store', type=str, required=True)

# converter options
parser.add_argument('--in-encoding', '-i',  action='store', required=True)
parser.add_argument('--out-encoding', '-o', action='store', required=True)
parser.add_argument('--keep-backup', '-k',  action='store_true', default=True)

# the regular expressions: to include and exclude files
parser.add_argument('--regexp', '-r', action='store')
parser.add_argument('--ng-regexp', '-nr', action='store')

# the extensions: can include or exclude extensions
group = parser.add_mutually_exclusive_group()
group.add_argument('--extensions', '-e', action='store')
group.add_argument('--ng-extensions', '-ne', action='store')

args = parser.parse_args()


# check whether file or directory
if os.path.isdir(args.target):
    pass
elif os.path.isfile(args.target):
    lib.files.change_file_encoding(args.target, args.in_encoding, args.out_encoding, args.keep_backup)
    pass
else:
    print "There are no file or directory '%s'" % args.target
    sys.exit(1)
