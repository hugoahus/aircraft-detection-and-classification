CONFIG = {
    # Model and data
    "model": "yolo11l.pt",           
    "data": "/kaggle/working/aircraft-detection-and-classification/dataset.yaml",
    "imgsz": 640,         

    # Training settings
    "epochs": 150,        
    "batch": -1,
    "patience": 30,        
    "device": 0,       

    # Optimizer
    "optimizer": "AdamW",            
    "lr0": 0.0007,              
    "lrf": 0.1,                   
    "weight_decay": 0.0007,          
    "warmup_epochs": 3.0,

    "cls": 1.5,
    "close_mosaic": 20,

    # Augmentation
    "mosaic": 1.0,                 
    "mixup": 0.05,                   
    "copy_paste": 0.1,              
    "hsv_h": 0.015,                
    "degrees": 10.0,            

    # Logging and saving
    "project": "runs/train",
    "name": "aircraft_yolo11l_v6_optimized",
    "exist_ok": True,
    "plots": True,              
    "save_period": 5         
}