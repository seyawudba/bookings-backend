# from django.test import TestCase

# Create your tests here.

import pytest


@pytest.mark.django_db
class TestSample:
    def test_set_up(self, test_sample):
        value = test_sample
        assert value == 5
