
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(default='', max_length=30)),
                ('car_desc', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='car/images')),
            ],
        ),
    ]
