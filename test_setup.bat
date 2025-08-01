@echo off
echo ========================================
echo    Testing Setup
echo ========================================
echo.
echo Testing if all requirements are installed...
echo.

REM Test Python
echo Testing Python...
python --version
if errorlevel 1 (
    echo ERROR: Python not found
    pause
    exit /b 1
)

REM Test key dependencies
echo.
echo Testing key dependencies...

echo Testing requests...
python -c "import requests; print('✓ requests - OK')" 2>nul
if errorlevel 1 echo ✗ requests - NOT FOUND

echo Testing psutil...
python -c "import psutil; print('✓ psutil - OK')" 2>nul
if errorlevel 1 echo ✗ psutil - NOT FOUND

echo Testing pynput...
python -c "import pynput; print('✓ pynput - OK')" 2>nul
if errorlevel 1 echo ✗ pynput - NOT FOUND

echo Testing PIL...
python -c "from PIL import ImageGrab; print('✓ PIL (Pillow) - OK')" 2>nul
if errorlevel 1 echo ✗ PIL (Pillow) - NOT FOUND

echo Testing colorama...
python -c "import colorama; print('✓ colorama - OK')" 2>nul
if errorlevel 1 echo ✗ colorama - NOT FOUND

echo Testing cryptography...
python -c "import cryptography; print('✓ cryptography - OK')" 2>nul
if errorlevel 1 echo ✗ cryptography - NOT FOUND

echo.
echo ========================================
echo    Test Complete
echo ========================================
echo.
echo If all dependencies show "OK", you're ready to use the builder!
echo Run start_builder.bat to begin.
echo.
pause 