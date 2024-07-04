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
Output
The analysis results will be saved in the output directory as JSON files, containing detailed information about the detected objects (players, ball, goal) in each frame of the video.

Conclusion
This application provides a comprehensive pipeline for analyzing football matches using YOLOv8 models. By following the steps outlined in this guide, you can train custom models and generate detailed analysis reports for football match videos.