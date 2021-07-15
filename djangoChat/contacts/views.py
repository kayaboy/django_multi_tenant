from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def main(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'contacts/main.html', {'contacts': contacts, 'search_input': search_input})

def index(request):
    
    return render(request, 'index.html')

def addContact(request):
    if request.method == 'POST':

        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            address=request.POST['address'],
            )
        new_contact.save()
        return redirect('/contact/')

    return render(request, 'contacts/new.html')

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/contact/profile/'+str(contact.id))
    return render(request, 'contacts/edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/contact/')

    return render(request, 'contacts/delete.html', {'contact': contact})

def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contacts/contact-profile.html', {'contact':contact})