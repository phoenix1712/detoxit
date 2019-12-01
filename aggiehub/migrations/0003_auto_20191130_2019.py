# Generated by Django 3.1 on 2019-11-30 20:19

from django.db import migrations

def create_users(apps, schema_editor):
    
    User = apps.get_model("aggiehub", "User")
    db_alias = schema_editor.connection.alias
    
    User.objects.using(db_alias).bulk_create([
        User(name="Aditya", email="aditya@tamu.edu"),
        User(name="Vihang", email="vihang@tamu.edu"),
        User(name="Varsha", email="varsha@tamu.edu"),
        User(name="Yashwant", email="yashwant@tamu.edu"),
        User(name="Akhila", email="akhila@tamu.edu"),
        User(name="Aswin", email="aswin@tamu.edu"),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('aggiehub', '0002_auto_20191130_1644'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]

