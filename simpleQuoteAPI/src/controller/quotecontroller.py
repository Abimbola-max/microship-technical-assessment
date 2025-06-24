from src.service.quoteservice import QuoteService


class QuoteController:
    
    def __init__(self, quoteservice: QuoteService):
        self.quoteservice = quoteservice