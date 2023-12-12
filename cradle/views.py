from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import SensorData


@csrf_protect
def index(request):
    # Generate random sensor data if POST request
    if request.method == 'POST':
        sensor_data = SensorData.generate_random_data()
        noise_level = sensor_data['noise_level']
        is_crying = sensor_data['is_crying']

        sensor_data_obj = SensorData(
            timestamp=sensor_data['timestamp'],
            temperature=sensor_data['temperature'],
            humidity=sensor_data['humidity'],
            noise_level=noise_level,
            is_crying=is_crying
        )

        sensor_data_obj.save()

        return redirect(request.META['PATH_INFO'])

    # Get existing data if no POST request
    try:
        latest_data = SensorData.objects.latest('timestamp')
    except SensorData.DoesNotExist:
        latest_data = None

    is_button_clicked = request.method == 'POST'

    context = {
        'latest_data': latest_data,
        'is_button_clicked': is_button_clicked
    }

    return render(request, 'index.html', context)


def get_values(request):
    """
    This view function handles the POST request to get sensor data.
    """
    if request.method == 'POST':
        # Generate sensor data
        sensor_data = SensorData.generate_random_data()
        noise_level = sensor_data['noise_level']
        is_crying = sensor_data['is_crying']

        # Create a dictionary with the generated sensor data
        data = {
            'timestamp': sensor_data['timestamp'],
            'temperature': sensor_data['temperature'],
            'humidity': sensor_data['humidity'],
            'noise_level': noise_level,
            'is_crying': is_crying
        }

        return JsonResponse(data)
    else:
        return redirect('index')
