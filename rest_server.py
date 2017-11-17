from flask import Flask, request
from flask_restful import Resource, Api

import analyze_text

app = Flask(__name__)
api = Api(app)

class home(Resource):
    def get(self):
        return {'error': 'Please POST your query text.'}

    def put(self):
        data = request.form
        if 'text' in data.keys():
            text = data['text'].strip()
            if len(text) > 0:
                return analyze_text.analyze_text_block(text)
            else:
                return {'error': 'text was too short!'}
        else:
            return {'error': 'key "text" not found in data'}

api.add_resource(home, '/')

if __name__ == '__main__':
    app.run(port = 8011)
