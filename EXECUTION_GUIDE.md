# 🚀 Execution Guide - Where and How to Run

## Quick Answer

**You need to run the program in TWO places:**

1. **Backend (Terminal/Command Prompt)** - Runs the AI server
2. **Frontend (Web Browser)** - The user interface

---

## 📍 Where to Execute

### Location 1: Command Prompt / Terminal

**Windows:**
- Press `Win + R` → type `cmd` → Enter
- Or search "Command Prompt" in Start Menu

**macOS/Linux:**
- Press `Cmd + Space` (Mac) or `Ctrl + Alt + T` (Linux)
- Type "Terminal"

**Navigate to your project:**
```bash
cd "C:\Users\91703\OneDrive\Desktop\github repositories\ML-Waste-classification-"
```

### Location 2: Web Browser

- Chrome, Firefox, Edge, or Safari
- Just open the HTML file or use a local server

---

## 🎯 How to Execute (3 Simple Steps)

### Step 1: Install Dependencies (First Time Only)

```bash
pip install -r backend/requirements.txt
```

### Step 2: Start Backend Server

**Option A: Use the run script (Easiest)**
```bash
# Windows
run.bat

# macOS/Linux
chmod +x run.sh
./run.sh
```

**Option B: Manual start**
```bash
python backend/app.py
```

**✅ You should see:**
```
Starting Waste Classification API...
Model loaded successfully
 * Running on http://0.0.0.0:5000
```

**⚠️ Keep this terminal window open!**

### Step 3: Open Frontend

**Option A: Direct File (Easiest)**
1. Open File Explorer
2. Go to: `ML-Waste-classification-\frontend\`
3. Double-click `index.html`
4. It opens in your browser automatically

**Option B: Local Server (For Development)**
```bash
# Open a NEW terminal window
cd frontend
python -m http.server 8000
# Then visit http://localhost:8000
```

---

## 📊 Visual Execution Flow

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR COMPUTER                        │
│                                                         │
│  ┌──────────────┐              ┌──────────────┐       │
│  │   TERMINAL   │              │   BROWSER     │       │
│  │              │              │              │       │
│  │ $ python     │              │  index.html  │       │
│  │   backend/   │  ◄─────────► │              │       │
│  │   app.py     │   HTTP API   │  [Upload]    │       │
│  │              │              │  [Classify]  │       │
│  │ Running on   │              │  [Results]  │       │
│  │ :5000        │              │              │       │
│  └──────────────┘              └──────────────┘       │
│         │                                              │
│         │ Uses ML Model                                │
│         ▼                                              │
│  ┌──────────────┐                                      │
│  │  RF_Classifier│                                     │
│  │  .pkl        │                                      │
│  └──────────────┘                                      │
└─────────────────────────────────────────────────────────┘
```

---

## 🎬 Complete Execution Example

### Windows Example:

```powershell
# Step 1: Open PowerShell
# Navigate to project
cd "C:\Users\91703\OneDrive\Desktop\github repositories\ML-Waste-classification-"

# Step 2: Activate virtual environment (if using)
venv\Scripts\activate

# Step 3: Start backend
python backend/app.py

# Step 4: In File Explorer, navigate to frontend folder
# Double-click index.html
```

### macOS/Linux Example:

```bash
# Step 1: Open Terminal
# Navigate to project
cd ~/Desktop/github\ repositories/ML-Waste-classification-

# Step 2: Activate virtual environment (if using)
source venv/bin/activate

# Step 3: Start backend
python backend/app.py

# Step 4: Open browser and navigate to frontend/index.html
# Or use: open frontend/index.html
```

---

## ✅ Verification Checklist

Before running, ensure:

- [ ] Python 3.8+ is installed (`python --version`)
- [ ] Dependencies installed (`pip list` shows Flask, scikit-learn, etc.)
- [ ] Model file exists (`backend/models/RF_Classifier.pkl`)
- [ ] Backend terminal shows "Running on :5000"
- [ ] Browser opens the frontend page
- [ ] No errors in terminal or browser console

---

## 🔍 Testing the Output

### Test 1: Backend Health Check

In a new terminal:
```bash
curl http://localhost:5000/api/health
```

Expected output:
```json
{"status": "healthy", "model_loaded": true, "service": "Waste Classification API"}
```

### Test 2: Upload and Classify

1. Open frontend in browser
2. Upload an image from `test images/` folder
3. Click "Classify Waste"
4. See the result!

Expected output:
- Classification: ORGANIC or NON-ORGANIC
- Confidence percentage
- Probability bars

---

## 🛑 Stopping the Program

1. **Stop Backend:** In terminal, press `Ctrl + C`
2. **Close Browser:** Close the browser tab
3. **Stop Frontend Server (if used):** Press `Ctrl + C` in that terminal

---

## 📝 File Locations Summary

| Component | Location | How to Run |
|-----------|----------|------------|
| **Backend** | `backend/app.py` | `python backend/app.py` |
| **Frontend** | `frontend/index.html` | Double-click or open in browser |
| **Model** | `backend/models/RF_Classifier.pkl` | Auto-loaded by backend |
| **Config** | `backend/config.py` | Auto-loaded by backend |

---

## 🆘 Common Issues

### "Module not found"
→ Run: `pip install -r backend/requirements.txt`

### "Model not found"
→ Place `RF_Classifier.pkl` in `backend/models/` folder

### "Port 5000 in use"
→ Change port in `backend/config.py` or close the program using port 5000

### "Can't connect to backend"
→ Make sure backend is running (check terminal)

---

## 📚 More Help

- **Detailed Setup:** [SETUP.md](SETUP.md)
- **Quick Start:** [QUICKSTART.md](QUICKSTART.md)
- **Full Instructions:** [HOW_TO_RUN.md](HOW_TO_RUN.md)
- **Architecture:** [ARCHITECTURE.md](ARCHITECTURE.md)

---

**Ready to run?** Follow the steps above and you'll be classifying waste in minutes! 🎉
