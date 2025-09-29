import pandas as pd
import joblib 
import gradio as gr
from urllib.parse import quote
import requests, re
from bs4 import BeautifulSoup


## Image Extraction of Movies 
def wiki_poster(movie):
    title = movie.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{title}"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, "html.parser")
    infobox = soup.find("table", {"class": "infobox"})

    img = infobox.find("img") if infobox else None
    no_image = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg"

    return "https:" + img["src"] if img else no_image

movie = pd.read_csv('movie.csv')

## ML model 
similar_movies = joblib.load('similar_movies.pkl')

## All movies name 
movie_name = movie['names'].value_counts().index.str.strip().to_list()


## Recommadation function
def recommandation_movie(movie_name,k):

    movie_index = int(movie[movie['names'] == movie_name].index[0])
    
    similarity_scores = list(enumerate(similar_movies[movie_index]))

    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    similarity_scores = [(i, float(score)) for i, score in similarity_scores]

    top_n = similarity_scores[1:k+1] 

    recommendations = [movie.iloc[i[0]]['names'] for i in top_n]
    genre = [movie.iloc[i[0]]['genre'] for i in top_n]
    
    poster = [[wiki_poster(i),i] for i in recommendations]

    #df = pd.DataFrame({'recommandation_movie':recommendations , 'genre':genre , 'poster':poster } )
    return poster 

## UI 

theme = gr.themes.Glass(primary_hue="red",neutral_hue="indigo").set(
    body_background_fill_dark="#000000", 
    body_text_color_dark="#e5e7eb"        
)

with gr.Blocks(theme=theme, title="Movie Recommender") as demo:
    gr.Markdown("## Movie Recommender")
    inp = gr.Dropdown(movie_name, label="Pick a movie",value=movie_name[0] if movie_name else None)
    k = gr.Slider(1, 5, value=5, label="Number of recommendations")
    btn = gr.Button("Recommend")
    gallery = gr.Gallery(label="Movie Posters", show_label=True,columns=5, height="auto", object_fit="contain")

    btn.click(recommandation_movie, inputs=[inp, k], outputs=[gallery])


demo.launch()




