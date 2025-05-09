from django.core.management.base import BaseCommand
from django.utils import timezone
from reservations.models import TheReservation
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import timedelta


class CommandB(BaseCommand):
    help = 'Send email reminders for reservations in the next 24 hours'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        upcoming = now + timedelta(hours=24)
        reservations = TheReservation.objects.filter(
            start_time__gte=now,
            start_time__lte=upcoming
        )

        for res in reservations:
            ctx = {'reservation': res}
            subject = 'Reminder: Upcoming Reservation'
            text_body = render_to_string('emails/reminder_email.txt', ctx)
            html_body = render_to_string('emails/reminder_email.html', ctx)
            send_mail(subject, text_body, None, [res.user.email], html_message=html_body)
            self.stdout.write(f'Reminder sent to {res.user.email}')
