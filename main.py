from typing import List
from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import dotenv_values
credentials= dotenv_values(".env")
class EmailSchema(BaseModel):
    email: List[EmailStr]
class EmailContent(BaseModel):
    title: str
    content: str
    type : str
# PASS = Abcd!3JKNDnn
conf = ConnectionConfig(
    MAIL_USERNAME = credentials['MAIL_USERNAME'],
    MAIL_PASSWORD = credentials['MAIL_PASSWORD'],
    MAIL_FROM = credentials['MAIL_FROM'],
    MAIL_PORT = credentials['MAIL_PORT'],
    MAIL_SERVER = credentials['MAIL_SERVER'],
    MAIL_STARTTLS = credentials['MAIL_STARTTLS'],
    MAIL_SSL_TLS = credentials['MAIL_SSL_TLS'],
    USE_CREDENTIALS = credentials['USE_CREDENTIALS'],
)

app = FastAPI()


@app.post("/email")
async def send_email(email: EmailSchema, content: EmailContent):
    html = f"""
    <h1>Test Test</h1>
    <h2>Tessst</h2>    
    <br>
    <p>{content.content}</p>
    <br>
    <p>Best regard!</p> 
    """
    
    if content.type =='html':
        html=f'{content.content}'
        message = MessageSchema(
        subject=content.title,
        recipients=email.dict().get("email"),
        body=html,
        subtype='html')

    fm = FastMail(conf)
    await fm.send_message(message)
    return {'status': 'ok'}
