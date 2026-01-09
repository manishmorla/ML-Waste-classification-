"""
Helper script to organize training data
This script helps you set up the Data folder structure and organize images
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

def create_folder_structure():
    """Create the Data folder structure"""
    print("=" * 60)
    print("Creating Data Folder Structure")
    print("=" * 60)
    
    # Create directories
    DATA_DIR.mkdir(exist_ok=True)
    ORGANIC_DIR.mkdir(exist_ok=True)
    NONORGANIC_DIR.mkdir(exist_ok=True)
    
    print(f"✅ Created: {DATA_DIR}")
    print(f"✅ Created: {ORGANIC_DIR}")
    print(f"✅ Created: {NONORGANIC_DIR}")
    print()

def list_test_images():
    """List all test images"""
    if not TEST_IMAGES_DIR.exists():
        print(f"❌ Test images folder not found: {TEST_IMAGES_DIR}")
        return []
    
    image_files = list(TEST_IMAGES_DIR.glob('*.jpg')) + \
                  list(TEST_IMAGES_DIR.glob('*.png')) + \
                  list(TEST_IMAGES_DIR.glob('*.jpeg')) + \
                  list(TEST_IMAGES_DIR.glob('*.bmp'))
    
    return sorted(image_files)

def copy_image_to_category(source, destination_dir, filename):
    """Copy an image to a category folder"""
    destination = destination_dir / filename
    try:
        shutil.copy2(source, destination)
        return True
    except Exception as e:
        print(f"Error copying {filename}: {e}")
        return False

def interactive_organize():
    """Interactive mode to organize images"""
    create_folder_structure()
    
    images = list_test_images()
    
    if not images:
        print("No images found in test images folder!")
        return
    
    print(f"Found {len(images)} images to organize")
    print()
    print("Instructions:")
    print("- Type 'o' or '1' for ORGANIC")
    print("- Type 'n' or '2' for NONORGANIC")
    print("- Type 's' to skip this image")
    print("- Type 'q' to quit")
    print()
    
    organized = {'organic': 0, 'nonorganic': 0, 'skipped': 0}
    
    for i, image_path in enumerate(images, 1):
        print(f"\n[{i}/{len(images)}] Image: {image_path.name}")
        
        while True:
            choice = input("Category (o/n/s/q): ").strip().lower()
            
            if choice in ['q', 'quit']:
                print("\nOrganization stopped by user.")
                break
            elif choice in ['o', '1', 'organic']:
                if copy_image_to_category(image_path, ORGANIC_DIR, image_path.name):
                    organized['organic'] += 1
                    print(f"✅ Copied to ORGANIC folder")
                break
            elif choice in ['n', '2', 'nonorganic', 'non-organic']:
                if copy_image_to_category(image_path, NONORGANIC_DIR, image_path.name):
                    organized['nonorganic'] += 1
                    print(f"✅ Copied to NONORGANIC folder")
                break
            elif choice in ['s', 'skip']:
                organized['skipped'] += 1
                print("⏭️  Skipped")
                break
            else:
                print("Invalid choice. Please enter 'o', 'n', 's', or 'q'")
        
        if choice in ['q', 'quit']:
            break
    
    # Summary
    print("\n" + "=" * 60)
    print("Organization Summary")
    print("=" * 60)
    print(f"✅ ORGANIC: {organized['organic']} images")
    print(f"✅ NONORGANIC: {organized['nonorganic']} images")
    print(f"⏭️  Skipped: {organized['skipped']} images")
    print()
    print(f"Total organized: {organized['organic'] + organized['nonorganic']} images")
    print()
    
    if organized['organic'] + organized['nonorganic'] > 0:
        print("✅ Data folder is ready for training!")
        print("Run: python backend/train_model.py")
    else:
        print("⚠️  No images were organized. Please try again.")

def auto_setup_only():
    """Just create the folder structure without organizing"""
    create_folder_structure()
    print()
    print("✅ Folder structure created!")
    print()
    print("Next steps:")
    print("1. Manually copy images from 'test images' folder")
    print("2. Organize them into:")
    print(f"   - {ORGANIC_DIR}")
    print(f"   - {NONORGANIC_DIR}")
    print("3. Run: python backend/train_model.py")
    print()
    print("Or run this script in interactive mode:")
    print("   python organize_data.py --interactive")

if __name__ == '__main__':
    import sys
    
    if '--interactive' in sys.argv or '-i' in sys.argv:
        interactive_organize()
    else:
        print("=" * 60)
        print("Data Organization Helper")
        print("=" * 60)
        print()
        print("This script will help you organize your training data.")
        print()
        print("Choose an option:")
        print("1. Interactive mode (recommended) - Organize images one by one")
        print("2. Just create folders - You'll organize manually")
        print()
        
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == '1':
            interactive_organize()
        else:
            auto_setup_only()
