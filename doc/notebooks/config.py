CONFIG = {
    "model": "yolo11n.pt",
    "data": "../../dataset.yaml",
    "imgsz": 320,

    # Hyperparameters
    "epochs": 5,
    "batch": 1,
    "optimizer": "SGD",
    "lr0": 1e-3,
    "lrf": 0.01,
    "momentum": 0.937,
    "weight_decay": 5e-4,

    # Default
    "device": "cpu",
    "project": "runs/train",
    "name": "exp1",
    "exist_ok": False,
}
