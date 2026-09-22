from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_adslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='section',
            field=models.CharField(choices=[('useful_links', 'Links úteis'), ('how_to', 'Como solicitar'), ('phones', 'Telefones úteis'), ('addresses', 'Endereços'), ('videos', 'Vídeos'), ('whatsapp_accommodation', 'WhatsApp (acomodação)'), ('job_sites', 'Sites de emprego'), ('fb_jobs_group', 'Grupos de emprego (Facebook)'), ('daily_apps', 'Apps úteis')], max_length=32),
        ),
    ]
