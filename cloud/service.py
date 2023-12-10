from google.oauth2 import service_account
from google.cloud import compute_v1
credentials = service_account.Credentials.from_service_account_file(
    'key.json')


from django.apps import AppConfig

class ApplicationConfig(AppConfig):
    name = 'cloud'