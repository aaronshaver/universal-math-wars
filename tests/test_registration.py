import unittest
import uuid

from registration import generate_uuid_string, is_valid_username

class TestRegistration(unittest.TestCase):

    # --- UUID Generation Tests ---

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

    # --- Username Validation Tests ---

    def test_valid_username(self):
        self.assertTrue(is_valid_username("valid_user_123"))
        self.assertTrue(is_valid_username("abc")) # min length
        self.assertTrue(is_valid_username("a" * 20)) # max length
        self.assertTrue(is_valid_username("user-name"))
        self.assertTrue(is_valid_username("USER_NAME"))

    def test_invalid_length(self):
        self.assertFalse(is_valid_username("ab")) # too short
        self.assertFalse(is_valid_username("a" * 21)) # too long

    def test_invalid_characters(self):
        self.assertFalse(is_valid_username("invalid space"))
        self.assertFalse(is_valid_username("invalid!char"))
        self.assertFalse(is_valid_username("invalid@char"))
        self.assertFalse(is_valid_username("invalid.char"))

    def test_blacklisted_substrings(self):
        self.assertFalse(is_valid_username("a_nigger"))
        self.assertFalse(is_valid_username("nigger_my"))
        self.assertFalse(is_valid_username("a_cool_nigger_man"))
        self.assertFalse(is_valid_username("a_cool_NIGGER_man"))