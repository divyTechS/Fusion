from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_cms", "0002_gradingscheme_studentevaluation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursedocuments",
            name="document_url",
            field=models.TextField(blank=True, null=True),
        ),
    ]
