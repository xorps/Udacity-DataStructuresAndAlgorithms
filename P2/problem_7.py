from collections import defaultdict
import unittest

class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = defaultdict(RouteTrieNode)
    def insert(self, path):
        return self.children[path]

class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)
    def insert(self, paths, handler):
        node = self.root
        for path in paths:
            node = node.insert(path)
        node.handler = handler
    def find(self, paths):
        node = self.root
        for path in paths:
            if path not in node.children: return None
            node = node.children[path]
        return node.handler

class Router:
    def __init__(self, root_handler, not_found_handler):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler
    def add_handler(self, path, handler):
        self.route_trie.insert(self.split_path(path), handler)
    def lookup(self, path):
        handler = self.route_trie.find(self.split_path(path))
        return handler if handler else self.not_found_handler
    def split_path(self, path):
        return [route for route in path.split('/') if route]

class RouterTests(unittest.TestCase):
    def test_split_paths(self):
        self.assertEqual(Router.split_path(None, '/'), [])
        self.assertEqual(Router.split_path(None, '/home'), ['home'])
        self.assertEqual(Router.split_path(None, '/home/about'), ['home', 'about'])
        self.assertEqual(Router.split_path(None, '/home/about/'), ['home', 'about'])
        self.assertEqual(Router.split_path(None, '/home/about/me'), ['home', 'about', 'me'])
    def test_cases(self):
        router = Router('root handler', 'not found handler')
        router.add_handler('/home/about', 'about handler')
        self.assertEqual(router.lookup('/'), 'root handler')
        self.assertEqual(router.lookup('/home'), 'not found handler')
        router.add_handler('/home/', 'home handler')
        self.assertEqual(router.lookup('/home'), 'home handler')
        self.assertEqual(router.lookup('/home/'), 'home handler')
        self.assertEqual(router.lookup('/home/about'), 'about handler')
        self.assertEqual(router.lookup('/home/about/'), 'about handler')
        self.assertEqual(router.lookup('/home/about/me'), 'not found handler')
        router.add_handler('/home/about/me', 'about me')
        self.assertEqual(router.lookup('home/about/me'), 'about me')

if __name__ == '__main__':
    unittest.main()