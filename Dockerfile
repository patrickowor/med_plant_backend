FROM cnstark/pytorch:2.0.1-py3.10.11-ubuntu22.04
WORKDIR /mediplant

COPY . /mediplant/

RUN pip install -r requirements.txt

EXPOSE 4000

CMD [ "uvicorn", "--reload", "--port", "4000", "app.main:app" ]