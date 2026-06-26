# 🎬 Movie Recommendation System

A Machine Learning-based **Movie Recommendation System** built using **Python, Scikit-Learn, Streamlit, and TMDB Movie Dataset**. The application recommends movies based on content similarity by analyzing genres, keywords, cast, crew, and movie overviews using Natural Language Processing (NLP) and cosine similarity. The project provides an intuitive web interface where users can search for a movie and instantly receive the top 20 most similar movie recommendations along with their posters.

## 🚀 Live Demo

**Live Application:**
https://movies-recommendation-system-app.streamlit.app/

---

## 📌 Features

* 🎥 Content-Based Movie Recommendation System
* 🔍 Search movies from the TMDB dataset
* 🖼️ Displays movie posters for every recommendation
* 🤖 Machine Learning recommendation engine
* 📊 NLP-based feature extraction using CountVectorizer
* 📐 Cosine Similarity for recommendation generation
* 🌐 Interactive Streamlit web application
* ⚡ Fast and responsive user interface
* 🎯 Top 20 personalized movie recommendations

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Streamlit
* Pickle
* gdown
* TMDB Movie Dataset

---

## 📊 Machine Learning Workflow

1. Data Cleaning & Preprocessing
2. Feature Engineering
3. Text Processing using NLP
4. Count Vectorization
5. Cosine Similarity Matrix Generation
6. Recommendation Engine
7. Streamlit Web Application Deployment

---

## 📂 Project Structure

```
Movie-Recommendation-System
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── poster.pkl
├── requirements.txt
├── README.md
└── Movie_Recommender_code.ipynb
```

---

## ▶️ How to Run Locally

Clone the repository:

```bash
git clone https://github.com/Aayush-Naithani/Movies-Recommendation-System.git
```

Navigate to the project folder:

```bash
cd Movies-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📈 Recommendation Method

The recommendation engine follows a **Content-Based Filtering** approach:

* Combines important movie attributes into a single text feature.
* Applies **CountVectorizer** to convert text into numerical vectors.
* Computes **Cosine Similarity** between movie vectors.
* Returns the **Top 20 most similar movies** along with their posters.

---

## 📸 Application Preview

* Search any movie from the dropdown list.
* View the selected movie poster.
* Receive 20 recommended movies displayed with posters in a responsive grid layout.

---

## 🎯 Future Improvements

* TMDB API integration for real-time movie data
* Search bar with autocomplete
* Movie ratings and release dates
* Genre-based filtering
* User authentication
* Hybrid recommendation system
* Collaborative filtering

---

## 👨‍💻 Author

**Aayush Naithani**

* GitHub: https://github.com/Aayush-Naithani
* LinkedIn: https://www.linkedin.com/in/aayush-naithani-8433102a8/

---

⭐ If you found this project helpful, consider giving the repository a **Star**.
