import unittest
from indiosint.phone import lookup_phone
from indiosint.utils import print_banner, extract_potential_name, extract_emails

class TestIndiOSINT(unittest.TestCase):
    def test_banner(self):
        # Just check if it runs without error
        try:
            print_banner()
        except Exception as e:
            self.fail(f"print_banner failed with {e}")

    def test_phone_logic_invalid(self):
        # Test with invalid number
        try:
            lookup_phone("123")
        except Exception as e:
            self.fail(f"lookup_phone failed with {e}")

    def test_extraction_logic(self):
        # Test name extraction
        self.assertEqual(extract_potential_name("https://www.linkedin.com/in/john-doe-123"), "John Doe")
        self.assertEqual(extract_potential_name("https://twitter.com/johndoe"), "johndoe")

        # Test email extraction
        emails = extract_emails("Contact me at test@example.com or info@domain.in")
        self.assertIn("test@example.com", emails)
        self.assertIn("info@domain.in", emails)

if __name__ == "__main__":
    unittest.main()
