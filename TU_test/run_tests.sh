#!/bin/bash
set -e

echo "========================================="
echo "   TU_test - Setup & Run (Windows Fix)"
echo "========================================="

# (a) System Dependencies
echo "[1/3] Checking dependencies..."
if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    echo "Python is not installed on this host. Please install Python for Windows."
    exit 1
fi

# Determine the correct python command
PYTHON_CMD="python"
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
fi

# (b) Download Execution Files
echo "[2/3] Installing packages..."
if [ ! -d "venv" ]; then
    $PYTHON_CMD -m venv venv
fi

# Windows Git Bash uses Scripts instead of bin
if [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

pip install --upgrade pip -q
pip install -r requirements.txt -q
playwright install chromium

# (c) Run pytest -v
echo "[3/3] Running pytest -v ..."
echo "========================================="
pytest -v