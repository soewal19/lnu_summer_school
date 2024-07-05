import os
import cv2
import urllib.request
import numpy as np
import subprocess
import time


def download_video(url, save_path):
    urllib.request.urlretrieve(url, save_path)
    print(f"Video downloaded to {save_path}")


def load_video(video_path):
    if not os.path.exists(video_path):
        print(f"Video file {video_path} does not exist.")
        return None
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Failed to open video file {video_path}.")
        return None
    return cap


def process_video(video_path):
    print(f"Processing video: {video_path}")
    subprocess.run(['python', 'scripts/data_preprocessing.py'])
    subprocess.run(['python', 'scripts/train_model.py'])
    subprocess.run(['python', 'scripts/detect_objects.py', video_path])
    subprocess.run(['python', 'scripts/analyze_events.py'])
    subprocess.run(['python', 'scripts/generate_report.py'])
    print("Pipeline execution completed.")


def main():
    default_video_path = 'testVideo/test.mp4'
    video_path = ''

    user_input = input("Do you want to load a video from a URL? (Y/N): ").strip().lower()
    if user_input == 'y':
        video_url = input("Please enter the video URL: ").strip()
        video_path = 'downloaded_video.mp4'
        download_video(video_url, video_path)
    else:
        print("Press 'T' to load the default test video or 'ESC' to exit.")
        while True:
            key = input("Your choice: ").strip().lower()
            if key == 't':
                video_path = default_video_path
                break
            elif key == 'esc':
                print("\033[91mProgram terminated by the user.\033[0m")
                return
            else:
                print("Invalid input. Please press 'T' to load the default test video or 'ESC' to exit.")

    if video_path:
        cap = load_video(video_path)
        if cap:
            print("Press 'P' to pause the program, 'ESC' to exit.")
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("End of video.")
                    break
                cv2.imshow('Video', frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('p'):
                    print("\033[93mProgram is paused. Press any key to continue...\033[0m")
                    cv2.waitKey(0)  # Wait indefinitely for a key press
                elif key == 27:  # ESC key
                    print("\033[91mProgram terminated by the user.\033[0m")
                    break
            cap.release()
            cv2.destroyAllWindows()
            process_video(video_path)
        else:
            print("Failed to load the video.")
    else:
        print("No video selected.")


if __name__ == "__main__":
    main()
