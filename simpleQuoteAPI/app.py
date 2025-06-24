from flask import Flask

from src.controller.quotecontroller import QuoteController
from src.service.quoteservice import QuoteService

app = Flask(__name__)


quote_service = QuoteService()
quote_controller = QuoteController(quote_service)

@app.route("/quotes", methods=["GET"])
def get_quotes():
    return quote_controller.get_quotes()

@app.route("/quotes", methods=["POST"])
def add_quote():
    return quote_controller.add_quote()

if __name__ == "__main__":
    app.run(debug=True)
