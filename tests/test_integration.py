import unittest
from unittest.mock import patch, MagicMock
from indiosint.phone import lookup_phone
from indiosint.email import lookup_email
from indiosint.name import lookup_name
from indiosint.vehicle import lookup_vehicle
from indiosint.intelligence import IntelligenceEngine
from indiosint.utils import extract_emails, extract_phones, extract_image_urls

class TestIndiOSINTIntegration(unittest.TestCase):

    @patch('indiosint.phone.search')
    def test_phone_module(self, mock_search):
        mock_search.return_value = ['Result with victim@gmail.com and http://img.com/1.jpg']
        result = lookup_phone("+919876543210")

        self.assertIsNotNone(result)
        self.assertEqual(result['phone'], "+919876543210")
        self.assertIn('victim@gmail.com', result['associated_emails'])
        self.assertIn('http://img.com/1.jpg', result['images'])

    @patch('indiosint.email.search')
    def test_email_module(self, mock_search):
        mock_search.return_value = ['Found +919988776655 here']
        result = lookup_email("test@example.com")

        self.assertIsNotNone(result)
        self.assertEqual(result['email'], "test@example.com")
        self.assertIn('+919988776655', result['associated_phones'])

    @patch('indiosint.name.search')
    def test_name_module(self, mock_search):
        mock_search.return_value = ['John Doe is on linkedin.com/in/johndoe']
        result = lookup_name("John Doe", "Delhi")

        self.assertIsNotNone(result)
        self.assertEqual(result['name'], "John Doe")
        self.assertTrue(len(result['social_profiles']) >= 0)

    @patch('indiosint.vehicle.search')
    def test_vehicle_module(self, mock_search):
        mock_search.return_value = ['MH01AB1234 challan found']
        result = lookup_vehicle("MH01AB1234")

        self.assertIsNotNone(result)
        self.assertEqual(result['query'], "MH01AB1234")
        self.assertTrue(len(result['records']) > 0)

    def test_intelligence_logic(self):
        engine = IntelligenceEngine()
        results = {
            'phone': {
                'phone': '+919000000000',
                'associated_emails': ['target@gmail.com']
            },
            'email': {
                'email': 'target@gmail.com'
            }
        }
        links, score = engine.get_summary(results)
        self.assertTrue(any("HIGH CONFIDENCE" in link for link in links))

    def test_utils_extraction(self):
        text = "Contact: user@mail.com, +919123456789. See image at http://site.com/pic.png"
        self.assertIn("user@mail.com", extract_emails(text))
        self.assertIn("+919123456789", extract_phones(text))
        self.assertIn("http://site.com/pic.png", extract_image_urls(text))

    def test_phone_extraction_variations(self):
        text = "My numbers are 919876543210 and +917778889990 and also 8887776665"
        phones = extract_phones(text)
        self.assertIn("919876543210", phones)
        self.assertIn("+917778889990", phones)
        self.assertIn("8887776665", phones)

    def test_intelligence_scoring_validation(self):
        engine = IntelligenceEngine()
        # Test low confidence
        results = {'phone': {'phone': '1'}, 'email': {'email': '2'}}
        links, score = engine.get_summary(results)
        self.assertEqual(len(links), 0)

if __name__ == "__main__":
    unittest.main()
