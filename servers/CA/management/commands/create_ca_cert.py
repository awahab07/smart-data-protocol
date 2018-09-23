from django.core.management.base import BaseCommand, CommandError

from ...cert import cert

class Command(BaseCommand):
    help = 'Generates CA RSA certificate. \nAll subsequent client/server certificate creation and validation operations will be based on this certificate.\n This certificate must be created first in order to take advantage of the encryption and certificate validation.\n\nUsage: python manage.py create_CA_cert <validity in seconds>'

    def add_arguments(self, parser):
        parser.add_argument('validity', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Received validity %d seconds' % options['validity'][0]))
        cert.create_ca_cert(options['validity'][0])

