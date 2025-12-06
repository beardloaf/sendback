"""
SendBack API - Return Automation Backend
Flask API for processing order confirmations and providing return information
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from datetime import datetime

from order_parser import parse_order_confirmation, OrderParser
from merchant_database import find_merchant, get_all_merchants, MERCHANT_DATABASE

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'SendBack API'})


@app.route('/api/merchants', methods=['GET'])
def list_merchants():
    """List all supported merchants"""
    merchants = []
    for key, info in MERCHANT_DATABASE.items():
        merchants.append({
            'key': key,
            'name': info.merchant_name,
            'return_window_days': info.return_window_days,
            'free_label': info.free_return_label,
            'portal_url': info.return_portal_url
        })
    return jsonify({'merchants': merchants})


@app.route('/api/merchant/<merchant_key>', methods=['GET'])
def get_merchant(merchant_key):
    """Get return information for specific merchant"""
    info = find_merchant(merchant_key)

    if not info:
        return jsonify({'error': 'Merchant not found'}), 404

    return jsonify({
        'merchant': info.merchant_name,
        'return_address': info.return_address,
        'return_portal_url': info.return_portal_url,
        'return_window_days': info.return_window_days,
        'free_return_label': info.free_return_label,
        'instructions': info.instructions,
        'customer_service': info.customer_service
    })


@app.route('/api/parse', methods=['POST'])
def parse_order():
    """Parse uploaded order confirmation"""

    # Check if file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    # Save file
    filename = secure_filename(file.filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_{filename}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        # Parse the order confirmation
        parsed_order = parse_order_confirmation(filepath)

        # Get merchant return info
        merchant_info = None
        if parsed_order.merchant_name:
            merchant_info = find_merchant(parsed_order.merchant_name)

        # Build response
        response = {
            'parsed': {
                'merchant': parsed_order.merchant_name,
                'order_number': parsed_order.order_number,
                'order_date': parsed_order.order_date.isoformat() if parsed_order.order_date else None,
                'return_by_date': parsed_order.return_by_date.isoformat() if parsed_order.return_by_date else None,
                'items': parsed_order.items,
                'total': parsed_order.total_amount,
                'extracted_return_address': parsed_order.extracted_return_address
            }
        }

        # Add merchant return info if found
        if merchant_info:
            response['merchant_info'] = {
                'name': merchant_info.merchant_name,
                'return_address': merchant_info.return_address,
                'return_portal_url': merchant_info.return_portal_url,
                'return_window_days': merchant_info.return_window_days,
                'free_return_label': merchant_info.free_return_label,
                'instructions': merchant_info.instructions,
                'customer_service': merchant_info.customer_service
            }

        # Calculate days remaining
        if parsed_order.return_by_date:
            days_remaining = (parsed_order.return_by_date - datetime.now()).days
            response['days_remaining'] = max(0, days_remaining)

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': f'Failed to parse order: {str(e)}'}), 500

    finally:
        # Clean up uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)


@app.route('/api/parse/text', methods=['POST'])
def parse_text():
    """Parse text content directly (for copy-paste)"""

    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']

    try:
        # Parse the text
        parser = OrderParser()
        parsed_order = parser.parse_text(text)

        # Get merchant return info
        merchant_info = None
        if parsed_order.merchant_name:
            merchant_info = find_merchant(parsed_order.merchant_name)

        # Build response
        response = {
            'parsed': {
                'merchant': parsed_order.merchant_name,
                'order_number': parsed_order.order_number,
                'order_date': parsed_order.order_date.isoformat() if parsed_order.order_date else None,
                'return_by_date': parsed_order.return_by_date.isoformat() if parsed_order.return_date else None,
                'items': parsed_order.items,
                'total': parsed_order.total_amount,
                'extracted_return_address': parsed_order.extracted_return_address
            }
        }

        # Add merchant return info if found
        if merchant_info:
            response['merchant_info'] = {
                'name': merchant_info.merchant_name,
                'return_address': merchant_info.return_address,
                'return_portal_url': merchant_info.return_portal_url,
                'return_window_days': merchant_info.return_window_days,
                'free_return_label': merchant_info.free_return_label,
                'instructions': merchant_info.instructions,
                'customer_service': merchant_info.customer_service
            }

        # Calculate days remaining
        if parsed_order.return_by_date:
            days_remaining = (parsed_order.return_by_date - datetime.now()).days
            response['days_remaining'] = max(0, days_remaining)

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': f'Failed to parse text: {str(e)}'}), 500


@app.route('/api/label-instructions/<merchant_key>', methods=['GET'])
def get_label_instructions(merchant_key):
    """Get step-by-step instructions for obtaining a return label"""

    info = find_merchant(merchant_key)

    if not info:
        return jsonify({'error': 'Merchant not found'}), 404

    instructions = {
        'merchant': info.merchant_name,
        'free_label_available': info.free_return_label,
        'steps': []
    }

    # Add specific steps based on merchant
    if info.return_portal_url:
        instructions['steps'].append({
            'step': 1,
            'action': 'Visit Return Portal',
            'url': info.return_portal_url,
            'description': f'Go to {info.merchant_name}\'s official return portal'
        })
        instructions['steps'].append({
            'step': 2,
            'action': 'Log In',
            'description': 'Sign in to your account with your order details'
        })
        instructions['steps'].append({
            'step': 3,
            'action': 'Select Order',
            'description': 'Find your order in the order history'
        })
        instructions['steps'].append({
            'step': 4,
            'action': 'Request Return',
            'description': 'Click "Return Items" and select items to return'
        })

        if info.free_return_label:
            instructions['steps'].append({
                'step': 5,
                'action': 'Print Label',
                'description': 'Download and print the prepaid return label'
            })
        else:
            instructions['steps'].append({
                'step': 5,
                'action': 'Check Label Status',
                'description': 'Check if seller provides free return label (varies by seller)'
            })

        instructions['steps'].append({
            'step': 6,
            'action': 'Pack & Ship',
            'description': 'Pack item securely, attach label, and drop off at carrier location'
        })

    else:
        instructions['steps'].append({
            'step': 1,
            'action': 'Contact Customer Service',
            'phone': info.customer_service,
            'description': 'Call customer service to initiate return'
        })

    instructions['full_instructions'] = info.instructions
    instructions['customer_service'] = info.customer_service
    instructions['return_address'] = info.return_address

    return jsonify(instructions)


if __name__ == '__main__':
    print("=" * 60)
    print("SendBack API - Ethical Return Automation")
    print("=" * 60)
    print(f"Supported merchants: {len(MERCHANT_DATABASE)}")
    print(f"Upload folder: {UPLOAD_FOLDER}")
    print("Starting server on http://localhost:5000")
    print("=" * 60)

    app.run(debug=True, host='0.0.0.0', port=5000)
