FROM anibali/pytorch:2.0.1-cuda11.8-ubuntu22.04
WORKDIR /mediplant

COPY . /mediplant/

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

RUN pip install --upgrade setuptools pip
RUN pip install -r requirements.txt

EXPOSE 4000

CMD [ "uvicorn", "--reload", "--port", "4000", "app.main:app" ]