import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image, ImageDraw, ImageFont
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("pascregistrationappdemo-firebase-adminsdk-db0o6-f51fd3003b.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

wordFreqDic = {
    "Hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 43
    }
print(wordFreqDic)
