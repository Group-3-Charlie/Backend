"""
flask -> Flask, jsonify, request
flasgger -> Swagger
api_logic -> APILogic
"""
from flask import Flask, jsonify, request

from api_logic import APILogic

app = Flask(__name__)


class API:
    """
    API class to define the routes and run the API.
    """

    def __init__(self) -> None:
        """
        Constructor to initialize the API.
        """
        self.app = Flask(__name__)
        self.define_routes()

    def define_routes(self) -> None:
        """
        Defines the routes for the API.
        :return:
        """

        @self.app.route('/', methods=['GET'])
        def index() -> jsonify:
            """
            Index route.

            This endpoint returns a welcome message.

            ---
            responses:
                200:
                    description: Welcome message
                schema:
                    id: message
                    properties:
                        message:
                            type: string
            :return:
            """
            return jsonify({'message': 'Welcome to the API!, use /get_routes to see available routes'})

        @self.app.route('/about', methods=['GET'])
        def about() -> jsonify:
            """
            About route.

            This endpoint returns a simple message about the API.

            ---
            responses:
                200:
                    description: About message
                schema:
                    id: message
                    properties:
                        message:
                            type: string
            """
            return jsonify({'message': 'This is a simple API to demonstrate how to build an API with Flask'})

        @self.app.route('/get_routes', methods=['GET'])
        def get_routes() -> jsonify:
            """
            Get routes route.

            This endpoint returns all the available routes in the API.

            ---
            responses:
                200:
                    description: All available routes
                schema:
                    id: routes
                    properties:
                        routes:
                            type: array
                            items:
                                type: object
                                properties:
                                    route:
                                        type: string
                                    endpoint:
                                        type: string
                                    methods:
                                        type: array
                                        items:
                                            type: string
                                    arguments:
                                        type: array
                                        items:
                                            type: string
            :return:

            """
            return self._get_routes()

        @self.app.route('/get_data', methods=['GET'])
        def get_data() -> jsonify:
            """
            Get data route.

            This endpoint returns the data passed in the request.

            ---
            parameters:
                - name: data
                  in: query
                  type: string
                  required: true
                  description: The data to return
            responses:
                200:
                    description: The data passed in the request
                schema:
                    id: data
                    properties:
                        data:
                            type: string
                400:
                    description: No data passed in the request
                500:
                    description: Internal server error
            :return:
            """
            data = request.args.get('data')
            return self._get_data(data)

        @self.app.route('/upload_csv', methods=['POST'])
        def upload() -> jsonify:
            """
            Upload route.

            This endpoint uploads a file and loads the data into the AI logic.

            ---
            parameters:
                - name: file
                  in: formData
                  type: file
                  required: true
                  description: The file to upload
            responses:
                200:
                    description: File successfully uploaded
                400:
                    description: No file part in the request
                400:
                    description: No file selected for uploading
                500:
                    description: Internal server error
            :return:
            """
            return APILogic.upload(request)

        @self.app.route('/select_target', methods=['POST'])
        def select_target() -> jsonify:
            """
            Select target route.

            This endpoint selects the target column for the prediction.

            ---
            parameters:
                - name: target
                  in: formData
                  type: string
                  required: true
                  description: The target column
            responses:
                200:
                    description: Target successfully selected
                400:
                    description: Target not found in dataset
                500:
                    description: Internal server error
            :return:
            """
            return APILogic.select_target(request)

        @self.app.route('/predict', methods=['POST'])
        def predict() -> jsonify:
            """
            Predict route.

            This endpoint returns the predictions.

            ---
            responses:
                200:
                    description: The predictions
                400:
                    description: Error
                500:
                    description: Internal server error
            :return:
            """
            return APILogic.predict(request)

    def _get_routes(self) -> jsonify:
        """
        Returns all the available routes in the API.
        :return:
        """
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

    def _get_data(self, data) -> jsonify:
        """
        Returns the data passed in the request.
        :param data:
        :return:
        """
        return jsonify({'data': data})

    def run(self) -> None:
        """
        Runs the API.
        :return:
        """
        self.app.run("localhost", 4567, debug=True)
