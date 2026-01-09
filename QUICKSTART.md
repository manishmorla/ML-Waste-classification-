# Quick Start Guide

Get up and running in 5 minutes! ⚡

## Prerequisites Check

- ✅ Python 3.8+ installed
- ✅ pip installed
- ✅ Modern web browser

## Installation (3 Steps)

### 1. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### 2. Add Model File

Place your trained model `RF_Classifier.pkl` in:
```
backend/models/RF_Classifier.pkl
```

> **Note**: If you don't have a model yet, train it using the Jupyter notebook: `waste classification organic and non organic-code.ipynb`

### 3. Start the Application

**Terminal 1 - Backend:**
```bash
python backend/app.py
```
✅ Backend running at `http://localhost:5000`

**Terminal 2 - Frontend (Optional):**
```bash
cd frontend
python -m http.server 8000
```
✅ Frontend at `http://localhost:8000`

Or simply open `frontend/index.html` in your browser!

## Test It!

1. Open the frontend in your browser
2. Upload a waste image (JPG, PNG, GIF, or BMP)
3. Click "Classify Waste"
4. See the results! 🎉

## Troubleshooting

**Backend won't start?**
- Check if port 5000 is available
- Verify Python version: `python --version`
- Check dependencies: `pip list`

**Model not found?**
- Ensure `RF_Classifier.pkl` is in `backend/models/`
- Check file permissions

**Frontend can't connect?**
- Verify backend is running
- Check browser console for errors
- Ensure CORS is enabled in backend

## Next Steps

- 📖 Read the full [README.md](README.md)
- 🏗️ Check [ARCHITECTURE.md](ARCHITECTURE.md) for system design
- 🤝 See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

---

**Need Help?** Open an issue on GitHub!
