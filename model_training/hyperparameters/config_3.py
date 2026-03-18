CONFIG = {
    "model": "yolo11m.pt",           
    "data": "../../dataset.yaml",
    "imgsz": 640,

    # Hyperparameters             
    "epochs": 150,                   
    "batch": -1, # Auto-batch, maximizes GPU memory utilization
    "patience": 30,
    "device": 0,                
    "optimizer": "AdamW",            
    "lr0": 0.001,                     
    "lrf": 0.01,                                       
    "weight_decay": 0.0005, 
    "warmup_epochs": 5.0,   

    "mosaic": 1.0,
    "mixup": 0.1,
    "copy_paste": 0.1,
    "hsv_h": 0.015,
    "degrees": 10.0,

    "project": "runs/train",
    "name": "aircraft_yolo11m_v3_optimized",
    "exist_ok": True,
    "plots": True,
    "save_period": 5               
}