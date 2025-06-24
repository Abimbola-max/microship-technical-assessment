from src.dto.request.quoterequest import QuoteRequest
from src.dto.response.quoteresponse import QuoteResponse


class QuoteService:

    def __init__(self):
        self.list_of_quotes = []

    def add_quote(self, description: str)-> Quote:
        self.list_of_quotes.append(description)