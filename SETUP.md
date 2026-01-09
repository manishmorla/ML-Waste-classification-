# Setup Guide

This guide will help you set up the Waste Classification AI project on your local machine.

## Quick Start

### Option 1: Automated Setup (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ML-Waste-classification-.git
   cd ML-Waste-classification-
   ```

2. **Run setup script**
   ```bash
   # Windows
   setup.bat
   
   # macOS/Linux
   chmod +x setup.sh
   ./setup.sh
   ```

### Option 2: Manual Setup

#### Step 1: Python Environment Setup

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

#### Step 2: Install Dependencies

```bash
pip install -r backend/requirements.txt
```

#### Step 3: Prepare Model File

1. Train the model using the Jupyter notebook: `waste classification organic and non organic-code.ipynb`
2. Or download a pre-trained model
3. Place `RF_Classifier.pkl` in `backend/models/` directory

#### Step 4: Start Backend Server

```bash
python backend/app.py
```

The API will start on `http://localhost:5000`

#### Step 5: Open Frontend

**Option A: Direct File**
- Open `frontend/index.html` in your web browser

**Option B: Local Server (Recommended)**
```bash
cd frontend
python -m http.server 8000
```
Then visit `http://localhost:8000`

## Verification

1. **Check Backend Health**
   ```bash
   curl http://localhost:5000/api/health
   ```
   Should return: `{"status": "healthy", "model_loaded": true, ...}`

2. **Test Frontend**
   - Open the frontend in your browser
   - Try uploading a test image
   - Verify classification works

## Troubleshooting

### Backend Issues

**Port Already in Use:**
- Change port in `backend/config.py`: `FLASK_PORT = 5001`
- Or kill the process using port 5000

**Model Not Found:**
- Ensure `RF_Classifier.pkl` exists in `backend/models/`
- Check file permissions

**Import Errors:**
- Verify virtual environment is activated
- Reinstall dependencies: `pip install -r backend/requirements.txt`

### Frontend Issues

**CORS Errors:**
- Ensure backend is running
- Check CORS configuration in `backend/config.py`

**API Connection Failed:**
- Verify backend URL in `frontend/js/middleware.js`
- Check browser console for errors

## Environment Variables (Optional)

Create a `.env` file in the project root:

```env
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=True
CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
LOG_LEVEL=INFO
```

## Next Steps

- Read the [README.md](README.md) for detailed documentation
- Check [API Documentation](README.md#-api-documentation) for endpoint details
- Review [Contributing Guide](CONTRIBUTING.md) if you want to contribute

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing GitHub issues
3. Create a new issue with detailed information
