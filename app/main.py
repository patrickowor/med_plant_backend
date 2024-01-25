from fastapi import FastAPI, Form, File, UploadFile, Depends, Request, Response
from pydantic import BaseModel
from ultralytics import YOLO
import os
import numpy as np
import cv2
from app.db import init_db, get_session, AsyncSession
from sqlmodel import select
from app.models import *
from app.authentication import auth_handler


MODEL_LOCATION = os.path.join(os.getcwd(), 'best.pt')
# MODEL_Weight = os.path.join(os.getcwd(), 'yolov8n.pt')


app = FastAPI()
model = YOLO(MODEL_LOCATION)
# model2 = YOLO(MODEL_Weight)


class Login(BaseModel):
    email : str
    password : str 


@app.post("/login")
async def login(
    data : Login,
    request : Request,
    session : AsyncSession = Depends(get_session)
    ):
    try:
        user_or_none = (await session.execute(select(User).where(User.email == data.email))).first()
        if user_or_none is None:
            user = User(name = "", email = data.email, password=auth_handler.get_password_hash(data.password))
            session.add(user)
            await session.commit()
        else:
            user = user_or_none[0]
            if  not (auth_handler.verify_password(data.password, user.password)):
                return {"success" : False , "message" : "wrong password!" } 
        token = auth_handler.encode_token(data.email)
        return {"success" : True , "message" : token}
    except:
        return {"success" : False , "message" : "failed!" } 

@app.post("/upload")
async def upload(image: UploadFile,
        response : Response,
                 ):
    try:
        nparr = np.frombuffer(image.file.read(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (64, 64))
        # r1 = model2(image)
        # return r1[0].names
        result = model(image, conf=0.99)
        return {"success" : True , "message" : result[0].names[result[0].probs.top1] } 
    except :
        return {"success" : False , "message" : "failed!" } 

@app.on_event("startup")
async def on_startup():
    

    pass
    # init_db()       
