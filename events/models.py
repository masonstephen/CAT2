from django.db import models
from django.contrib.auth.models import User

def get_default_user():
    return User.objects.first().id if User.objects.exists() else 1

class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=get_default_user)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Added price for event
    
    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view_event", "Can view event"),
            ("can_edit_event", "Can edit event"),
        ]

class Attendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=get_default_user)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField(Event, through='Ticket')
    
    def __str__(self):
        return self.name

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('canceled', 'Canceled'),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
    def __str__(self):
        return f'{self.attendee} - {self.event}'

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review for {self.event.title} by {self.user.username}'
