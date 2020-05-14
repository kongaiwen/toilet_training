from django.apps import AppConfig


class ToiletTrainingConfig(AppConfig):
    name = 'toilet_training'

    def ready(self):
        import toilet_training.signals
