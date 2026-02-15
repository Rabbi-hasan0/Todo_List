import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo_List.settings')

application = get_wsgi_application()

from whitenoise import WhiteNoise
application = WhiteNoise(application, root='/opt/render/project/src/media/')
application.add_files('/opt/render/project/src/media/', prefix='/media/')