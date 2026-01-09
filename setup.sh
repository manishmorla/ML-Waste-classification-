#!/bin/bash

echo "===================================="
echo "Waste Classification AI - Setup"
echo "===================================="
echo ""

echo "[1/4] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    echo "Please ensure Python 3 is installed"
    exit 1
fi

echo "[2/4] Activating virtual environment..."
source venv/bin/activate

echo "[3/4] Installing Python dependencies..."
pip install --upgrade pip
pip install -r backend/requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo "[4/4] Creating necessary directories..."
mkdir -p backend/models
mkdir -p backend/uploads

echo ""
echo "===================================="
echo "Setup Complete!"
echo "===================================="
echo ""
echo "Next steps:"
echo "1. Place your trained model (RF_Classifier.pkl) in backend/models/"
echo "2. Run: python backend/app.py"
echo "3. Open frontend/index.html in your browser"
echo ""
echo "For detailed instructions, see SETUP.md"
echo ""
