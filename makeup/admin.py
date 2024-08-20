from django.contrib import admin

from .models import (
    BlogArticle,
    Booking,
    CertificateImage,
    Client,
    ContactForm,
    MakeUpArtist,
    PortfolioImage,
    Product,
    Promotion,
    Review,
    Service,
)

# Register your models here.


@admin.register(MakeUpArtist)
class MakeUpArtistAdmin(admin.ModelAdmin):
    search_fields = ["user"]
    autocomplete_fields = ["user"]
    list_select_related = ["user"]


@admin.register(Promotion)
class PromoAdmin(admin.ModelAdmin):
    list_display = ["title", "start", "end", "expired"]


@admin.register(CertificateImage, PortfolioImage)
class UserFilesAdmin(admin.ModelAdmin):
    search_fields = ["artist"]
    list_display = ["title", "artist"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "availability", "description", "pricing", "duration"]
    list_select_related = ["promotions"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ["user"]
    autocomplete_fields = ["user"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    search_fields = ["client"]
    autocomplete_fields = ["client"]
    list_display = ["location", "date_needed", "time_booked"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "price"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "review_type"]


@admin.register(BlogArticle)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "content_type"]


@admin.register(ContactForm)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
