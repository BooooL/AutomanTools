# Generated by Django 2.2.2 on 2019-08-28 04:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('originals', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('file_path', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=100)),
                ('delete_flag', models.BooleanField(default=False)),
                ('frame_count', models.IntegerField(default=-1)),
                ('original', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_rosbag', to='originals.Original')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='DatasetDatasetCandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.LabelDataset')),
                ('dataset_candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='originals.DatasetCandidate')),
            ],
        ),
    ]
