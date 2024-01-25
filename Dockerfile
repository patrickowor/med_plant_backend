FROM cnstark/pytorch:2.0.1-py3.10.11-ubuntu22.04
WORKDIR /mediplant

COPY . /mediplant/
RUN apt-get update && apt-get install -y libgl1

RUN pip install -U opencv-python
RUN apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx
RUN pip install -r requirements.txt

EXPOSE 4000

CMD [ "uvicorn", "--reload", "--port", "4000", "app.main:app" ]