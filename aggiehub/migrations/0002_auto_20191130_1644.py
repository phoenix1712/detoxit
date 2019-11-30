# Generated by Django 3.1 on 2019-11-30 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aggiehub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('CLAIM_TOXIC', 'Claim Toxic'), ('CLAIM_NONTOXIC', 'Claim Non-Toxic'), ('TOXIC', 'Toxic')], default='TOXIC', max_length=20)),
                ('notif_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggiehub.User')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='survey',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Toxic',
        ),
    ]
