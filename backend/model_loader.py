"""
Model loading and management utilities
"""

import os
import pickle
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ModelLoader:
    """Handles loading and management of ML models"""
    
    def __init__(self, model_path):
        """
        Initialize ModelLoader
        
        Args:
            model_path: Path to the model file
        """
        self.model_path = Path(model_path)
        self.model = None
        self.is_loaded = False
    
    def load(self):
        """
        Load the pre-trained model
        
        Returns:
            bool: True if model loaded successfully, False otherwise
        """
        try:
            if not self.model_path.exists():
                logger.warning(f"Model file not found at {self.model_path}")
                return False
            
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            
            self.is_loaded = True
            logger.info(f"Model loaded successfully from {self.model_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            self.is_loaded = False
            return False
    
    def predict(self, image_data):
        """
        Make prediction on image data
        
        Args:
            image_data: Preprocessed image data
            
        Returns:
            tuple: (prediction, probabilities)
        """
        if not self.is_loaded or self.model is None:
            raise ValueError("Model is not loaded")
        
        prediction = self.model.predict(image_data)[0]
        probabilities = self.model.predict_proba(image_data)[0]
        
        return prediction, probabilities
    
    def get_status(self):
        """
        Get model status information
        
        Returns:
            dict: Model status information
        """
        return {
            'is_loaded': self.is_loaded,
            'model_path': str(self.model_path),
            'model_exists': self.model_path.exists()
        }
