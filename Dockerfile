FROM python:3.10.6
LABEL authors="hadi"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR src
COPY ./requirments /requirements
COPY ./src /src

EXPOSE 8000
#RUN pip install --upgrade pip
RUN pip install -r /requirements/requirments.txt
