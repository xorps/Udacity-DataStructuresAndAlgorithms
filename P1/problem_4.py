from collections import deque
import unittest

class Group:
    def __init__(self, name):
        self.name = name
        self.groups = []
        self.users = []
    def add_group(self, group):
        self.groups.append(group)
    def add_user(self, user):
        self.users.append(user)
    def get_groups(self):
        return self.groups
    def get_users(self):
        return self.users

def is_user_in_group(user, group):
    if not isinstance(user, str): raise TypeError('expected user to be a string')
    if len(user) == 0: raise ValueError('excepted non-empty string')
    if not isinstance(group, Group): raise TypeError('expected group to be of type Group')
    queue = deque()
    queue.append(group)
    while len(queue) > 0:
        group = queue.popleft()
        if user in group.get_users(): return True
        queue.extend(group.get_groups())
    return False

class GroupTests(unittest.TestCase):
    def test_a(self):
        self.assertEqual(is_user_in_group('user', Group('bob')), False)
    def test_recurse(self):
        gA = Group('GroupA')
        gB = Group('GroupB')
        gC = Group('GroupC')
        gC.add_user('Bob')
        gB.add_group(gC)
        gA.add_group(gB)
        self.assertEqual(is_user_in_group('user', gA), False)
        self.assertEqual(is_user_in_group('Bob', gA), True)
        self.assertEqual(is_user_in_group('Bob', gB), True)
        self.assertEqual(is_user_in_group('Bob', gC), True)
    def test_inputs(self):
        with self.assertRaises(ValueError):
            is_user_in_group('', Group('test'))
        with self.assertRaises(TypeError):
            is_user_in_group(None, Group('test'))
        with self.assertRaises(TypeError):
            is_user_in_group('user', 'group')

if __name__ == '__main__':
    unittest.main()