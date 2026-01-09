# 🚀 Quick Model Training Guide

## The Problem
Your model file (`RF_Classifier.pkl`) is missing. You need to train it first!

## Solution: Train the Model

### Step 1: Check if you have training data

Your project needs a `Data` folder with this structure:

```
Data/
├── ORGANIC/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ... (more organic waste images)
└── NONORGANIC/
    ├── image1.jpg
    ├── image2.jpg
    └── ... (more non-organic waste images)
```

### Step 2: Train the Model

**If you have the Data folder ready:**

```bash
python backend/train_model.py
```

**If your data is in a different location:**

```bash
python backend/train_model.py "path/to/your/Data"
```

### Step 3: Wait for Training to Complete

You'll see output like:
```
Starting Model Training
Step 1: Loading and preprocessing images...
Loaded 200 images total
Step 2: Splitting data...
Step 3: Training Random Forest classifier...
Step 4: Evaluating model...
Accuracy: 92.50%
Step 5: Saving model...
Model saved to: backend/models/RF_Classifier.pkl
✅ Training completed successfully!
```

### Step 4: Verify Model Created

```bash
dir backend\models\RF_Classifier.pkl
```

If the file exists, you're good to go!

### Step 5: Start the Backend

```bash
python backend/app.py
```

Now the model will load and you can use the application!

## Don't Have Training Data?

### Option A: Use Test Images (Quick Test)

If you want to quickly test, you can temporarily use your `test images` folder:

1. Create a `Data` folder
2. Create `ORGANIC` and `NONORGANIC` subfolders
3. Manually organize some test images into these folders
4. Run training

### Option B: Download a Dataset

You can find waste classification datasets online:
- Kaggle
- Google Dataset Search
- Research paper datasets

### Option C: Use Your Own Images

1. Collect images of organic waste (food, leaves, etc.)
2. Collect images of non-organic waste (plastic, metal, etc.)
3. Organize them into `Data/ORGANIC/` and `Data/NONORGANIC/` folders
4. Run training

## Minimum Requirements

- **At least 20-30 images per category** (more is better!)
- **Clear, representative images**
- **JPG, PNG, JPEG, or BMP format**

## After Training

Once training completes:

1. ✅ Model file will be in `backend/models/RF_Classifier.pkl`
2. ✅ Start backend: `python backend/app.py`
3. ✅ Open frontend and test!

## Troubleshooting

**"Data directory not found"**
→ Create `Data/` folder with `ORGANIC/` and `NONORGANIC/` subfolders

**"No images found"**
→ Check that images are in JPG/PNG format and in the correct folders

**"Training takes too long"**
→ Normal for large datasets. Be patient!

**"Low accuracy"**
→ Add more training images, ensure they're clear and correctly categorized

---

**Ready to train?** Run: `python backend/train_model.py`
