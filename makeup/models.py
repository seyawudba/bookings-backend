from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.


class Promotions(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=300)
    start = models.DateTimeField()
    end = models.DateTimeField()
    expired = models.BooleanField(default=True)


class MakeUpArtist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio_experience = models.CharField(max_length=255)
    social_media_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username


class CertificationsAndPortfolio(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(MakeUpArtist, on_delete=models.CASCADE)
    cert_image = models.ImageField(upload_to="makeup/certifications/")
    portfolio_image = models.ImageField(upload_to="makeup/portfolios/")


class Services(models.Model):
    SERVICE_AVAILABLE = "AVAILABLE"
    SERVICE_UNAVAILABLE = "UNAVAILABLE"
    SERVICE_COMING_SOON = "COMING_SOON"

    AVAILABILITY = [
        (SERVICE_AVAILABLE, "Available"),
        (SERVICE_UNAVAILABLE, "Unavailable"),
        (SERVICE_COMING_SOON, "Coming Soon"),
    ]
    availability = models.CharField(max_length=20, choices=AVAILABILITY, default=SERVICE_AVAILABLE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    promotions = models.ManyToManyField(Promotions)
    duration = models.DurationField()


class Clients(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Bookings(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date_needed = models.DateField()
    time_booked = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)


class Products(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promotions = models.ManyToManyField(Promotions)


class Reviews(models.Model):
    COMMENT_REVIEW = "REVIEW"
    TESTTIMONIAL_REVIEW = "TESTIMONIAL"

    COMMENT_TYPE = [
        (COMMENT_REVIEW, "REVIEW"),
        (TESTTIMONIAL_REVIEW, "TESTIMONIAL"),
    ]
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=55)
    content = models.CharField(max_length=300)
    review_type = models.CharField(max_length=55, choices=COMMENT_TYPE, default=TESTTIMONIAL_REVIEW)
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class BlogArticle(models.Model):
    BLOG = "B"
    ARTICLE = "A"
    CONTENT_TYPE = ((BLOG, "BLOG"), (ARTICLE, "ARTICLE"))
    title = models.CharField(max_length=55)
    content = models.CharField(max_length=300)
    content_type = models.CharField(max_length=15, choices=CONTENT_TYPE, default=ARTICLE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    label = models.CharField(max_length=25)
    description = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)


class ContactForm(models.Model):
    GENERAL = "G"
    BOOKINGS = "B"
    PARTNERSHIP = "P"

    INQUIRY_TYPE = [(GENERAL, "GENERAL"), (BOOKINGS, "BOOKING"), (PARTNERSHIP, "PARTNERSHIP")]
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=55)
    message = models.CharField(max_length=300)
    inquiry_type = models.CharField(choices=INQUIRY_TYPE, default=GENERAL, max_length=55)
