from ultralytics import YOLO
import cv2
import json
from pathlib import Path


def analyze_video(model_path, video_path, output_path):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)
    frame_idx = 0
    results = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections = model(frame)
        frame_results = {
            'frame': frame_idx,
            'detections': []
        }

        for det in detections:
            frame_results['detections'].append({
                'class': det.cls,
                'confidence': det.conf,
                'bbox': det.xyxy
            })

        results.append(frame_results)
        frame_idx += 1

    cap.release()

    with open(output_path, 'w') as f:
        json.dump(results, f, indent=4)


if __name__ == '__main__':
    model_path = 'path_to_your_trained_model.pt'
    video_folder = './videos'
    output_folder = './output'

    os.makedirs(output_folder, exist_ok=True)
    video_files = list(Path(video_folder).glob('*.mp4'))

    for video_file in video_files:
        output_path = os.path.join(output_folder, f'{video_file.stem}_analysis.json')
        analyze_video(model_path, video_file, output_path)
