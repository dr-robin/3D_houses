# 3D_houses

3D House Project

The goal of the project is to generate a model house in 3D from any address in Flanders, Belgium.

Features to be added: 
* 3D lookup of houses.

To install docker:
sudo apt-get update
sudo apt-get install 3.7.6 docker-ce docker-ce-cl:containerd.io

Activate venv environment:
cd flask-venv
. flask-venv/bin/activate

To build docker:
docker build -t flask-sample:latest

To run docker container:
docker run -d -p 5000:5000 flask-sample

Check docker container is running:
docker ps -a

Start flask app:
export FLASK_APP = 3D_house_app.py

Stop docker container and remove images
docker stop $(docker ps -a -q)
docker system prune
