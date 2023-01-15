from django.core.mail.message import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ConfirmEmail
from datetime import datetime

class Util:
    @staticmethod
    def send_mail(message):
        email = EmailMessage(subject=message["email_subject"], body=message["email_body"], to=[message["to_email"]]) # 제목, 내용, 보낼 사람
        email.send()    
    
    def email_authentication_send(user):
        secured_key = RefreshToken.for_user(user).access_token # refresh token 중에서 access_token을 발급 >> access_token 발급
        print(secured_key["exp"])
        expired_at = datetime.fromtimestamp(secured_key["exp"]).strftime("%Y-%m-%dT%H:%M:%S") # 13 안에 expired가 있는데, 1673768558 << unixtimestamp을 str로 바꿔준 것

        ConfirmEmail.objects.create(secured_key=secured_key, expired_at=expired_at, user=user)

        domain_site = "" 
        absurl = f"http://{domain_site}?secured_key={str(secured_key)}"
        email_body = "안녕하세요!" + user.email +"고객님 이메일인증을 하시려면 아래 사이트를 접속해주세요 \n" + absurl
        message = {
                "email_body": email_body,
                "to_email": user.email,
                "email_subject": "이메일 인증",
            }
        Util.send_mail(message)