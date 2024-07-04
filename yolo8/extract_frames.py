import cv2
import os
import random
from pathlib import Path

# Paths to video folder and output directories
video_folder = './videos'
train_images_folder = './data/football/train/images'
val_images_folder = './data/football/val/images'
train_labels_folder = './data/football/train/labels'
val_labels_folder = './data/football/val/labels'

# Create directories if they don't exist
os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(val_images_folder, exist_ok=True)
os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(val_labels_folder, exist_ok=True)


def extract_frames(video_path, output_folder, label_folder, frame_rate=1):
    video_name = Path(video_path).stem
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = fps // frame_rate

    frame_idx = 0
    extracted_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % frame_interval == 0:
            image_path = os.path.join(output_folder, f'{video_name}_frame_{extracted_count:04d}.jpg')
            cv2.imwrite(image_path, frame)

            # Create an empty label file for the frame
            label_path = os.path.join(label_folder, f'{video_name}_frame_{extracted_count:04d}.txt')
            open(label_path, 'w').close()

            extracted_count += 1

        frame_idx += 1

    cap.release()


# List of video files
video_files = list(Path(video_folder).glob('*.mp4'))

# Shuffle and split videos into training and validation sets
random.shuffle(video_files)
split_index = int(0.8 * len(video_files))
train_videos = video_files[:split_index]
val_videos = video_files[split_index:]

# Extract frames for training videos
for video_file in train_videos:
    extract_frames(video_file, train_images_folder, train_labels_folder)

# Extract frames for validation videos
for video_file in val_videos:
    extract_frames(video_file, val_images_folder, val_labels_folder)
