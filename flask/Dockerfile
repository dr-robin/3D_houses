FROM python:3
MAINTAINER Robin 'robinmcgregor@gmail.com'
WORKDIR /home/becode/dr-robin/fl
COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ['python','3Dhouseapp.py']
