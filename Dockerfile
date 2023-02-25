FROM ubuntu
FROM python:3.10

MAINTAINER ShadyLaz "ShadyLaz"

# Update aptitude with new repo.
RUN apt-get update

# Install software
RUN apt-get install -y git

WORKDIR app/

COPY . .
RUN git clone https://github.com/Nergan123/UAC_rover.git
RUN rm UAC_rover/requirements.txt
RUN mv UAC_rover/* .
RUN pip install -r requirements.txt
RUN pylint ./**/*.py
CMD ["python", "tests_main.py"]


