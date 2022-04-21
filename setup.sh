#!/bin/bash
echo "Checking if python is installed..."
if ! [ -x "$(command -v python)" ]; then
    echo "[ERROR] Python is not installed. Please install python and try again, https://www.python.org/downloads/"
    exit 1
fi
echo "[OK] Find python version... $(python --version)"

echo "Checking if pip is installed..."
if ! [ -x "$(command -v pip)" ]; then
    echo "[ERROR] Pip3 is not installed. Please install pip and try again, https://pip.pypa.io/en/stable/"
    exit 1
fi
echo "[OK] Find pip version... $(pip --version)"

echo "Checking if virtualenv is installed..."
if ! [ -x "$(command -v virtualenv)" ]; then
    echo "[WARN] Virtualenv is not installed..."
    echo "Installing virtualenv..."
    if $(pip install virtualenv); then
        echo "[OK] virtualenv installed"
    else
        echo "[ERROR] virtualenv installation failed. Please try install virtualenv manually"
        exit 1
    fi
else
    echo "[OK] Find virtualenv version... $(virtualenv --version)"
fi

echo "Creating a virtual environment..."
virtualenv .venv
if ! [ -d ".venv" ]; then
    echo "[ERROR] virtual environment creation failed. Please try create virtual environment manually"
    exit 1
fi

echo "Activating virtual environment..."
source ./.venv/bin/activate
echo "Virtual environment activated, python from $(which python) and pip from $(which pip)"

echo "Installing requirements..."
pip install -r requirements.txt

exit 0