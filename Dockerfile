#Build image starting with...
FROM python:3

MAINTAINER Robin 'robinmcgregor@gmail.com'

#Mounts volume?
ADD . /3D_houses

#Set working directory
WORKDIR /3D_houses

#Set environment variables
ENV FLASK_APP 3D_house_app.py
ENV FLASK_RUN_HOST 0.0.0.0

#Install gcc and dependencies
#RUN apk add --no-cache gcc muscl-dev linux-headers

#Copy python libraries required
COPY requirements.txt requirements.txt

#Install python libraries required 
RUN pip install -r requirements.txt

#Add image metadata to show the listening port of the container
EXPOSE 5000

#Copy current directory to image container directory
COPY . .

#CMD ['python', '3D_house_app.py']
CMD ['Flask', 'run']
