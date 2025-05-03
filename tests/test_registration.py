import unittest
import uuid

from registration import generate_uuid

class TestRegistration(unittest.TestCase):

    def test_generate_uuid(self):
        """Test that generate_uuid returns a valid UUID."""
        result = generate_uuid()
        self.assertIsInstance(result, uuid.UUID)
