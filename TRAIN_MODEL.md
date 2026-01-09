# How to Train the Model

## Quick Answer

The model file (`RF_Classifier.pkl`) is missing. You need to train it first.

## Option 1: Train Using Python Script (Recommended)

### Step 1: Prepare Your Data

Your training images should be organized like this:

```
ML-Waste-classification-/
├── Data/
│   ├── ORGANIC/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   └── NONORGANIC/
│       ├── image1.jpg
│       ├── image2.jpg
│       └── ...
```

### Step 2: Run Training Script

```bash
python backend/train_model.py
```

The script will:
- ✅ Load images from `Data/` folder
- ✅ Preprocess them (resize to 150x150x3)
- ✅ Train Random Forest classifier
- ✅ Save model to `backend/models/RF_Classifier.pkl`
- ✅ Show accuracy and evaluation metrics

### Step 3: Verify Model Created

```bash
# Check if model exists
dir backend\models\RF_Classifier.pkl
```

## Option 2: Train Using Jupyter Notebook

1. **Open Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Open:** `waste classification organic and non organic-code.ipynb`

3. **Run all cells** - This will train and save the model

4. **Move the model file:**
   - The notebook saves `RF_Classifier.pkl` in the project root
   - Move it to: `backend/models/RF_Classifier.pkl`

## Option 3: Use Custom Data Directory

If your data is in a different location:

```bash
python backend/train_model.py "path/to/your/Data"
```

## Data Requirements

- **Format:** Images should be in JPG, PNG, JPEG, or BMP format
- **Structure:** Two folders named `ORGANIC` and `NONORGANIC`
- **Minimum:** At least 10-20 images per category (more is better)
- **Size:** Any size (will be resized to 150x150 during training)

## Training Output

You'll see:
```
Starting Model Training
============================================================
Step 1: Loading and preprocessing images...
Loaded 200 images total

Step 2: Splitting data into train/test sets...
Training samples: 140
Test samples: 60

Step 3: Training Random Forest classifier...
Training completed!

Step 4: Evaluating model...
Accuracy: 92.50%

Step 5: Saving model...
Model saved to: backend/models/RF_Classifier.pkl
============================================================
Training completed successfully!
```

## After Training

Once the model is trained:

1. **Start the backend:**
   ```bash
   python backend/app.py
   ```

2. **The model will load automatically!**

3. **Test it:**
   - Open frontend
   - Upload an image
   - Get classification results!

## Troubleshooting

### "Data directory not found"
- ✅ Create `Data/` folder in project root
- ✅ Add `ORGANIC/` and `NONORGANIC/` subfolders
- ✅ Add training images to each folder

### "No images found"
- ✅ Check image file extensions (.jpg, .png, .jpeg, .bmp)
- ✅ Verify images are in the correct folders
- ✅ Check file permissions

### "Training takes too long"
- ✅ Normal for large datasets (100+ images)
- ✅ Be patient, it will complete
- ✅ You can reduce `n_estimators` in the script for faster training

### "Low accuracy"
- ✅ Add more training images
- ✅ Ensure images are clear and representative
- ✅ Check that images are correctly categorized

## Quick Start (If You Have Data Ready)

```bash
# 1. Ensure Data folder exists with ORGANIC and NONORGANIC subfolders
# 2. Run training
python backend/train_model.py

# 3. Start backend
python backend/app.py

# 4. Open frontend and test!
```

## Need Help?

- Check your `Data/` folder structure
- Verify images are in correct format
- Check the training script output for errors
- See `backend/train_model.py` for code details
