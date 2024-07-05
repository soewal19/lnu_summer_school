# User Guide

## Introduction
This application is designed to analyze football matches using YOLOv8 models. The application extracts frames from recorded videos, trains YOLOv8 models, and analyzes the videos to generate JSON reports containing football match analytics.

## Installation
Clone the repository:
```
git clone <repository-url>
cd football_analysis
Install dependencies:



pip install -r requirements.txt
or run file into windows setup_and_run.bat
Double-click setup_and_run.bat to execute it. This will set up the environment and run the pipeline.
Preparing the Dataset
Place your recorded football match videos in the videos directory. The videos ould be in .mp4 format.

Run the extract_frames.py script to extract frames from the videos:



python extract_frames.py
Training the Models
Annotate the extracted frames using an annotation tool like LabelImg. Save the annotations in the labels directories.

Run the train_yolo.py script to train the YOLOv8 models:



python train_yolo.py
Analyzing Videos
Run the analyze_football.py script to analyze the videos and generate JSON reports:



python analyze_football.py
### Output
The analysis results will be saved in the output directory as JSON files, containing detailed information about the detected objects (players, ball, goal) in each frame of the video.

Conclusion
This application provides a comprehensive pipeline for analyzing football matches using YOLOv8 models. By following the steps outlined in this guide, you can train custom models and generate detailed analysis reports for football match videos.

## Explanation of main.py
Download Video:

download_video(url, save_path): Downloads a video from the given URL and saves it to the specified path.
Load Video:

load_video(video_path): Loads a video from the specified path and checks if it can be opened.
Process Video:

process_video(video_path): Runs the data preprocessing, model training, object detection, event analysis, and report generation scripts.
Main Function:

Prompts the user to enter a video URL or load a default test video.
Allows the user to pause the program (with a yellow message) or exit (with a red message).
Processes the selected video using the defined pipeline.
### Instructions for Using the Program
Ensure Dependencies:

Make sure to have the required dependencies installed (ultralytics, opencv-python, clearml).
Prepare Default Video:

Place a test video named test.mp4 in the testVideo folder.
Run the Program:

Execute main.py to start the program.
Follow the on-screen prompts to either download a video from a URL or load the default test video.
Use the specified keys to control the program (e.g., pause or exit).
This script provides a flexible and user-friendly interface for running the YOLOv8-based football analytics pipeline.







