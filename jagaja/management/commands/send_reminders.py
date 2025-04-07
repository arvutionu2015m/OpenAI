from django.core.management.base import BaseCommand
from django.utils import timezone
from jagaja.models import Ülesanne
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Saadab meeldetuletused ülesannete kohta, mille tähtaeg on täna või möödas'

    def handle(self, *args, **kwargs):
        täna = timezone.now().date()
        ülesanded = Ülesanne.objects.filter(tähtaeg__lte=täna)

        for ülesanne in ülesanded:
            kasutaja = ülesanne.kasutaja
            if kasutaja.email:
                send_mail(
                    subject='Meeldetuletus: Ülesande tähtaeg',
                    message=f'Tere {kasutaja.username},\n\nSinu ülesande "{ülesanne.pealkiri}" tähtaeg oli {ülesanne.tähtaeg}.',
                    from_email=None,
                    recipient_list=[kasutaja.email]
                )
                self.stdout.write(self.style.SUCCESS(f'Saadetud: {kasutaja.email}'))
