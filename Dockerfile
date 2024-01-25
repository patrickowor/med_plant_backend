FROM python:3.11.3-alpine

WORKDIR /mediplant

COPY . /mediplant/

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install -r requirements.txt

EXPOSE 4000

CMD [ "uvicorn", "--reload", "--port", "4000", "app.main:app" ]