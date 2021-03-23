from django.shortcuts import render

# Create your views here.


def home(request):
    views = {}
    views['feedbacks'] = Review.objects.all()
    views = {}
    views["projects"] = Project.objects.all()


    return render(request, 'index.html', views)

def about(request):
    views = {}
    views['feedbacks'] = Review.objects.all()
    return render(request, 'about.html', views)

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')

def price(request):
    return render(request, 'price.html')

def elements(request):
    return render(request, 'elements.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def bloghome(request):
    return render(request, 'blog-home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()
    return render(request, 'contact.html')