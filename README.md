
# FarmerAid: A Smart Platform for Farmers

This repository contains the implementation of **FarmerAid**, a platform designed to assist farmers by providing data-driven insights to improve crop yield and farming practices. The project was developed as part of a competition held at **Mar Baselios College of  Engineering and Technology**. Our team was honored to be selected for the **Smart India Hackathon** from our college, though we did not advance further.

## Project Overview

FarmerAid leverages machine learning models to offer actionable insights for farmers. The platform is equipped with the following functionalities:

### 1. Crop Prediction Model
Predicts the optimal crop to grow based on:
- Soil moisture
- Temperature
- Humidity
- Climate data

These inputs are sourced from external hardware devices (not implemented in this project). Instead, the values are provided manually during testing.

### 2. Fertilizer and Pesticide Recommendation Model
Recommends the best fertilizers and pesticides tailored to:
- The crop
- Soil type
- Specific requirements provided as input

### 3. Plant Disease Prediction (Planned)
Although not implemented in this version, we aim to:
- Predict diseases affecting crops using a trained model.
- Suggest cures and recovery steps based on the identified disease.

## Dataset
The models are trained on pre-existing datasets:
- Crop prediction dataset
- Fertilizer and pesticide recommendation dataset

These datasets are included in this repository for ease of testing and further development.

## Team Members
This project was a collaborative effort by:
- **Liya Mary Kurian**
- **Sudhin Suresh**
- **Noble John**
- **Alvin P Mathews**
- **Kasinadhan**

## Tools and Technologies
- **Python**: Core language for building and training the models.
- **Scikit-learn/TensorFlow**: Machine learning frameworks for model training.
- **Flask**: Backend framework for API development.
- **Dataset Files**: Custom and pre-existing datasets for training.

## How It Works
1. **Crop Prediction**: Enter soil and environmental parameters as inputs, and the trained model will predict the best crop for the given conditions.
2. **Fertilizer and Pesticide Recommendation**: Provide crop and soil-specific details to get recommendations for optimal fertilizers or pesticides.
3. **Disease Prediction (Future Scope)**: Detect plant diseases and get actionable solutions to mitigate the issue.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ayuktha63/Farmer-Platform.git
   cd Farmer-Platform
   ```
2. Run the application:
   ```bash
   python app.py
   ```

## Acknowledgements
We thank **Mar Baselios College of  Engineering and Technology** for hosting this event, providing us the opportunity to innovate, and inspiring us to address real-world problems faced by farmers.

## Future Scope
- Integrate real-time data collection through IoT hardware.
- Implement plant disease prediction and solution models.
- Enhance model accuracy with more extensive datasets.

## License
This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to explore the repository and contribute to its development.
