import unittest

from src.controller.quotecontroller import QuoteController
from src.service.quoteservice import QuoteService


class TestQuoteService(unittest.TestCase):
    def setUp(self):
        self.service = QuoteService()
        self.controller = QuoteController(self.service)

    def test_add_quote(self):
        self.controller.add_quote()
        self.assertEqual(len(self.service.list_of_quotes), 1)


if __name__ == '__main__':
    unittest.main()
