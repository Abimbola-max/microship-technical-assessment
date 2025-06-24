import unittest

from src.controller.quotecontroller import QuoteController
from src.service.quoteservice import QuoteService


class TestQuoteAPI(unittest.TestCase):

    def setUp(self):
        self.service = QuoteService()
        self.controller = QuoteController(self.service)

    def test_add_quote_success(self):
        data = {"description": "This is a test quote."}
        response, status = self.controller.post_quote(data)
        self.assertEqual(status, 201)
        self.assertIn("description", response)
        self.assertEqual(response["description"], data["description"])


if __name__ == '__main__':
    unittest.main()
