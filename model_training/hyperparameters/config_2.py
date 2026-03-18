CONFIG = {
    "model": "yolo11m.pt",           
    "data": "../../dataset.yaml",
    "imgsz": 640,

    # Hyperparameters             
    "epochs": 100,                   
    "batch": 32,                     
    "optimizer": "AdamW",            
    "lr0": 0.01,                     
    "lrf": 0.01,                     
    "patience": 20,                  
    "save_period": 5,
    "weight_decay": 0.0005,          
    "device": 0,                     
    "project": "runs/train",
    "name": "aircraft_yolo11m_v2",
    "exist_ok": True,
    "plots": True,                  
    "mosaic": 0.0                
}