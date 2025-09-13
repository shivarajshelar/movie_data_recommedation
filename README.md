# movie_recommedation 

### Example pic of Recommend photo


![Movie Recommender Screenshot](images/demo1.png)

![Movie Recommender Screenshot](images/demo2.png)

![Movie Recommender Screenshot](images/demo3.png)




### Create and activate a virtual environment
```
conda create -p rec_venv python==3.12 -y

conda activate rec_venv/

```
### install dependencies
```
pip install -r requirements.txt

```
### Git commands

```
1. git init

2. git add .  or git add README.md notebook text files

3. git commit -m "first commit"

4. git remote remove origin

5. git add origin https://github.com/shivarajshelar/movie_data_recommedation.git

6. git remote -v

7. git branch -M main

8. git push -u origin

```

using sckit learn

doing the count vector to store data

from sklearn.feature_extraction.text import CountVectorizer


from sklearn.metrics.pairwise import cosine_similarity

to seach top 5 movies on the basis of the similrity

