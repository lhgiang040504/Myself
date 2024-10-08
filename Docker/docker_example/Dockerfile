FROM ubuntu

WORKDIR /src

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-sklearn

COPY code.py ./code.py

CMD [ "python3", "code.py"]