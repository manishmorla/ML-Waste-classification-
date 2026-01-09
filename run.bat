@echo off
echo ====================================
echo Waste Classification AI - Launcher
echo ====================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found!
    echo Please run setup.bat first or create venv manually.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if model exists
if not exist "backend\models\RF_Classifier.pkl" (
    echo.
    echo WARNING: Model file not found!
    echo Please ensure RF_Classifier.pkl is in backend\models\ folder
    echo.
    pause
)

echo.
echo Starting backend server...
echo Backend will run on http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
echo ====================================
echo.

REM Start the Flask app
python backend/app.py

pause
