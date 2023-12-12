from django.shortcuts import render
from .models import SensorData
def index(request):
    # Generate random sensor data
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

    # Save the sensor data to the database
    sensor_data_obj.save()

    
    # Create a context dictionary to pass data to the template
    context = {
        'timestamp': sensor_data['timestamp'],
        'temperature': sensor_data['temperature'],
        'humidity': sensor_data['humidity'],
        'noise_level': sensor_data['noise_level'],
        'is_crying': sensor_data['is_crying']
    }

    # Render the index template with the context dictionary
    return render(request, 'index.html', context)

# def login_page(request):
#     return render(request,'login.html')

    
