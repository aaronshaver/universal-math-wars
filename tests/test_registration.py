import unittest
import uuid

from registration import generate_uuid_string

class TestRegistration(unittest.TestCase):

    def test_generate_uuid_string_returns_string(self):
        """generate_uuid_string() should return a str."""
        self.assertIsInstance(generate_uuid_string(), str)

    def test_generate_uuid_string_valid_uuid_v4(self):
        """The string should parse as a canonical UUID‑v4."""
        val = generate_uuid_string()
        parsed = uuid.UUID(val, version=4)
        self.assertEqual(parsed.version, 4)
        self.assertEqual(str(parsed), val)  # same canonical form

    def test_generate_uuid_string_uniqueness(self):
        """Two successive calls shouldn't collide (very low‑probability sanity check)."""
        self.assertNotEqual(generate_uuid_string(), generate_uuid_string())
