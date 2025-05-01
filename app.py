import streamlit as st
import pickle
import pandas as pd

page_bg_img = '''
<style>
.stApp {
  background: 
    /* Top-heavy gradient (dark at the top) */
    linear-gradient(
      to bottom,
      rgba(0, 0, 0, 0.95) 0%, 
      rgba(0, 0, 0, 0.6) 100%, 
      rgba(0, 0, 0, 0.2) 100%, 
      rgba(0, 0, 0, 0.0) 100%
    ),

    /* Vignette around edges */
    radial-gradient(
      ellipse at center,
      rgba(0,0,0,0) 60%,
      rgba(0,0,0,0.5) 100%
    ),

    /* Actual background image */
    url("https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");

  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
}
</style>
'''
import streamlit as st

st.markdown(page_bg_img, unsafe_allow_html=True)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        #fetch posters unable to do so #beacuse ISP are not allowing access to TMDB!
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# --- Load data ---
movies_dict = pickle.load(open('movies_Dict.pkl', 'rb'))   # Keep full dataframe
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


# --- Streamlit UI ---

# Insert this right above or below your title code
import streamlit as st

st.markdown("""
    <style>
    /* Selectbox container */
    div[data-baseweb="select"] {
        background-color: rgba(0, 0, 0, 0.6) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 6px;
    }

    /* Selected text in collapsed view */
    div[data-baseweb="select"] div[role="button"] {
        color: white !important;
    }

    /* Deep targeting for selected text */
    div[data-baseweb="select"] div[role="button"] > div {
        color: white !important;
    }

    /* Placeholder and dropdown arrow */
    div[data-baseweb="select"] div[role="button"] span,
    div[data-baseweb="select"] div[role="button"] svg {
        color: white !important;
    }

    /* Label above the box */
    label {
        font-size: 18px !important;
        color: white !important;
    }

    /* Dropdown menu items */
    ul[role="listbox"] {
        background-color: #111 !important;
        color: white !important;
    }

    ul[role="listbox"] li {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)





st.markdown(
    '<h1 style="color:white; font-size: 64px; font-weight: 900; font-family: Arial, Helvetica, sans-serif;">Movie Recommender</h1>',
    unsafe_allow_html=True
)

selected_movie_name = st.selectbox(
    "What kind of movie you are looking for?",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



