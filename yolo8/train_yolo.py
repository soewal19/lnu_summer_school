from ultralytics import YOLO

def train_model(model_name, data_path, epochs, batch_size, imgsz, name):
    model = YOLO(model_name)
    results = model.train(
        data=data_path,
        imgsz=imgsz,
        epochs=epochs,
        batch=batch_size,
        name=name
    )
    return results

if __name__ == '__main__':
    data_path = 'football_v8.yaml'
    epochs = 50
    batch_size = 8
    imgsz = 1280

    # Train YOLOv8 Nano
    train_model('yolov8n.pt', data_path, epochs, batch_size, imgsz, 'yolov8n_v8_50e')

    # Train YOLOv8 Small
    train_model('yolov8s.pt', data_path, epochs, batch_size, imgsz, 'yolov8s_v8_50e')

    # Train YOLOv8 Medium
    train_model('yolov8m.pt', data_path, epochs, batch_size, imgsz, 'yolov8m_v8_50e')
