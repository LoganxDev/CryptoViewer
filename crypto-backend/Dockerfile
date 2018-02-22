FROM python:3.6

MAINTAINER Logan Lasiter

COPY . /usr/src/app
WORKDIR /usr/src/app

# add requirements
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]