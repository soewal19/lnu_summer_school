@echo off
REM Setup script for YOLOv8 Football Analytics Project

REM Create a virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install required packages
echo Installing required packages...
pip install ultralytics opencv-python clearml

REM Install additional dependencies
echo Installing additional dependencies...
pip install -r requirements.txt

REM Run the main pipeline
echo Running the main pipeline...
python main.py

REM Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate

echo Setup and pipeline execution completed.
pause
