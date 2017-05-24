import unittest
 
from final_traceroute import ipToDict

out = """traceroute to google.com (216.58.209.142), 30 hops max, 60 byte packets
 1  192.168.31.254 (192.168.31.254)  8.134 ms  8.117 ms  8.103 ms
 2  10.59.1.1 (10.59.1.1)  8.112 ms  8.086 ms  8.058 ms
 3  itk-gw.eenet.ee (193.40.194.220)  8.647 ms  8.641 ms  9.222 ms
 4  fi-csc.nordu.net (109.105.98.113)  10.580 ms  15.220 ms  15.231 ms
 5  se-tug.nordu.net (109.105.97.89)  16.518 ms  16.526 ms  16.500 ms
 6  netnod-ix-ge-a-sth.google.com (194.68.123.115)  16.906 ms  10.318 ms  10.220 ms
 7  216.239.43.122 (216.239.43.122)  10.152 ms  10.161 ms  10.136 ms
 8  216.239.49.217 (216.239.49.217)  10.664 ms  10.970 ms  10.906 ms
 9  arn09s05-in-f14.1e100.net (216.58.209.142)  10.835 ms  10.871 ms  10.909 ms"""

my_dict={'192.168.31.254': None, '10.59.1.1': None, '193.40.194.220': None, '109.105.98.113': None, '109.105.97.89': None, 
 '194.68.123.115': None, '216.239.43.122': None, '216.239.49.217': None, '216.58.209.142': None}
 
class HelloWorldTestCase(unittest.TestCase):
    def test_value(self):
        result = ipToDict(out)
        self.assertDictEqual(my_dict, result)

