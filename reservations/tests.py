from django.test import TestCase

# Create your tests here.

class ReservationTesting(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.room = Room.objects.create(name='Test Room', capacity=10)
        self.reservation = Reservation.objects.create(user=self.user, room=self.room, start_time='2022-01-01 10:00:00', end_time='2022-01-01 11:00:00')
