
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_id',
            field=models.IntegerField(default=0),
        ),
    ]
