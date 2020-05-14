import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Profile, Trainee
# Create your tests here.


class AddTraineeViewTests(TestCase):

    def test_trainee_added(self):
        """tests that the data from the TraineeForm() has been saved to a new instance of Trainee in the db. """
        pass

    def test_add_multiple_trainers(self):
        """ tests that the user is able to add two or more trainers to the new trainee's model. Trainers are ManyToMany relationship with Profile """
        pass

    
