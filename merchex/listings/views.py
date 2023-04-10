from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band,Contact,Listing

def hello(request):
    liste_bands = Band.objects.all()
    return render(request,
                'listings/hello.html',
                {'liste_bands': liste_bands})
def about(request):
    liste_contacts = Contact.objects.all()
    return render(request,
                  'listings/about.html',
                  {'liste_contacts': liste_contacts})

def listing(request):
    liste_listings = Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'liste_listings': liste_listings})

