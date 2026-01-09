"""
Utility functions for image preprocessing and validation
"""

import os
import logging
from pathlib import Path
from werkzeug.utils import secure_filename
from skimage.io import imread
from skimage.transform import resize
import numpy as np

logger = logging.getLogger(__name__)


def allowed_file(filename, allowed_extensions):
    """
    Check if file extension is allowed
    
    Args:
        filename: Name of the file
        allowed_extensions: Set of allowed file extensions
        
    Returns:
        bool: True if file extension is allowed
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


def preprocess_image(image_path):
    """
    Preprocess image for model prediction
    
    Args:
        image_path: Path to the image file
        
    Returns:
        numpy.ndarray: Preprocessed image array ready for prediction
        
    Raises:
        Exception: If image processing fails
    """
    try:
        # Read image
        img = imread(image_path)
        
        # Resize to 150x150x3 (as per training)
        img_resized = resize(img, (150, 150, 3))
        
        # Flatten the image
        img_flattened = img_resized.flatten()
        
        return img_flattened.reshape(1, -1)
    except Exception as e:
        logger.error(f"Error preprocessing image: {str(e)}")
        raise


def validate_image_file(file, allowed_extensions, max_size):
    """
    Validate uploaded image file
    
    Args:
        file: File object from request
        allowed_extensions: Set of allowed file extensions
        max_size: Maximum file size in bytes
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not file or file.filename == '':
        return False, 'No file selected'
    
    if not allowed_file(file.filename, allowed_extensions):
        return False, f'Invalid file type. Allowed types: {", ".join(allowed_extensions)}'
    
    # Check file size
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)  # Reset file pointer
    
    if file_size > max_size:
        return False, f'File size too large. Maximum size: {max_size / (1024*1024):.1f}MB'
    
    return True, None


def ensure_directory(path):
    """
    Ensure directory exists, create if it doesn't
    
    Args:
        path: Path to directory
    """
    Path(path).mkdir(parents=True, exist_ok=True)
