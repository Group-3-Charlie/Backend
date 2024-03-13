import os

from flask import jsonify
from werkzeug.utils import secure_filename

from ai_logic import AILogic


class APILogic:

    @classmethod
    def upload(cls, request):
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected for uploading'}), 400
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join('../uploads', filename)
            file.save(filepath)
            AILogic.load_data(filepath)
            return jsonify({'message': 'File successfully uploaded'}), 200

    @classmethod
    def select_target(cls, request):
        target = request.form.get('target')
        try:
            AILogic.select_target(target)
            return jsonify({'message': 'Target successfully selected'}), 200
        except ValueError:
            return jsonify({'error': 'Target not found in dataset'}), 400

    @classmethod
    def predict(cls, request):
        try:
            predictions = AILogic.predict()
            return jsonify({'predictions': predictions}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
