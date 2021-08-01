from django.apps import AppConfig
import course

class CourseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course'

    def ready(self):
        import course.signel

