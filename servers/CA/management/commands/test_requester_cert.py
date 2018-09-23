from django.core.management.base import BaseCommand, CommandError

from ...cert import cert

class Command(BaseCommand):
    help = 'Tests requester certificate against provided user_id'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Testing requester certificate for user_id: %s' % options['user_id'][0]))
        if cert.verify_requester_cert(options['user_id'][0]):
            print ("Certificate Valid")
        else:
            print ("Certificate Invalid")


