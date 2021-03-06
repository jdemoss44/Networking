#!/usr/bin/env python3
# Joshua DeMoss
# 
# A simple test class to check some functionality of rdt.py

import sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(sys.argv[0])))

from network import *
from rdt import *

import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        print("begin setup")
        self.n = Network()
        self.h1 = Host(self.n, '192.168.10.1')
        self.h2 = Host(self.n, '192.168.10.2')
        self.h1.register_protocol(RDTProtocol)
        self.h2.register_protocol(RDTProtocol)
        self.s1 = self.h1.socket(RDTProtocol.PROTO_ID)
        self.s2 = self.h2.socket(RDTProtocol.PROTO_ID)
        self.s2a = self.h2.socket(RDTProtocol.PROTO_ID)

    def test_oneway(self):
        print("begin test 1")
        self.s1.bind(5000)
        self.s2.bind(5001)
        self.s2a.bind(5002)

        self.s1.listen()
        s, _ = self.s1.accept()
        self.s2.connect(('192.168.10.1', 5000))
        # s.send(b'test-notconnected')
        print("done")


        s.send(b'hello')
        self.assertEqual(self.s2.recv(), b'hello')
        s.send(b'')
        self.assertEqual(self.s2.recv(), b'')
        s.send(b' world')
        self.assertEqual(self.s2.recv(), b' world')

if __name__ == '__main__':
    unittest.main()
