from django.core.management.base import BaseCommand, CommandError

from ...cert import cert

class Command(BaseCommand):
    help = 'Generates certificate for requester'

    def add_arguments(self, parser):
        parser.add_argument('valid_after', nargs='+', type=int)
        parser.add_argument('valid_for', nargs='+', type=int)
        parser.add_argument('user_name', nargs='+', type=str)
        parser.add_argument('user_id', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Received requester certificate creation request %s' % options))
        cert.create_requester_cert(options['valid_after'][0], options['valid_for'][0], options['user_name'][0], options['user_id'][0])
        #cert.create_resource_cert(options['validity'][0])

