import datetime
from django.db import models
from django.contrib.auth.models import User
from faker import Faker




class SensorData(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    noise_level = models.FloatField()
    is_crying = models.BooleanField()

    def __str__(self):
        return f"SensorData: timestamp={self.timestamp}, temperature={self.temperature}, humidity={self.humidity}, noise_level={self.noise_level}, is_crying={self.is_crying}"

    @staticmethod
    def generate_random_data():
        fake = Faker()
        temperature = fake.pyfloat(left_digits=2, right_digits=1, positive=True, min_value=25, max_value=30)
        humidity = fake.pyfloat(left_digits=2, right_digits=1, positive=True, min_value=40, max_value=60)
        # noise_level = fake.pyint(min=30, max=100)
        # noise_level = fake.randint(min=30, max=100)
        noise_level = fake.random_int(min=50, max=101, step=1)
        is_crying = True if noise_level >= 80 else False
          
        timestamp = datetime.datetime.now()  # Generate a timestamp
        return {
            'timestamp': timestamp,
            'temperature': temperature,
            'humidity': humidity,
            'noise_level': noise_level,
            'is_crying': is_crying
        }

  