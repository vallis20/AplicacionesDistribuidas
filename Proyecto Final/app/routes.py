from flask import Blueprint, request, jsonify
from app.services import FileService, get_status, set_status

main_bp = Blueprint('main', __name__)

@main_bp.route('/upload', methods=['POST'])
def upload_file():
    try:
        set_status("transfiriendo")
        uploaded_file = request.files['file']
        FileService.upload_file(uploaded_file)
        set_status("online")
        return jsonify({'message': 'File uploaded successfully'})
    except Exception as e:
        set_status("online")
        print(f"Error al cargar el archivo: {e}")
        return jsonify({'error': 'Error during file upload'})

@main_bp.route('/download/<file_id>', methods=['GET'])
def download_file(file_id):
    file_data = FileService.download_file(file_id)
    # Implementa lógica para enviar el archivo al cliente
    if file_path:
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'})


@main_bp.route('/status', methods=['GET'])
def get_current_status():
    status = get_status()
    return jsonify({'status': status})