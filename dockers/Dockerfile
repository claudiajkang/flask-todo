FROM python:3.5
MAINTAINER Claudia J.Kang <claudiajkang@gmail.com>

RUN apt update -y
RUN apt install -y vim tmux

ARG proj
ENV PROJ_PATH /app/${proj}

RUN git clone https://github.com/ClaudiaJKang/flask-todo.git ${PROJ_PATH}
WORKDIR ${PROJ_PATH}

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
