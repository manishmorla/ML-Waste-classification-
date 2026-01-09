#!/bin/bash

echo "===================================="
echo "Waste Classification AI - Launcher"
echo "===================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found!"
    echo "Please run setup.sh first or create venv manually."
    echo ""
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if model exists
if [ ! -f "backend/models/RF_Classifier.pkl" ]; then
    echo ""
    echo "WARNING: Model file not found!"
    echo "Please ensure RF_Classifier.pkl is in backend/models/ folder"
    echo ""
fi

echo ""
echo "Starting backend server..."
echo "Backend will run on http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "===================================="
echo ""

# Start the Flask app
python backend/app.py
