from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import ContactForm, Distributor
import googlemaps
import time
from .forms import AddressForm
import json
#MAKE FUNTCTION THAT RETURNS API KEY

def home(request):
    context = {
        "title" : "The Truck Company"
    }

    return render(request, "home/home_page.html", context)

def about(request):
    context = {
        "title" : "About Us"
    }
    return render(request, "home/about.html", context)



def locate(request):
    #Define api key
    #API_KEY = _get_ssm_key('/Dev/WebServer/GOOGLE_KEY')
    API_KEY = os.environ['GOOGLE_API_KEY']
    

    #Define client
    gmaps = googlemaps.Client(key = API_KEY)
    
    
    def get_home_coordinates():
        search_address = ""
        if 'address' in request.GET:
            search_address = request.GET['address']
            geo_response = gmaps.geocode(address = search_address)

            latitude = geo_response[0]['geometry']['location']['lat']
            longitude = geo_response[0]['geometry']['location']['lng']
            lat_long_home = [latitude , longitude]
            return lat_long_home, search_address
        return "", ""
    


    queryset = Distributor.objects.all()
    dist_locations = []

    #ONLY NEED TO RUN THIS TO GENERATE NEW LIST OF DIST_LOCATIONS
    '''
    for distributor in queryset:
        #Geocode the address to get the lat and long
        dist_response = gmaps.geocode(address = distributor.address)
        latitude = dist_response[0]['geometry']['location']['lat']
        longitude = dist_response[0]['geometry']['location']['lng']
        #Add the name, lat and long to a new list of lists
        details = [distributor.name, latitude, longitude, distributor.address, distributor.phone, distributor.web_link]
        dist_locations.append(details)

        #JSON-ify the list
        #json_dist_locations = json.dumps(dist_locations)
    '''
    lat_long_home, search_address = get_home_coordinates()

    context = {
        "title" : "Our Distributors",
        "dist_locations" : dist_locations,
        'search_address' : search_address,
        "lat_long_home" : lat_long_home,
         "API_KEY" : API_KEY,
    }
    return render(request, "home/locate.html", context)


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message + "\n From: " + from_email, from_email, ['mallory.thetruckcompany@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "home/contact.html", {'form': form, "title": "Contact Us"})

def successView(request):
    return render(request, "home/success.html")
