# Adaptive UI Using AI/HCI Project

## Adaptive Gardening Recommendation Interface

This project demonstrates an adaptive user interface using a gardening
recommendation system.

The original gardening recommendation system was modified to adapt its
recommendations and guidance based on user selections and interactions
during the current session.

### Adaptive Features

- Tracks user interactions during the session
- Learns frequently selected plant and gardening-topic preferences
- Provides personalized gardening recommendations
- Adjusts guidance for Beginner, Intermediate, and Advanced users
- Uses TF-IDF and cosine similarity to rank gardening topics
- Allows users to reset learned preferences
- Provides an interactive interface using Gradio

### Files

- `Adaptive_UI_Gardening_Project.ipynb` – Python/Google Colab notebook
- `gardening_videos.csv` – Gardening recommendation dataset

### Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Gradio

### Running the Project

Open `Adaptive_UI_Gardening_Project.ipynb` in Google Colab and run the
notebook cells in order. The `gardening_videos.csv` dataset is required
for the recommendation system.
