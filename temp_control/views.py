from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Room, Weather

from modules.rpiModules import get_temperature, cooler_turn_on, cooler_turn_off, heater_turn_on, heater_turn_off


def index(request):
    room = Room.objects.get(pk=1)
    weather = Weather.objects.get()
    temperature = get_temperature()
    context = {
        'city_temperature': weather.city_temperature,
        'city_weather_condition': weather.city_weather_condition,
        'temperature': temperature,
        'room': room
    }
    return render(request, 'temp_control/index.html', context)


def cooler_toggle(request):
    room = Room.objects.get(pk=1)
    if not room.is_automatic:
        if room.cooler_status:
            cooler_turn_off()
            room.cooler_status = False
            room.save()

        else:
            cooler_turn_on()
            room.cooler_status = True
            room.save()

    return redirect('temp_control:room_info')


def heater_toggle(request):
    room = Room.objects.get(pk=1)
    if not room.is_automatic:
        if room.heater_status:
            heater_turn_off()
            room.heater_status = False
            room.save()

        else:
            heater_turn_on()
            room.heater_status = True
            room.save()

    return redirect('temp_control:room_info')


def automatic_toggle(request):
    room = Room.objects.get(pk=1)
    if room.is_automatic:
        room.is_automatic = False
        room.save()
    else:
        room.is_automatic = True
        heater_turn_off()
        cooler_turn_off()
        room.cooler_status = False
        room.heater_status = False
        room.save()
    return redirect('temp_control:room_info')


@api_view(['GET'])
def room_info(request):

    room = Room.objects.get(id=1)
    context = {
        'temperature': get_temperature(),
        'is_automatic': room.is_automatic,
        'cooler_status': room.cooler_status,
        'heater_status': room.heater_status,
    }
    return Response(context)


@api_view(['GET'])
def cooler_toggle_API(request):
    room = Room.objects.get(pk=1)
    if not room.is_automatic:
        if room.cooler_status:
            cooler_turn_off()
            room.cooler_status = False
            room.save()
            print('cooler is off')
            content = {"detail": "cooler OFF"}
            return Response(content)

        else:
            cooler_turn_on()
            room.cooler_status = True
            room.save()
            print('cooler is on')
            content = {"detail": "cooler ON"}
            return Response(content)

    else:
        content = {'detail': 'System is on automatic mode!'}

        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def heater_toggle_API(request):
    room = Room.objects.get(pk=1)
    if not room.is_automatic:
        if room.heater_status:
            heater_turn_off()
            room.heater_status = False
            room.save()
            print('heater is off')
            content = {"detail": "heater OFF"}
            return Response(content)

        else:
            heater_turn_on()
            room.heater_status = True
            room.save()
            print('heater is on')
            content = {"detail": "heater ON"}
            return Response(content)

    else:
        content = {'detail': 'System is on automatic mode!'}

        return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def automatic_toggle_API(request):
    room = Room.objects.get(pk=1)
    if room.is_automatic:
        room.is_automatic = False
        room.save()
        content = {'detail': 'system is on manual mode'}

        return Response(content)
    else:
        room.is_automatic = True
        heater_turn_off()
        cooler_turn_off()
        room.cooler_status = False
        room.heater_status = False
        room.save()
        content = {'detail': 'system is on automatic mode'}

        return Response(content)
