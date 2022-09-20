# manual migration

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Post',
            name='title',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
    ]
