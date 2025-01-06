@echo off
echo Checking for Python installation...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    echo.
    echo Please install the latest version of Python to install!
    echo Install the latest version of Python, then run the Install.bat!!
    echo.
    pause
    exit /b 1
)

echo Python is installed.

:: Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please ensure pip is installed with your Python installation.
    pause
    exit /b 1
)

echo pip is installed.

:: Install required third-party libraries
echo Installing required dependencies...
pip install psutil >nul 2>&1
if %errorlevel% neq 0 (
    echo Failed to install psutil. Please check your internet connection and try again.
    pause
    exit /b 1
)

echo All required dependencies have been installed successfully.
pause