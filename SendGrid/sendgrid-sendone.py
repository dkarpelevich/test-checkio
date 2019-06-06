import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content
from SendGrid import API_KEY
SUBJECT = 'Welcome'
BODY = 'Hi {}'

def send_email(email, name):
    message = Mail(
        from_email='from_email@example.com',
        to_emails='to@example.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content=BODY.format(name))
    try:
        sg = sendgrid.SendGridAPIClient(api_key=API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
