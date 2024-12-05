# Stock Movement Analysis Based on Social Media Sentiment

<!-- Brief overview of the project -->
This project predicts stock price movements by analyzing social media discussions. It includes data scraping, preprocessing, feature extraction, and a machine-learning model for prediction.

---

## Table of Contents
<!-- Navigation for easy reference -->
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [How to Run the Project](#how-to-run-the-project)
4. [Directory Structure](#directory-structure)
5. [Model Evaluation](#model-evaluation)
6. [License](#license)

---

## Project Overview
<!-- High-level description of the project -->
The project scrapes Reddit posts related to stock discussions, performs sentiment analysis, and predicts stock movements using a Random Forest model.

---

## Features
<!-- Key functionalities and processes -->
- Scraping data from Reddit.
- Data preprocessing and feature extraction.
- Sentiment analysis of posts.
- Machine learning model training and evaluation.

---

## How to Run the Project
<!-- Step-by-step instructions to run the project -->

### Prerequisites
1. Install Python 3.8 or higher.
2. Clone the repository (if using Git on desktop):
   ```bash
   git clone https://github.com/[YourUsername]/Stock-Movement-Analysis.git
   cd Stock-Movement-Analysis
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
1. **Scrape data**:
   ```bash
   python scraper/reddit_scraper.py
   ```
2. **Preprocess data**:
   ```bash
   python model/data_preprocessing.py
   ```
3. **Train the model**:
   ```bash
   python model/train_model.py
   ```
4. **Evaluate the model**:
   ```bash
   python model/evaluate_model.py
   ```

---

## Directory Structure
<!-- Organization of the repository for clarity -->

```
Stock-Movement-Analysis/
├── README.md                 # Project overview and instructions
├── LICENSE                   # License details
├── .gitignore                # Files and folders to ignore in Git
├── requirements.txt          # Dependencies
├── notebooks/                # Jupyter notebooks
│   ├── 01_data_scraping.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
├── scraper/                  # Data scraping code
│   └── reddit_scraper.py
├── model/                    # Model-related scripts
│   ├── data_preprocessing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── feature_extraction.py
├── data/                     # Data files
│   ├── reddit_posts_with_sentiment.csv
│   ├── preprocessed_data.csv
├── saved_models/             # Saved models
│   └── random_forest_model.pkl
└── docs/                     # Documentation
    └── Project_Report.pdf
```

---

## Model Evaluation
<!-- Overview of model performance -->
The Random Forest model achieved the best results, with an accuracy of 85%. For detailed metrics, refer to the [evaluation notebook](notebooks/04_model_evaluation.ipynb).

---

## License
<!-- Licensing information -->
This project is licensed under the MIT License. Please take a look at the [LICENSE](LICENSE) file for details.
```

### **How to Use This**

- Copy the snippet into your `README.md` file in the repository.
- Replace placeholders like `[YourUsername]` with your GitHub username.
- Ensure that all file paths (e.g., `notebooks/`, `scraper/`, etc.) match the actual repository structure.
