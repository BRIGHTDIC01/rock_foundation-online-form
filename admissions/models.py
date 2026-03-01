from django.db import models

class Application(models.Model):

    VOCATION_CHOICES = [
        ('BAKING', 'BAKING'),
        ('CATERING', 'CATERING'),
        ('INTERLOCK', 'INTERLOCK'),
        ('BARBING', 'BARBING'),
        ('HAIRDRESSING', 'HAIRDRESSING'),
        ('PAINTING', 'PAINTING'),
        ('ART AND CRAFTS', 'ART AND CRAFTS'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    RELATIONSHIP_CHOICES = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Guardian', 'Guardian'),
        ('Sponsor', 'Sponsor'),
    ]

    HEALTH_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
    ]

    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    dob = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=100)

    class_of_entry = models.CharField(max_length=50)
    home_address = models.TextField()
    state_of_residence = models.CharField(max_length=100)

    guardian_name = models.CharField(max_length=200)
    guardian_relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)
    guardian_phone = models.CharField(max_length=20)
    guardian_email = models.EmailField()
    guardian_occupation = models.CharField(max_length=100)

    previous_school = models.CharField(max_length=200)
    school_address = models.TextField()
    last_class = models.CharField(max_length=50)
    reason_for_leaving = models.TextField()

    health_issues = models.CharField(max_length=10, choices=HEALTH_CHOICES)
    health_details = models.TextField(blank=True)

    vocational_skill = models.CharField(max_length=50, choices=VOCATION_CHOICES)

    career_aspiration = models.CharField(max_length=100)
    extracurricular = models.CharField(max_length=200)
    how_heard = models.CharField(max_length=200)
    additional_comments = models.TextField()

    payment_proof = models.FileField(upload_to='payment_proofs/')
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.surname} {self.first_name}"