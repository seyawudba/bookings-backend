# Generated by Django 5.0.8 on 2024-08-25 09:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Certificate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("cert_image", models.ImageField(upload_to="makeup/certifications/")),
            ],
        ),
        migrations.CreateModel(
            name="ContactForm",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=55)),
                ("message", models.CharField(max_length=300)),
                (
                    "inquiry_type",
                    models.CharField(
                        choices=[("G", "GENERAL"), ("B", "BOOKING"), ("P", "PARTNERSHIP")], default="G", max_length=55
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("portfolio_image", models.ImageField(upload_to="makeup/portfolios/")),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("artist_image", models.ImageField(upload_to="makeup/artists/")),
            ],
        ),
        migrations.CreateModel(
            name="Promotion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=55)),
                ("description", models.CharField(max_length=300)),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                ("expired", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("label", models.CharField(max_length=25)),
                ("description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
                (
                    "profile_pic",
                    models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to="makeup.profile"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("phone_number", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("location", models.CharField(max_length=255)),
                ("date_needed", models.DateField()),
                ("time_booked", models.DateTimeField(auto_now_add=True)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="makeup.client"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MakeUpArtist",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("bio_experience", models.CharField(max_length=255)),
                ("social_media_link", models.URLField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BlogArticle",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=55)),
                ("content", models.CharField(max_length=300)),
                (
                    "content_type",
                    models.CharField(choices=[("B", "BLOG"), ("A", "ARTICLE")], default="A", max_length=15),
                ),
                ("date_submitted", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="makeup.makeupartist")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=55)),
                ("description", models.CharField(max_length=1000)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("promotions", models.ManyToManyField(to="makeup.promotion")),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=55)),
                ("content", models.CharField(max_length=300)),
                (
                    "review_type",
                    models.CharField(
                        choices=[("REVIEW", "REVIEW"), ("TESTIMONIAL", "TESTIMONIAL")],
                        default="TESTIMONIAL",
                        max_length=55,
                    ),
                ),
                ("date_submitted", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "client",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="makeup.client"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "availability",
                    models.CharField(
                        choices=[
                            ("AVAILABLE", "Available"),
                            ("UNAVAILABLE", "Unavailable"),
                            ("COMING_SOON", "Coming Soon"),
                        ],
                        default="AVAILABLE",
                        max_length=20,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=1000)),
                ("pricing", models.DecimalField(decimal_places=2, max_digits=6)),
                ("duration", models.DurationField()),
                ("promotions", models.ManyToManyField(to="makeup.promotion")),
                (
                    "provider",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="makeup.makeupartist"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaggedItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("object_id", models.PositiveSmallIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "content_type",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="contenttypes.contenttype"),
                ),
                ("tag", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="makeup.tag")),
            ],
        ),
    ]
