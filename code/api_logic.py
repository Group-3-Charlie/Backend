from flask import jsonify, request

from code.ai_logic import AILogic


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
        if request.method == 'POST':
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected for uploading'}), 400

        if file and file.filename.endswith('.csv'):
            file.save(file.filename)
            return jsonify({'message': 'File successfully uploaded'}), 200
        else:
            return jsonify({'error': 'Only CSV files are allowed'}), 400

    @classmethod
    def select_target(cls, request):
        """
        Selects the target column from the dataset.
        :param request:
        :return:
        """
        target = request.form.get('target')
        try:
            AILogic.select_target(target)
            return jsonify({'message': 'Target successfully selected'}), 200
        except ValueError:
            return jsonify({'error': 'Target not found in dataset'}), 400

    @classmethod
    def predict(cls, request):
        """
        Predicts the results based on the selected target and the new data.
        :param request:
        :return:
        """
        try:
            predictions = AILogic.predict()
            return jsonify({'predictions': predictions}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
