from django.core.mail import EmailMessage


class Util:
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email="jobaergaibandha@gmail.com",
      to=[data['to_email']]
    )
    email.send()