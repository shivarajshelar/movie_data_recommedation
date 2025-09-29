# Python Base Image 
FROM python:3.12-slim

# Working dir for the container
WORKDIR /app

# Copy the lib list in docker image dir list
COPY requirement.txt  /app/requirement.txt  

# install build tools 
RUN pip install -r /app/requirement.txt

# rest thing copy 
COPY app.py  /app/app.py
COPY similar_movies.pkl  /app/similar_movies.pkl
COPY movie.csv .

# gradio default port 
EXPOSE 7860

# Gradio server
ENV GRADIO_SERVER_NAME="0.0.0.0"

# command need to run:7860 
CMD ["python", "app.py"]

