@echo off
echo ========================================
echo    Educational Malware Builder Setup
echo ========================================
echo.
echo Installing required Python packages...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

echo Python found. Installing requirements...
echo.

REM Install requirements
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install some requirements
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo ========================================
echo    Setup Complete!
echo ========================================
echo.
echo All requirements have been installed successfully.
echo You can now run the builder with: start_builder.bat
echo.
pause 