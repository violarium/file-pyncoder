# coding=utf-8
from tests.helpers import *
from lib.files import *
import unittest
import os
import shutil
import codecs


class TestChangeFileEncoding(unittest.TestCase):
    def setUp(self):
        # Create tmp directory to test something
        self.test_dir = os.path.dirname(os.path.realpath(__file__)) + '/tmp'
        self.tearDown()
        os.mkdir(self.test_dir)

    def tearDown(self):
        # Remove tmp directory
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_correct_converting(self):
        """
        Test if files encoding goes correctly
        """
        test_content = u'Hello & Привет'

        # create two files with different encodings
        utf8_filename = self.test_dir + '/utf8.txt'
        windows1251_filename = self.test_dir + '/windows1251.txt'
        with codecs.open(utf8_filename, 'w', 'utf-8') as f:
            f.write(test_content)
        with codecs.open(windows1251_filename, 'w', 'windows-1251') as f:
            f.write(test_content)

        # should not be equal because of different encodings
        utf8_content = read_file(utf8_filename)
        windows1251_content = read_file(windows1251_filename)
        self.assertNotEquals(utf8_content, windows1251_content)

        # Copy and convert one file to another
        utf8_converted_filename = self.test_dir + '/utf8_converted.txt'
        shutil.copy(utf8_filename, utf8_converted_filename)
        change_file_encoding(utf8_converted_filename, 'utf-8', 'windows-1251')
        # Contents should be equal
        utf8_converted_content = read_file(utf8_converted_filename)
        self.assertEquals(windows1251_content, utf8_converted_content)

    def test_backup_files(self):
        """
        Test if backup files are created correctly
        """
        filename = create_test_file(self.test_dir)
        back_filename = filename + '.back'

        # Should not create a backup file
        change_file_encoding(filename, 'utf-8', 'utf-8', False)
        self.assertFalse(os.path.exists(back_filename))

        # Should create a backup file
        change_file_encoding(filename, 'utf-8', 'utf-8')
        self.assertTrue(os.path.exists(back_filename))

    def test_file_not_exists(self):
        """
        Test if an error raises when file not exists
        """
        unknown_filename = self.test_dir + '/unknown_file'
        self.assertRaises(IOError, change_file_encoding, unknown_filename, 'utf-8', 'utf-8')

    def test_incorrect_encodings(self):
        """
        Test if an error raises when unknown encodings are sent
        """
        filename = create_test_file(self.test_dir)
        self.assertRaises(LookupError, change_file_encoding, filename, 'utf-8', 'awesome')
        self.assertRaises(LookupError, change_file_encoding, filename, 'awesome', 'utf-8')


class TestGetFilesList(unittest.TestCase):
    def test_files_list(self):
        """
        Test if getting of files is list going correctly
        """
        self.target_dir = os.path.dirname(os.path.realpath(__file__)) + '/fixtures'
        files_list = get_files_list(self.target_dir)

        files_to_search = [self.target_dir + '/1.txt', self.target_dir + '/sub_dir/2.txt',
                           self.target_dir + '/sub_dir/3.txt']
        self.assertListEqual(files_to_search, files_list)
