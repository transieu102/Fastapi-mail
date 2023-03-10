from typing import List
from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from typing import Union
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
class User(BaseModel):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
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
# async def send_email(email: EmailSchema, content: EmailContent,user:User | None = None): #python 3.10
async def send_email(email: EmailSchema, content: EmailContent,user:Union[User, None] = None):
    config=conf
    if user:
        config = ConnectionConfig(
        MAIL_USERNAME = user.MAIL_USERNAME,
        MAIL_PASSWORD = user.MAIL_PASSWORD,
        MAIL_FROM = credentials['MAIL_FROM'],
        MAIL_PORT = credentials['MAIL_PORT'],
        MAIL_SERVER = credentials['MAIL_SERVER'],
        MAIL_STARTTLS = credentials['MAIL_STARTTLS'],
        MAIL_SSL_TLS = credentials['MAIL_SSL_TLS'],
        USE_CREDENTIALS = credentials['USE_CREDENTIALS'],)
    html = f"""
    <p>{content.content}</p>
    """
    if content.type =='html':
        html=f'{content.content}'
    message = MessageSchema(
    subject=content.title,
    recipients=email.dict().get("email"),
    body=html,
    subtype='html')

    fm = FastMail(config)
    await fm.send_message(message)
    return {'status': 'ok'}
