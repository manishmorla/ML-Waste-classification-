# How to Run the Waste Classification Program

This guide will walk you through executing the program step by step.

## Prerequisites

Before running, ensure you have:
- ✅ Python 3.8 or higher installed
- ✅ pip (Python package manager)
- ✅ A trained model file (`RF_Classifier.pkl`) in `backend/models/` folder
- ✅ A modern web browser (Chrome, Firefox, Edge, Safari)

## Step-by-Step Execution

### Step 1: Open Terminal/Command Prompt

**Windows:**
- Press `Win + R`, type `cmd` or `powershell`, press Enter
- Or search for "Command Prompt" or "PowerShell" in Start Menu

**macOS/Linux:**
- Press `Cmd + Space` (Mac) or `Ctrl + Alt + T` (Linux)
- Type "Terminal" and press Enter

### Step 2: Navigate to Project Directory

```bash
cd "C:\Users\91703\OneDrive\Desktop\github repositories\ML-Waste-classification-"
```

> **Note**: Adjust the path if your project is in a different location

### Step 3: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command prompt.

### Step 4: Install Python Dependencies

```bash
pip install -r backend/requirements.txt
```

Wait for all packages to install. This may take a few minutes.

### Step 5: Verify Model File Exists

Check if your model file is in the correct location:

```bash
# Windows
dir backend\models\RF_Classifier.pkl

# macOS/Linux
ls backend/models/RF_Classifier.pkl
```

If the file doesn't exist:
- Train the model using the Jupyter notebook: `waste classification organic and non organic-code.ipynb`
- Or download/obtain a pre-trained model file

### Step 6: Start the Backend Server

**Keep this terminal window open!**

```bash
python backend/app.py
```

You should see output like:
```
Starting Waste Classification API...
Model loaded successfully
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

✅ **Backend is now running!** Keep this terminal open.

### Step 7: Open the Frontend

You have **two options**:

#### Option A: Direct File (Easiest)

1. Open File Explorer (Windows) or Finder (Mac)
2. Navigate to: `ML-Waste-classification-\frontend\`
3. Double-click `index.html`
4. It will open in your default browser

#### Option B: Local Server (Recommended for Development)

**Open a NEW terminal window** (keep the backend terminal running):

```bash
# Navigate to frontend folder
cd "C:\Users\91703\OneDrive\Desktop\github repositories\ML-Waste-classification-\frontend"

# Start local server
python -m http.server 8000
```

Then open your browser and go to: `http://localhost:8000`

### Step 8: Use the Application

1. **Upload an Image:**
   - Click the upload area or drag & drop an image
   - Supported formats: JPG, PNG, GIF, BMP
   - Max size: 16MB

2. **Classify:**
   - Click the "Classify Waste" button
   - Wait a few seconds for processing

3. **View Results:**
   - See if it's ORGANIC or NON-ORGANIC
   - View confidence percentages
   - Try another image!

## Visual Guide

```
Terminal 1 (Backend)          Terminal 2 (Frontend)          Browser
─────────────────────          ─────────────────────          ─────────
$ python backend/app.py        $ cd frontend                   http://localhost:8000
                              $ python -m http.server 8000    or
* Running on :5000                                              file:///.../index.html
                                                               [Upload Image]
                                                               [Classify]
                                                               [See Results]
```

## Testing the API Directly

You can also test the backend API directly using curl or Postman:

### Health Check
```bash
curl http://localhost:5000/api/health
```

### Test Classification
```bash
curl -X POST -F "image=@test images/your_image.jpg" http://localhost:5000/api/predict
```

## Troubleshooting

### ❌ "Module not found" error
**Solution:** Make sure you activated the virtual environment and installed dependencies:
```bash
pip install -r backend/requirements.txt
```

### ❌ "Model not found" error
**Solution:** Ensure `RF_Classifier.pkl` exists in `backend/models/` folder

### ❌ "Port 5000 already in use"
**Solution:** Change the port in `backend/config.py`:
```python
FLASK_PORT = 5001  # Change to any available port
```

### ❌ Frontend can't connect to backend
**Solution:** 
- Verify backend is running (check terminal 1)
- Check if URL in `frontend/js/middleware.js` matches your backend port
- Ensure CORS is enabled (it should be by default)

### ❌ "Permission denied" (macOS/Linux)
**Solution:** 
```bash
chmod +x setup.sh
```

## Quick Commands Reference

```bash
# Start backend
python backend/app.py

# Start frontend server (optional)
cd frontend
python -m http.server 8000

# Install dependencies
pip install -r backend/requirements.txt

# Check Python version
python --version

# Check if backend is running
curl http://localhost:5000/api/health
```

## Expected Output

### Backend Terminal Output:
```
INFO - Starting Waste Classification API...
INFO - Model loaded successfully from backend/models/RF_Classifier.pkl
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### Frontend Browser:
- Beautiful dark-themed interface
- Upload area for images
- Classification results with confidence scores
- Smooth animations

### API Response Example:
```json
{
  "success": true,
  "prediction": "ORGANIC",
  "confidence": 95.5,
  "probabilities": {
    "ORGANIC": 95.5,
    "NONORGANIC": 4.5
  }
}
```

## Stopping the Program

1. **Stop Backend:** In the backend terminal, press `Ctrl + C`
2. **Stop Frontend Server:** In the frontend terminal, press `Ctrl + C`
3. **Close Browser:** Simply close the browser tab/window

## Next Steps

- Try different waste images from the `test images/` folder
- Experiment with various image types
- Check the API documentation in `README.md`
- Explore the code structure in `ARCHITECTURE.md`

---

**Need Help?** Check the other documentation files or open an issue on GitHub!
