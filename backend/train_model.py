"""
Train the Waste Classification Model
This script trains a Random Forest classifier on waste images
"""

import os
import numpy as np
import pickle
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from skimage.io import imread
from skimage.transform import resize
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'Data'
MODEL_DIR = BASE_DIR / 'backend' / 'models'
MODEL_PATH = MODEL_DIR / 'RF_Classifier.pkl'

CATEGORIES = ['ORGANIC', 'NONORGANIC']


def load_and_preprocess_images(data_dir):
    """
    Load and preprocess images from data directory
    
    Args:
        data_dir: Path to data directory containing category folders
        
    Returns:
        tuple: (flat_data, target) arrays
    """
    flat_data_arr = []
    target_arr = []
    
    data_path = Path(data_dir)
    
    # Check if data directory exists
    if not data_path.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")
    
    logger.info(f"Loading images from: {data_path}")
    
    # Process each category
    for category in CATEGORIES:
        category_path = data_path / category
        
        if not category_path.exists():
            logger.warning(f"Category folder not found: {category_path}")
            continue
        
        logger.info(f"Processing category: {category}")
        image_files = list(category_path.glob('*.jpg')) + list(category_path.glob('*.png')) + \
                      list(category_path.glob('*.jpeg')) + list(category_path.glob('*.bmp'))
        
        if len(image_files) == 0:
            logger.warning(f"No images found in {category_path}")
            continue
        
        for img_path in image_files:
            try:
                # Read and resize image
                img = imread(img_path)
                img_resized = resize(img, (150, 150, 3))
                
                # Flatten image
                flat_data_arr.append(img_resized.flatten())
                target_arr.append(CATEGORIES.index(category))
                
            except Exception as e:
                logger.error(f"Error processing {img_path}: {e}")
                continue
        
        logger.info(f"Loaded {len([t for t in target_arr if t == CATEGORIES.index(category)])} images for {category}")
    
    if len(flat_data_arr) == 0:
        raise ValueError("No images were loaded! Please check your Data directory structure.")
    
    return np.array(flat_data_arr), np.array(target_arr)


def train_model(data_dir=None):
    """
    Train the Random Forest classifier
    
    Args:
        data_dir: Path to data directory (default: project_root/Data)
    """
    if data_dir is None:
        data_dir = DATA_DIR
    
    logger.info("=" * 60)
    logger.info("Starting Model Training")
    logger.info("=" * 60)
    
    # Load and preprocess images
    logger.info("Step 1: Loading and preprocessing images...")
    try:
        flat_data, target = load_and_preprocess_images(data_dir)
        logger.info(f"Loaded {len(flat_data)} images total")
        logger.info(f"Image shape: {flat_data[0].shape}")
    except Exception as e:
        logger.error(f"Failed to load images: {e}")
        logger.error("\nPlease ensure your Data directory structure is:")
        logger.error("Data/")
        logger.error("  ├── ORGANIC/")
        logger.error("  │   ├── image1.jpg")
        logger.error("  │   └── image2.jpg")
        logger.error("  └── NONORGANIC/")
        logger.error("      ├── image1.jpg")
        logger.error("      └── image2.jpg")
        return False
    
    # Split data
    logger.info("\nStep 2: Splitting data into train/test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        flat_data, target, test_size=0.30, random_state=77
    )
    logger.info(f"Training samples: {len(X_train)}")
    logger.info(f"Test samples: {len(X_test)}")
    
    # Train model
    logger.info("\nStep 3: Training Random Forest classifier...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    logger.info("Training completed!")
    
    # Evaluate model
    logger.info("\nStep 4: Evaluating model...")
    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100
    logger.info(f"Accuracy: {accuracy:.2f}%")
    
    # Classification report
    logger.info("\nClassification Report:")
    logger.info("\n" + classification_report(y_test, y_pred, target_names=CATEGORIES))
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    logger.info("\nConfusion Matrix:")
    logger.info(f"\n{cm}")
    
    # Save model
    logger.info("\nStep 5: Saving model...")
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(rf, f)
    
    logger.info(f"Model saved to: {MODEL_PATH}")
    logger.info("\n" + "=" * 60)
    logger.info("Training completed successfully!")
    logger.info("=" * 60)
    
    return True


if __name__ == '__main__':
    import sys
    
    # Allow custom data directory
    data_dir = sys.argv[1] if len(sys.argv) > 1 else None
    
    try:
        success = train_model(data_dir)
        if success:
            print("\n✅ Model training completed! You can now run the backend server.")
        else:
            print("\n❌ Model training failed. Please check the error messages above.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nTraining interrupted by user.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"\nUnexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
