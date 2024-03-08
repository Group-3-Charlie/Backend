from flask import Flask, jsonify, request

from api_logic import APILogic


class API:
    def __init__(self):
        self.app = Flask(__name__)
        self.define_routes()

    def define_routes(self):
        @self.app.route('/', methods=['GET'])
        def index():
            return jsonify({'message': 'Welcome to the API!, use /get_routes to see available routes'})

        @self.app.route('/about', methods=['GET'])
        def about():
            return jsonify({'message': 'This is a simple API to demonstrate how to build an API with Flask'})

        @self.app.route('/get_routes', methods=['GET'])
        def get_routes():
            return self._get_routes()

        @self.app.route('/get_data', methods=['GET'])
        def get_data():
            data = request.args.get('data')
            return self._get_data(data)

        @self.app.route('/upload', methods=['POST'])
        def upload():
            return APILogic.upload(request)

        @self.app.route('/select_target', methods=['POST'])
        def select_target():
            return APILogic.select_target(request)

        @self.app.route('/predict', methods=['POST'])
        def predict():
            return APILogic.predict(request)

    def _get_routes(self):
        routes = []
        for rule in self.app.url_map.iter_rules():
            route = {
                'route': str(rule),
                'endpoint': rule.endpoint,
                'methods': list(rule.methods),
                'arguments': list(rule.arguments)
            }
            routes.append(route)
        return jsonify({'routes': routes})

    def _get_data(self, data):
        return jsonify({'data': data})

    def run(self):
        self.app.run("localhost", 4567, debug=True)
