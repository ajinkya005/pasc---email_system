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




docs = db.collection('Combined').stream()



def send_email(email,message):
    print('Sending Mail to '+email)
    # reciever = email
    reciever = "ajinkyakulkarni300@gmail.com"
    sender = "testcertificate211@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = reciever
    msg['Subject'] = "Thanks for participating in PULZION 2019!"
    body = "Congratulations for participating in PULZION 2019. Following are your event details: \n"
    temp = ""
    for key,val in message.items():
        temp = key + " : " + val + '\n'
        body += temp
    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, "root@123")
    text = msg.as_string()
    s.sendmail(sender, reciever, text)
    s.quit()

def emailChecked(event_name,id):
    docs = db.collection(event).where('id','==',id).stream()
    for doc in docs:
        city_ref = db.collection(event).document(doc.id)
        city_ref.set({
            u'email_sent': True
        }, merge=True)

# event_name = ['BugOff' , 'Cerebro' , 'Code_Buddy' , 'Combined' 'DC' , 'DataQuest' , 'Dextrous' , 'ElectroQuest' , 'Event_Details' , 'Friends' , 'GOT' , 'Harry_Potter' , 'Insight' , 'JustCoding' , 'Marvel' , 'Photoshop_Royale' , 'Quiz2Bid' , 'Recode_It' , 'Web_&_App_Development']


sendData = {}
for doc in docs:

    data = doc.to_dict()
    user_email = data['mail']
    user_name1 = data['participant1']
    user_id = data['id']
    user_college = data['collegeName']
    events = data['events']

    for event in events:
        status = False
        event_collection =  db.collection(event)
        event_coll_data = event_collection.where('id','==',user_id).stream()

        for xyz in event_coll_data:
            abc = xyz.to_dict()
            if 'email_sent' in abc.keys():
                status = True
            sendData[event] = abc['slot']
    if status == False:
        send_email(user_email,sendData)
        emailChecked(event,user_id)
    else:
        print("email already sent to " + user_email + '\n')
    sendData.clear()
    print("\n")



    # print(event[0])
