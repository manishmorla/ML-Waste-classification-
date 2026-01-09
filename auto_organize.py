"""
Automatic Data Organization Script
Organizes images based on filename prefixes:
- O_* = ORGANIC
- R_* = NONORGANIC
"""

import os
import shutil
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'Data'
TEST_IMAGES_DIR = BASE_DIR / 'test images'
ORGANIC_DIR = DATA_DIR / 'ORGANIC'
NONORGANIC_DIR = DATA_DIR / 'NONORGANIC'

def create_folders():
    """Create the Data folder structure"""
    DATA_DIR.mkdir(exist_ok=True)
    ORGANIC_DIR.mkdir(exist_ok=True)
    NONORGANIC_DIR.mkdir(exist_ok=True)
    print("Created folder structure")

def organize_images():
    """Automatically organize images based on filename prefix"""
    print("=" * 60)
    print("Automatic Image Organization")
    print("=" * 60)
    print()
    
    # Create folders
    create_folders()
    
    if not TEST_IMAGES_DIR.exists():
        print(f"ERROR: Test images folder not found: {TEST_IMAGES_DIR}")
        return False
    
    # Get all image files
    image_files = list(TEST_IMAGES_DIR.glob('*.jpg')) + \
                  list(TEST_IMAGES_DIR.glob('*.png')) + \
                  list(TEST_IMAGES_DIR.glob('*.jpeg')) + \
                  list(TEST_IMAGES_DIR.glob('*.bmp'))
    
    if not image_files:
        print("ERROR: No images found in test images folder!")
        return False
    
    print(f"Found {len(image_files)} images to organize")
    print()
    
    organic_count = 0
    nonorganic_count = 0
    unknown_count = 0
    
    # Organize images
    for image_path in image_files:
        filename = image_path.name
        
        # Check prefix
        if filename.startswith('O_'):
            # Organic
            dest = ORGANIC_DIR / filename
            shutil.copy2(image_path, dest)
            organic_count += 1
        elif filename.startswith('R_'):
            # Non-Organic (Recyclable)
            dest = NONORGANIC_DIR / filename
            shutil.copy2(image_path, dest)
            nonorganic_count += 1
        else:
            # Unknown prefix - skip or ask user
            print(f"WARNING: Unknown prefix for: {filename}")
            unknown_count += 1
    
    # Summary
    print("=" * 60)
    print("Organization Complete!")
    print("=" * 60)
    print(f"ORGANIC: {organic_count} images")
    print(f"NONORGANIC: {nonorganic_count} images")
    if unknown_count > 0:
        print(f"WARNING: {unknown_count} images with unknown prefix (not organized)")
    print()
    print(f"Total organized: {organic_count + nonorganic_count} images")
    print()
    
    if organic_count > 0 and nonorganic_count > 0:
        print("SUCCESS: Data is ready for training!")
        print()
        print("Next step: Run training")
        print("  python backend/train_model.py")
        return True
    else:
        print("WARNING: Need images in both categories for training!")
        return False

if __name__ == '__main__':
    try:
        success = organize_images()
        if success:
            print("\nAll done! You can now train your model.")
        else:
            print("\nOrganization incomplete. Please check the output above.")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
