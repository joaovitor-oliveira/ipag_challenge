FROM python:3.9-slim

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./.github .
COPY ./challenge_01 .
COPY ./challenge_02 .
COPY ./challenge_03 .
COPY ./challenge_04 .
COPY ./challenge_05 .
COPY ./challenge_06 .
COPY ./challenge_07 .
COPY ./challenge_08 .
COPY ./challenge_09 .
COPY ./challenge_10 .
COPY ./.flake8 .
COPY ./.gitignore .
COPY ./.coveragerc .
COPY ./README.md .
COPY ./requirements.txt .
COPY ./sonar-project.properties .
COPY ./tox.ini .


CMD ["tail", "-f", "/dev/null"]