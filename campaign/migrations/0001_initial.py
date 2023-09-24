# Generated by Django 4.1.4 on 2022-12-28 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=30)),
                ('test_description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'blood_test',
            },
        ),
        migrations.CreateModel(
            name='Blood_Type',
            fields=[
                ('type', models.CharField(db_column='type', max_length=3, primary_key=True, serialize=False)),
                ('compatible_types', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'blood_type',
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=50)),
                ('donor_count', models.IntegerField(null=True)),
                ('isActive', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'campaign',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Personal_Information',
            fields=[
                ('person_id', models.OneToOneField(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dob', models.DateField()),
                ('cnic', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'personal_information',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.OneToOneField(db_column='staff_id', default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cnic', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=15)),
                ('campaign_id', models.ManyToManyField(db_column='campaign_id', to='campaign.campaign')),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.OneToOneField(db_column='doctor_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='campaign.staff')),
                ('specialization', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='HealthCare_Worker',
            fields=[
                ('worker_id', models.OneToOneField(db_column='worker_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='campaign.staff')),
                ('designation', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'healthcare_worker',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('volunteer_id', models.OneToOneField(db_column='volunteer_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('designation', models.CharField(max_length=20)),
                ('campaign_id', models.ManyToManyField(db_column='campaign_id', to='campaign.campaign')),
            ],
            options={
                'db_table': 'volunteer',
            },
        ),
        migrations.CreateModel(
            name='Performed_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=8)),
                ('campaign_id', models.ForeignKey(db_column='campaign_id', on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
                ('donor_id', models.ForeignKey(db_column='donor_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('test_id', models.ForeignKey(db_column='test_id', on_delete=django.db.models.deletion.CASCADE, to='campaign.blood_test')),
            ],
            options={
                'db_table': 'performed_test',
            },
        ),
        migrations.CreateModel(
            name='Medical_Information',
            fields=[
                ('person_id', models.OneToOneField(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('last_donation', models.DateField(null=True)),
                ('blood_type', models.ForeignKey(db_column='blood_type', on_delete=django.db.models.deletion.RESTRICT, to='campaign.blood_type')),
                ('campaign_id', models.ManyToManyField(blank=True, db_column='campaign_id', to='campaign.campaign')),
            ],
            options={
                'db_table': 'medical_information',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=15)),
                ('location_id', models.ForeignKey(db_column='location_id', on_delete=django.db.models.deletion.RESTRICT, to='campaign.location')),
            ],
            options={
                'db_table': 'hospital',
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='location_id',
            field=models.ForeignKey(db_column='location_id', on_delete=django.db.models.deletion.RESTRICT, to='campaign.location'),
        ),
        migrations.CreateModel(
            name='Blood_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_collected', models.IntegerField()),
                ('blood_type', models.ForeignKey(db_column='blood_type', on_delete=django.db.models.deletion.RESTRICT, to='campaign.blood_type')),
                ('campaign_id', models.ForeignKey(db_column='campaign_id', on_delete=django.db.models.deletion.RESTRICT, to='campaign.campaign')),
            ],
            options={
                'db_table': 'blood_record',
            },
        ),
        migrations.CreateModel(
            name='Blood_Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=15)),
                ('location_id', models.ForeignKey(db_column='location_id', on_delete=django.db.models.deletion.RESTRICT, to='campaign.location')),
            ],
            options={
                'db_table': 'blood_bank',
            },
        ),
        migrations.CreateModel(
            name='Lab_Technician',
            fields=[
                ('tech_id', models.OneToOneField(db_column='tech_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='campaign.staff')),
                ('test_assigned', models.ForeignKey(db_column='test_assigned', on_delete=django.db.models.deletion.RESTRICT, to='campaign.blood_test')),
            ],
            options={
                'db_table': 'lab_technician',
            },
        ),
    ]
