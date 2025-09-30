# movie_recommedation 

### first Example pic of Recommend photo on Local System
![Movie Recommender Screenshot](images/demo4.png)

### Second Example pic of Recommend photo local system
![Movie Recommender Screenshot](images/demo6.png)

### Third Example pic of Recommend photo AWS instance ec2 system 
![Movie Recommender Screenshot](images/demo8.png)

### Fourth Example pic of Recommend photo AWS instance ec2 system 
![Movie Recommender Screenshot](images/demo7.png)



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

5. git remote add origin https://github.com/shivarajshelar/movie_data_recommedation.git

6. git remote -v

7. git branch -M main

8. git push -u origin main 

```
## Library are used for this project

1. Pandas
2. Numpy
3. scikit-learn
4. Gradio

##  Dockerize command file and Push to docker from Local system
```
docker build -t mass19/movie_sub .

docker run -p 7860:7860 mass19/movie_sug

docker push mass19/movie_sug:lastest

local machine address --> http://127.0.0.1:7860

```

## AWS EC2 Command to install docker 

```
Create EC2 instance 

Connect to intance

sudo apt-get update 

sudo apt-get install -y docker.io

sudo systemctl start docker 

sudo systemctl enable docker 

sudo usermode -aG docker $USER  -- give the permission to ec2 for the pull docker images

exit

Restart Connection

docker pull mass19/movie_sug:latest

docker run -p 7860:7860 mass19/movie_sug

http://13.60.85.218:7860/   this is aws ec2 public ip address

```

## How it works

First, the **CountVectorizer** method is applied to convert the text data (such as genres, keywords, or movie descriptions) into a numerical format. This creates a "bag of words" representation where each movie is stored as a vector of word counts.  

Next, **cosine similarity** is used to measure how close or similar two movies are based on their text vectors. Movies with higher similarity scores share more common features in their descriptions.  

Finally, for any given movie, the system compares it with all other movies and returns the **top 5 most similar movies** as recommendations.

