import streamlit as st
import pickle
import gdown
import os

@st.cache_resource
def load_data():
    if not os.path.exists("movies.pkl"):
        gdown.download("https://drive.google.com/file/d/1M8Xz5p_WEV4LyWp-yAlLVAJtv__k8-cc/view?usp=sharing", "movies.pkl", quiet=False)
    if not os.path.exists("similarity.pkl"):
        gdown.download("https://drive.google.com/file/d/10_MPFZlXiuKLTbFAYGsWIoTOwgIHlFlV/view?usp=drive_link", "similarity.pkl", quiet=False)
    if not os.path.exists("poster.pkl"):
        gdown.download("https://drive.google.com/file/d/1jrrJNPpawbnrrlr7Lhs-9CRtBS7R4dV1/view?usp=drive_link", "poster.pkl", quiet=False)

    movies_list = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    poster_list = pickle.load(open("poster.pkl", "rb"))
    return movies_list, similarity, poster_list

def poster(mov_ind):
    return poster_list[mov_ind]

def recommend(movie):
    mov_ind = movies_list[movies_list["Title"]==movie].index[0]
    distances = similarity[mov_ind]
    suggestions = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:21]
    recommendations = []
    posters = []
    for i in suggestions:
        recommendations.append(movies_list["Title"][i[0]])
        posters.append(poster(i[0]))
    return recommendations, posters

movies_list, similarity, poster_list = load_data()

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Search Your movies below......",
    (movies_list["Title"].values)
)


if st.button("Search"):

    recommendations, posters = recommend(selected_movie_name)

    # --------------------------
    # Selected Movie
    # --------------------------
    st.markdown(
        f"<h3>You Searched For: <span style='color:#FF4B4B'>{selected_movie_name}</span></h3>",
        unsafe_allow_html=True
    )

    movie_index = movies_list[movies_list["Title"] == selected_movie_name].index[0]

    st.image(
        poster(movie_index),
        width=250
    )

    st.markdown("---")
    st.subheader("Recommended Movies")

    # --------------------------
    # Recommended Movies
    # --------------------------
    for i in range(1, len(recommendations), 5):

        cols = st.columns(5)

        for col, movie, poster_url in zip(
            cols,
            recommendations[i:i+5],
            posters[i:i+5]
        ):
            with col:
                st.image(poster_url, use_container_width=True)
                st.caption(movie)