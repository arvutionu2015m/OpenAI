from django.core.management.base import BaseCommand
from jagaja.models import Ülesanne
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from jagaja.utils import soovita_olulised_ülesanded

class Command(BaseCommand):
    help = 'Saadab AI-põhised soovitused ja meeldetuletused kasutajatele'

    def handle(self, *args, **kwargs):
        kasutajad = User.objects.all()
        for kasutaja in kasutajad:
            ülesanded = Ülesanne.objects.filter(kasutaja=kasutaja, tähtaeg__isnull=False, alamülesanded__tehtud=False).distinct()
            if ülesanded.exists() and kasutaja.email:
                ai_vastus = soovita_olulised_ülesanded(ülesanded)
                send_mail(
                    subject='AI soovitab tänaseid tähtsaid ülesandeid',
                    message=f'Tere {kasutaja.username},\n\n{ai_vastus}',
                    from_email=None,
                    recipient_list=[kasutaja.email]
                )
                self.stdout.write(f'Saadetud AI-soovitused: {kasutaja.email}')
