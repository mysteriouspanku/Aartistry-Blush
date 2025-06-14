

# from django.db import models

# POST_TYPE_CHOICES = [
#     ('nailart', 'Nail Art'),
#     ('makeup', 'Make Up'),
#     ('productreview', 'Product Review'),
# ]

# def upload_path(instance, filename):
#     return f"{instance.post_type}/{filename}"  # dynamic folder

# class Posts(models.Model):
#     title = models.CharField(max_length=100)
#     image = models.ImageField(upload_to=upload_path)  # uses post_type folder
#     post_type = models.CharField(max_length=20, choices=POST_TYPE_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title


from django.db import models

POST_TYPE_CHOICES = [
    ('nailart', 'Nail Art'),
    ('makeup', 'Make Up'),
    ('productreview', 'Product Review'),
]

PLATFORM_CHOICES = [
    ('instagram', 'Instagram'),
    ('youtube', 'YouTube'),
]

def upload_path(instance, filename):
    return f"{instance.post_type}/{filename}"

class Posts(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_path)
    post_type = models.CharField(max_length=20, choices=POST_TYPE_CHOICES)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    background_gradient = models.CharField(max_length=255, default='linear-gradient(90deg,rgba(42, 123, 155, 1) 0%, rgba(87, 199, 133, 1) 50%, rgba(237, 221, 83, 1) 100%)')
    font_family = models.CharField(max_length=255, default='Arial, sans-serif')
    heading_color = models.CharField(max_length=100, default='#333')
    text_color = models.CharField(max_length=100, default='#555')

    def __str__(self):
        return "Site Settings"


# New model for Carousel Images
def carousel_upload_path(instance, filename):
    return f"carousel/{filename}"

class CarouselImage(models.Model):
    image = models.ImageField(upload_to=carousel_upload_path)
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of the image in the carousel")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Carousel Image {self.id} - Order {self.order}"
    
    from django.db import models

class HomeCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image1 = models.ImageField(upload_to='cards/')  # Main image
    image2 = models.ImageField(upload_to='cards/', blank=True, null=True)  # Overlay image (optional)
    link = models.CharField(max_length=200)  # This can be "/nailart", "/makeup", etc.

    def __str__(self):
        return self.title