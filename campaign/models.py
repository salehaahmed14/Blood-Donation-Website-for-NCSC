from django.db import models
from django.contrib.auth.models import User

class Personal_Information(models.Model):
    person_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='person_id')
    dob = models.DateField()
    cnic = models.CharField(max_length=15)
    sex = models.CharField(max_length=6)
    address = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)

    def __str__(self):
        return (self.person_id.first_name + " " + self.person_id.last_name)

    class Meta:
        app_label = 'campaign'
        db_table = 'personal_information'

class Medical_Information(models.Model):
    person_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='person_id')
    blood_type = models.ForeignKey('Blood_Type', on_delete=models.RESTRICT, blank=False, db_column='blood_type')
    height = models.IntegerField()
    weight =  models.IntegerField()
    last_donation = models.DateField(null = True)
    campaign_id = models.ManyToManyField('Campaign', db_column='campaign_id', blank=True)

    def __str__(self):
        return (self.person_id.first_name + " " + self.person_id.last_name)

    class Meta:
        app_label = 'campaign'
        db_table = 'medical_information'

class Volunteer(models.Model):
    volunteer_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='volunteer_id')
    designation = models.CharField(max_length=20)
    campaign_id = models.ManyToManyField('Campaign', db_column='campaign_id')

    def __str__(self):
        return (self.volunteer_id.first_name + " " + self.volunteer_id.last_name)

    class Meta:
        app_label = 'campaign'
        db_table = 'volunteer'

class Blood_Type(models.Model):
    type = models.CharField(max_length=3, primary_key=True, db_column='type')
    compatible_types = models.CharField(max_length=25)

    def __str__(self):
        return self.type

    class Meta:
        app_label = 'campaign'
        db_table = 'blood_type'

class Blood_Record(models.Model):
    blood_type = models.ForeignKey(Blood_Type, on_delete=models.RESTRICT, db_column='blood_type')
    campaign_id = models.ForeignKey('Campaign', on_delete=models.RESTRICT, db_column='campaign_id')
    amount_collected = models.IntegerField()

    def __str__(self):
        return (self.campaign_id.title + " - Blood Group: " + str(self.blood_type))

    class Meta:
        app_label = 'campaign'
        db_table = 'blood_record'

class Campaign(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=50)
    donor_count = models.IntegerField(null=True)
    isActive = models.BooleanField(null=True)
    location_id = models.ForeignKey('Location', on_delete=models.RESTRICT, blank=False, db_column='location_id')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'campaign'
        db_table = 'campaign'

class Location(models.Model):
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address

    class Meta:
        app_label = 'campaign'
        db_table = 'location'

class Blood_Test(models.Model):
    test_name = models.CharField(max_length=30)
    test_description = models.CharField(max_length=100)

    def __str__(self):
        return self.test_name

    class Meta:
        app_label = 'campaign'
        db_table = 'blood_test'

class Performed_Test(models.Model):
    donor_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='donor_id')
    test_id = models.ForeignKey(Blood_Test, on_delete=models.CASCADE, db_column='test_id')
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE, db_column='campaign_id')
    result = models.CharField(max_length=8)

    def __str__(self):
        return (self.donor_id.first_name + " " + self.donor_id.last_name + " - " + self.test_id.test_name + " - " + str(self.campaign_id))

    class Meta:
        app_label = 'campaign'
        db_table = 'performed_test'

class Hospital(models.Model):
    name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=15)
    location_id = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=False, db_column='location_id')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'campaign'
        db_table = 'hospital'

class Blood_Bank(models.Model):
    name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=15)
    location_id = models.ForeignKey(Location, on_delete=models.RESTRICT, blank=False, db_column='location_id')


    def __str__(self):
        return self.name

    class Meta:
        app_label = 'campaign'
        db_table = 'blood_bank'

class Staff(models.Model):
    staff_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column='staff_id')
    cnic = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    campaign_id = models.ManyToManyField(Campaign, db_column='campaign_id')

    def __str__(self):
        return (self.staff_id.first_name + " " + self.staff_id.last_name)

    class Meta:
        app_label = 'campaign'
        db_table = 'staff'

class Doctor(models.Model):
    doctor_id = models.OneToOneField(Staff, on_delete=models.CASCADE, primary_key=True, db_column='doctor_id')
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return (self.doctor_id.staff_id.first_name + " " + self.doctor_id.staff_id.last_name)

    class Meta:
        app_label = 'campaign'
        db_table = 'doctor'

class HealthCare_Worker(models.Model):
    worker_id = models.OneToOneField(Staff, on_delete=models.CASCADE, primary_key=True, db_column='worker_id')
    designation = models.CharField(max_length=20)

    def __str__(self):
        return (self.worker_id.staff_id.first_name + " " + self.worker_id.staff_id.last_name)

    class Meta:
        app_label = 'campaign'
        db_table = 'healthcare_worker'

class Lab_Technician(models.Model):
    tech_id = models.OneToOneField(Staff, on_delete=models.CASCADE, primary_key=True, db_column='tech_id')
    test_assigned = models.ForeignKey(Blood_Test, on_delete=models.RESTRICT, db_column='test_assigned')

    def __str__(self):
        return (self.tech_id.staff_id.first_name + " " + self.tech_id.staff_id.last_name)

    class Meta:
        app_label = 'campaign'
        db_table = 'lab_technician'