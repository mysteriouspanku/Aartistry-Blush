from django.shortcuts import render,HttpResponse,redirect
from .forms import PostForm
from .models import Posts, SiteSettings, CarouselImage, HomeCard

def index(request):
    carousel_images = CarouselImage.objects.all()
    cards = HomeCard.objects.all()
    return render(request, 'index.html', {
        'carousel_images': carousel_images,
        'cards': cards
    })
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def nailart(request):
    posts = Posts.objects.filter(post_type='nailart').order_by('-created_at')
    return render(request, 'nailart.html', {'posts': posts})

def makeup(request):
    posts = Posts.objects.filter(post_type='makeup').order_by('-created_at')
    return render(request, 'makeup.html', {'posts': posts})

def productReview(request):
    posts = Posts.objects.filter(post_type='productreview').order_by('-created_at')
    return render(request, 'productReview.html', {'posts': posts})

def uploadPosts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nailart')  # optional: redirect based on post_type
    else:
        form = PostForm()
    return render(request, 'upload.html', {'form': form})
