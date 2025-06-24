from flask import jsonify, request
from marshmallow import ValidationError

from src.dto.request.quoterequest import QuoteRequest
from src.dto.response.quoteresponse import QuoteResponse
from src.service.quoteservice import QuoteService


class QuoteController:
    
    def __init__(self, quoteservice: QuoteService):
        self.quoteservice = quoteservice

    def add_quote(self):
        try:
            data = request.json
            schema = QuoteRequest()
            validated_data = schema.load(data)

            description = validated_data["description"]
            self.quoteservice.add_quote(description)

            response_schema = QuoteResponse()
            response_data = {
                "message": "Quote added successfully",
                "date": validated_data.get("date_quoted", None),
            }
            response = response_schema.dump(response_data)
            return jsonify(response), 201

        except ValidationError as e:
            return jsonify({"error": e.messages}), 400

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_quotes(self):
        quotes = self.quoteservice.get_all_quotes()
        quote_list = [
            {
                "description": quote.description,
                "date_quoted": quote.date_quoted,
            }
            for quote in quotes
        ]
        return jsonify({"quotes": quote_list}), 200