@echo off
echo ========================================
echo    Educational Malware Builder
echo ========================================
echo.
echo Starting the builder...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Check if main.py exists
if not exist "main.py" (
    echo ERROR: main.py not found
    echo Please make sure you're running this from the correct directory
    pause
    exit /b 1
)

echo Starting the Educational Malware Builder...
echo.
echo WARNING: This tool is for educational purposes only!
echo Use only in isolated lab environments.
echo.

REM Start the builder
python main.py

echo.
echo Builder has exited.
pause 