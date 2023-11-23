FROM ubuntu:latest
LABEL authors="hadi"

ENTRYPOINT ["top", "-b"]