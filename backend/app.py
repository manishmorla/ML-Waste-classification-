"""
Flask Backend API for Waste Classification
Serves the ML model for organic/non-organic waste classification
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
from pathlib import Path

from config import (
    FLASK_HOST, FLASK_PORT, FLASK_DEBUG,
    UPLOAD_FOLDER, ALLOWED_EXTENSIONS, MAX_FILE_SIZE,
    MODEL_PATH, CATEGORIES, CORS_ORIGINS, LOG_LEVEL
)
from model_loader import ModelLoader
from utils import (
    validate_image_file, preprocess_image, ensure_directory
)

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
# Enable CORS for frontend communication - allow all origins for file:// protocol
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# Configure Flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Ensure directories exist
ensure_directory(UPLOAD_FOLDER)
ensure_directory(MODEL_PATH.parent)

# Initialize model loader
model_loader = ModelLoader(MODEL_PATH)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model_loader.is_loaded,
        'service': 'Waste Classification API'
    }), 200


@app.route('/api/predict', methods=['POST'])
def predict():
    """Predict waste classification from uploaded image"""
    filepath = None
    try:
        # Check if file is present
        if 'image' not in request.files:
            return jsonify({
                'error': 'No image file provided',
                'message': 'Please upload an image file'
            }), 400
        
        file = request.files['image']
        
        # Validate file
        is_valid, error_message = validate_image_file(
            file, ALLOWED_EXTENSIONS, MAX_FILE_SIZE
        )
        
        if not is_valid:
            return jsonify({
                'error': 'Invalid file',
                'message': error_message
            }), 400
        
        # Check if model is loaded
        if not model_loader.is_loaded:
            return jsonify({
                'error': 'Model not loaded',
                'message': 'ML model is not available. Please train the model first.'
            }), 503
        
        # Save uploaded file temporarily
        from werkzeug.utils import secure_filename
        filename = secure_filename(file.filename)
        filepath = Path(app.config['UPLOAD_FOLDER']) / filename
        file.save(filepath)
        
        # Preprocess image
        processed_image = preprocess_image(str(filepath))
        
        # Make prediction
        prediction, probabilities = model_loader.predict(processed_image)
        
        # Get category
        category = CATEGORIES[prediction]
        confidence = float(probabilities[prediction]) * 100
        
        # Clean up uploaded file
        try:
            if filepath and filepath.exists():
                filepath.unlink()
        except Exception as e:
            logger.warning(f"Failed to delete temporary file: {e}")
        
        return jsonify({
            'success': True,
            'prediction': category,
            'confidence': round(confidence, 2),
            'probabilities': {
                'ORGANIC': round(float(probabilities[0]) * 100, 2),
                'NONORGANIC': round(float(probabilities[1]) * 100, 2)
            }
        }), 200
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        
        # Clean up on error
        try:
            if filepath and filepath.exists():
                filepath.unlink()
        except:
            pass
        
        return jsonify({
            'error': 'Prediction failed',
            'message': str(e)
        }), 500


@app.route('/api/model/status', methods=['GET'])
def model_status():
    """Get model status"""
    status = model_loader.get_status()
    return jsonify({
        **status,
        'categories': list(CATEGORIES.values())
    }), 200


if __name__ == '__main__':
    # Load model on startup
    logger.info("Starting Waste Classification API...")
    if model_loader.load():
        logger.info("Model loaded successfully")
    else:
        logger.warning("Model could not be loaded. API will run but predictions will fail.")
    
    # Run the Flask app
    app.run(debug=FLASK_DEBUG, host=FLASK_HOST, port=FLASK_PORT)
