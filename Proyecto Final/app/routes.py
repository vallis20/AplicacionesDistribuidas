from flask import Blueprint, request, jsonify
from app.services import FileService

main_bp = Blueprint('main', __name__)

@main_bp.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    FileService.upload_file(uploaded_file)
    return jsonify({'message': 'File uploaded successfully'})

@main_bp.route('/download/<file_id>', methods=['GET'])
def download_file(file_id):
    file_data = FileService.download_file(file_id)
    # Implementa lógica para enviar el archivo al cliente