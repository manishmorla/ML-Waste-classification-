@echo off
echo ====================================
echo Waste Classification AI - Setup
echo ====================================
echo.

echo [1/4] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    echo Please ensure Python is installed and in PATH
    pause
    exit /b 1
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing Python dependencies...
pip install --upgrade pip
pip install -r backend\requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/4] Creating necessary directories...
if not exist "backend\models" mkdir backend\models
if not exist "backend\uploads" mkdir backend\uploads

echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo.
echo Next steps:
echo 1. Place your trained model (RF_Classifier.pkl) in backend\models\
echo 2. Run: python backend\app.py
echo 3. Open frontend\index.html in your browser
echo.
echo For detailed instructions, see SETUP.md
echo.
pause
