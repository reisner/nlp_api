from flask import Flask, request
from flask_restful import Resource, Api

import analyze_text as at

app = Flask(__name__)
api = Api(app)

class analyze_text(Resource):
    def get(self):
        return {'error': 'Please POST your query text.'}

    def put(self):
        data = request.form
        if 'text' in data.keys():
            text = data['text'].strip()
            if len(text) > 0:
                return at.analyze_text_block(text)
            else:
                return {'error': 'text was too short!'}
        else:
            return {'error': 'key "text" not found in data'}

api.add_resource(analyze_text, '/analyze_text')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8011)
