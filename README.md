
# 🎬 Movie Recommendation System

A content-based movie recommender system built using **Python**, **Streamlit**, and **Machine Learning**. Select any movie, and it will suggest 5 similar movies along with their posters using the TMDb API.

---

## 📌 Features

- ✅ Content-based filtering using genres, keywords, cast & crew
- ✅ Cosine similarity for recommendation
- ✅ Fetches posters from TMDb API
- ✅ Lightweight and easy-to-use Streamlit interface
- ✅ Clean, fast, and responsive results

---

## 🗂️ Project Structure

![Image](https://github.com/user-attachments/assets/9961ef4d-4e26-4633-a450-12590fc97556)


---

## 🧠 How It Works

1. **Data Preprocessing**: Combines movie and credit data, extracts key features (genres, keywords, top 3 cast members, director).
2. **Tag Creation**: Creates a textual representation (`tags`) for each movie.
3. **Vectorization**: Converts tags into vectors using `CountVectorizer`.
4. **Similarity Calculation**: Computes pairwise cosine similarity between movies.
5. **Recommendation**: Returns top 5 similar movies based on selected title.
6. **Poster Display**: Uses TMDb API to fetch and show movie posters.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```
### 2. Install Dependencies
```bash
pip install pandas numpy scikit-learn streamlit requests
```
### 3. Prepare the Data
```bash
python main.py
```
### 4. Run the Streamlit App
```bash
streamlit run app.py
```
----

🔑 TMDb API Key
---
To fetch movie posters, you need a TMDb API key.

1. Sign up at TMDb

2. Navigate to Settings > API > Create API Key

3. Replace the placeholder in app.py
```bash
  API_KEY = "your_tmdb_api_key"
```
📸 Demo Screenshot
---
![Screenshot](https://github.com/user-attachments/assets/eabb30c7-b07b-4a44-b220-a94e5aaeafaa)

📈 Future Enhancements
---
🔄 Add collaborative filtering for user-based recommendations

🧠 Use TF-IDF or BERT-based models for smarter tagging

🌐 Deploy online with Streamlit Cloud, Render, or Heroku

🔍 Add filters for genre, year, or popularity

📄 License
---
This project is licensed under the MIT License.
