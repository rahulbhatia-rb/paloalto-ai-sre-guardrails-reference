import unittest
from src.remediation import Signal,action
class T(unittest.TestCase):
 def test_executes_bounded(self):self.assertEqual(action(Signal(.95,.8,1,True)),'execute-bounded-remediation')
 def test_protects_budget(self):self.assertEqual(action(Signal(.99,.1,1,True)),'escalate-protect-reliability')
 def test_requires_review(self):self.assertEqual(action(Signal(.7,.8,1,True)),'propose-for-review')
