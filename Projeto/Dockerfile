FROM python:3.6.8

LABEL author = Paulo Nunes

LABEL version = 1.0

WORKDIR /projeto

COPY . .

RUN apk add py3-pip; pip3 install --upgrade pip

RUN pip3 install -r requisitos.txt

EXPOSE 5000

CMD ["flask", "run"]