from django.core.management.base import BaseCommand, CommandError
from AnUrl.models import AnasUrl

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
    	print(options)
    	return AnasUrl.objects.refresh_shortcode(items=options['items'])
