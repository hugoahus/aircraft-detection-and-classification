# Deep Learning for Aircraft Type Detection and Operator Classification

## Overview

This repository contains a deep learning project focused on image‑based aircraft recognition and operator‑based categorization. The goal is to build an end‑to‑end pipeline that takes an input image, detects any aircraft present, identifies their specific types, and then maps each detected aircraft to a higher‑level operator group (primarily used by NATO countries, non‑NATO countries, or both).

The project is developed in the context of DATASCI 3ML3 – Introduction to Neural Networks and Machine Learning at McMaster University, and is designed to showcase practical applications of supervised learning, convolutional neural networks, optimization, and model evaluation.

## Dataset

The project uses the “**AeroScan: Military Aircraft Classification**” dataset obtained from Kaggle. The dataset consists of:
- Images of military aircraft and background scenes
- YOLO‑style annotation files (.txt) for each image, where each line encodes:
  - Class ID (aircraft type)
  - Normalized bounding box center coordinates (x_center, y_center)
  - Normalized bounding box width and height

Each image may contain one or multiple aircrafts. The class IDs are mapped to specific aircraft models and an additional metadata mapping is created to associate each aircraft type with an operator group (NATO, non‑NATO, or both) based on publicly available information.

## Problem formulation

At a high level, the project addresses the following tasks:

1. Object detection:  
    - Detect all aircraft present in an image and localize them with bounding boxes.
2. Type classification:  
    - For each detected aircraft, predict its aircraft type (one of the 88 classes in the dataset).
3. Operator‑based categorization:  
    - Map each predicted aircraft type to an operator group:
      - Primarily used by NATO countries
      - Primarily used by non‑NATO countries
      - Used by both NATO and non‑NATO countries
4. User‑facing output:  
    - For each detected aircraft, report:
      - The predicted aircraft model
      - The corresponding operator group
     
## Aircraft Classes used for training the model

| Class ID | Aircraft Type |
|---------|----------------|
| 0 | A10 |
| 1 | A400M |
| 2 | AG600 |
| 3 | AH64 |
| 4 | AKINCI |
| 5 | AV8B |
| 6 | An124 |
| 7 | An22 |
| 8 | An225 |
| 9 | An72 |
| 10 | B1 |
| 11 | B2 |
| 12 | B52 |
| 13 | Be200 |
| 14 | C1 |
| 15 | C130 |
| 16 | C17 |
| 17 | C2 |
| 18 | C390 |
| 19 | C5 |
| 20 | CH47 |
| 21 | CH53 |
| 22 | CL415 |
| 23 | E2 |
| 24 | E7 |
| 25 | EF2000 |
| 26 | EMB314 |
| 27 | F117 |
| 28 | F14 |
| 29 | F15 |
| 30 | F16 |
| 31 | F18 |
| 32 | F2 |
| 33 | F22 |
| 34 | F35 |
| 35 | F4 |
| 36 | FCK1 |
| 37 | H6 |
| 38 | Il76 |
| 39 | J10 |
| 40 | J20 |
| 41 | J35 |
| 42 | J36 |
| 43 | JAS39 |
| 44 | JF17 |
| 45 | JH7 |
| 46 | KAAN |
| 47 | KC135 |
| 48 | KF21 |
| 49 | KJ600 |
| 50 | Ka27 |
| 51 | Ka52 |
| 52 | MQ9 |
| 53 | Mi24 |
| 54 | Mi26 |
| 55 | Mi28 |
| 56 | Mi8 |
| 57 | Mig29 |
| 58 | Mig31 |
| 59 | Mirage2000 |
| 60 | P3 |
| 61 | RQ4 |
| 62 | Rafale |
| 63 | SR71 |
| 64 | Su24 |
| 65 | Su25 |
| 66 | Su34 |
| 67 | Su47 |
| 68 | Su57 |
| 69 | TB001 |
| 70 | TB2 |
| 71 | Tejas |
| 72 | Tornado |
| 73 | Tu160 |
| 74 | Tu22M |
| 75 | Tu95 |
| 76 | U2 |
| 77 | UH60 |
| 78 | US2 |
| 79 | V22 |
| 80 | Vulcan |
| 81 | WZ7 |
| 82 | X32 |
| 83 | XB70 |
| 84 | Y20 |
| 85 | YF23 |
| 86 | Z10 |
| 87 | Z19 |
