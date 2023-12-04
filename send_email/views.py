from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView


class CheckEmailCode(APIView):
    def post(self, request):
        name = request.data["name"]
        email = request.data["email"]
        phone = request.data["phone"]
        purpose = request.data["purpose"]
        description = request.data["description"]

        send_mail(
            "prountiy.uz",
            f"Name: {name}, email: {email}, phone: {phone}, purpose: {purpose}, description: {description}",
            "istamovibrohim8@gmail.com",
            [email],
            fail_silently=False,
        )
        return Response({"message": "Send message"})
