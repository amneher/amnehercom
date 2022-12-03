# pull official base image
FROM ubuntu

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3-pip tzdata nginx uwsgi postgresql-client postgresql-server-dev-all
RUN pip3 install --upgrade pip wheel
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY . .

# nginx conf file
RUN cp sundry/nginx.conf /etc/nginx/sites-available/amneher.conf
RUN ln -s /etc/nginx/sites-available/amneher.conf /etc/nginx/sites-enabled/amneher.conf

# uwsgi conf file
RUN cp sundry/uwsgi.ini /etc/uwsgi/apps-available/amneher.ini
RUN ln -s /etc/uwsgi/apps-available/amneher.ini /etc/uwsgi/apps-enabled/amneher.ini

EXPOSE 80

ENTRYPOINT exec python3 setup.py