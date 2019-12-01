from django.http import HttpResponse

def all_pets(request):
    text = ''
    pets = Pet.objects.all()
    for pet in pets:
        text += pet.name + ', '
    return HttpResponse(text)

def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(pet.name)


