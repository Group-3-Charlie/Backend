from flask import jsonify, request, send_file

from ai_logic import AILogic


class APILogic:
    """
    API Logic class to define the logic for the API.
    """

    @classmethod
    def upload(cls, request: request) -> jsonify:
        """
        Uploads a file to the server.
        :param request:
        :return:
        """
        if request.method != 'POST':
            return jsonify({'error': 'Only POST requests are allowed'}).headers.add('Access-Control-Allow-Origin',
                                                                                    '*'), 400

        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}).headers.add('Access-Control-Allow-Origin',
                                                                                 '*'), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected for uploading'}).headers.add('Access-Control-Allow-Origin',
                                                                                    '*'), 400

        if file and file.filename.endswith('.csv'):
            file.save(file.filename)
            AILogic.load_data(file.filename)
            response = jsonify({'message': 'File successfully uploaded'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 200
        else:
            return jsonify({'error': 'Only CSV files are allowed'}).headers.add('Access-Control-Allow-Origin', '*'), 400

    @classmethod
    def select_target(cls, request):
        """
        Selects the target column from the dataset.
        :param request:
        :return:
        """

        if request.method != 'POST':
            return jsonify({'error': 'Only POST requests are allowed'}).headers.add('Access-Control-Allow-Origin',
                                                                                    '*'), 400

        target = request.get_data(as_text=True)

        try:
            AILogic.select_target(target)
            response = jsonify({'message': 'Target successfully selected'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 200
        except ValueError:
            response = jsonify({'error': 'Target not found in dataset'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 400

    @classmethod
    def predict(cls, request):
        """
        Predicts the results based on the selected target and the new data.
        :param request:
        :return:
        """
        if request.method != 'POST':
            return jsonify({'error': 'Only POST requests are allowed'}).headers.add('Access-Control-Allow-Origin',
                                                                                    '*'), 400

        if AILogic.target is None:
            return jsonify({'error': 'No target selected'}).headers.add('Access-Control-Allow-Origin', '*'), 400

        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}).headers.add('Access-Control-Allow-Origin',
                                                                                 '*'), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected for uploading'}).headers.add('Access-Control-Allow-Origin',
                                                                                    '*'), 400

        if file and file.filename.endswith('.csv'):
            file.save(file.filename)
            AILogic.predict(file.filename)
            response = jsonify({'predictions': "Message test"})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 200

        else:
            return jsonify({'error': 'Only CSV files are allowed'}).headers.add('Access-Control-Allow-Origin', '*'), 400

    @classmethod
    def get_predictions(cls):
        """
        Return the predictions as a CSV file.
        :return:
        """
        predictions = "predictions.csv"
        response = send_file(predictions, as_attachment=True)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200

    @classmethod
    def get_columns(cls):
        """
        Return the columns of the dataset.
        :return:
        """
        print(AILogic.df.columns)
        columns = AILogic.df.columns.values.tolist()
        response = jsonify({'columns': columns})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200

    @classmethod
    def get_columns_without_target(cls):
        """
        Return the columns of the dataset without the target column.
        :return:
        """
        columns = AILogic.df.columns.values.tolist()
        columns.remove(AILogic.target)
        response = jsonify({'columns': columns})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
