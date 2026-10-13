from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_autoridad_delete_documento_delete_evento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='titulo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]