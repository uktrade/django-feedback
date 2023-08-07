# Generated by Django 4.1.10 on 2023-08-07 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_feedback_govuk', '0004_alter_basefeedback_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomFeedback',
            fields=[
                ('basefeedback_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_feedback_govuk.basefeedback')),
                ('satisfaction', models.CharField(choices=[('very_dissatisfied', 'Very dissatisfied'), ('dissatisfied', 'Dissatisfied'), ('neutral', 'Neither satisfied or dissatisfied'), ('satisfied', 'Satisfied'), ('very_satisfied', 'Very satisfied')], max_length=30)),
                ('comment', models.TextField(blank=True)),
                ('extra_comments', models.TextField(blank=True)),
            ],
            bases=('django_feedback_govuk.basefeedback',),
        ),
    ]
