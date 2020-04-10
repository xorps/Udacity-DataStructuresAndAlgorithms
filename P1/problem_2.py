import os
import sys
import unittest

def find_files(suffix, path):
    files = []
    queue = []
    def add_paths(path):
        if os.path.isfile(path):
            if path.endswith(suffix):
                files.append(path)
        else:
            queue.extend(os.path.join(path, new_path) for new_path in os.listdir(path))
    add_paths(path)
    while len(queue) > 0:
        path = queue.pop()
        add_paths(path)
    return files

class FindFilesTest(unittest.TestCase):
    def test_cfiles(self):
        expected = [
            'testdir/subdir1/a.c',
            'testdir/subdir3/subsubdir1/b.c',
            'testdir/subdir5/a.c',
            'testdir/t1.c'
        ]
        actual = find_files('.c', 'testdir')
        self.assertEqual(sorted(actual), sorted(expected))
    def test_hfiles(self):
        expected = [
            'testdir/subdir1/a.h',
            'testdir/subdir3/subsubdir1/b.h',
            'testdir/subdir5/a.h',
            'testdir/t1.h'
        ]
        actual = find_files('.h', 'testdir')
        self.assertEqual(sorted(expected), sorted(actual))
    def test_emptysuffix(self):
        expected = [
            'testdir/t1.h',
            'testdir/t1.c',
            'testdir/subdir5/a.h',
            'testdir/subdir5/a.c',
            'testdir/subdir4/.gitkeep',
            'testdir/subdir3/subsubdir1/b.h',
            'testdir/subdir3/subsubdir1/b.c',
            'testdir/subdir2/.gitkeep',
            'testdir/subdir1/a.h',
            'testdir/subdir1/a.c'
        ]
        actual = find_files('', 'testdir')
        self.assertEqual(sorted(expected), sorted(actual))
    def test_path_is_file(self):
        expected = ['testdir/t1.c']
        actual = find_files('.c', 'testdir/t1.c')
        self.assertEqual(actual, expected)
    def test_path_is_file_wrong_ext(self):
        expected = []
        actual = find_files('.h', 'testdir/t1.c')
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()