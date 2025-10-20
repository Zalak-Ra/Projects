# 🦺 Hard Hat Detection using CNN

## 📋 Project Overview
Binary classification model to detect whether a person is wearing a hard hat or not using Convolutional Neural Networks (CNN).

## 🎯 Key Features
- Converts YOLO object detection dataset to classification format
- Advanced data augmentation to prevent overfitting
- BatchNormalization and Dropout for regularization
- Early stopping and learning rate scheduling
- Achieves **92%** test accuracy

## 🛠️ Technologies Used
- Python 3.8+
- TensorFlow 2.17
- Keras
- NumPy, Matplotlib

## 📊 Model Architecture
- 3 Convolutional blocks with BatchNormalization
- MaxPooling and Dropout layers
- Dense layers with 50% dropout
- Binary classification output

## 📈 Results
- **Test Accuracy**: 92%
- **Test Loss**: 0.27

## 📁 Dataset
Dataset from [Roboflow Hard Hat Detection](https://www.kaggle.com/datasets/zalakran/hard-set)


