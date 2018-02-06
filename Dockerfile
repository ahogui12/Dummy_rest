FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY api.py /
WORKDIR /
RUN pip install Flask
ENV FLASK_APP /api.py
CMD ["python", "/api.py"]
