FROM python:3.6

MAINTAINER Logan Lasiter

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/app

ENTRYPOINT ["python"]
CMD ["app.py"]