FROM python:3.11.3-alpine

WORKDIR /mediplant

COPY . /mediplant/

RUN pip install -r requirements.txt

EXPOSE 4000

CMD [ "uvicorn", "--reload", "--port", "4000", "app.main:app" ]