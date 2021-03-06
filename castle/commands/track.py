from castle.command import Command
from castle.utils import timestamp
from castle.context.merger import ContextMerger
from castle.context.sanitizer import ContextSanitizer
from castle.validators.present import ValidatorsPresent


class CommandsTrack(object):
    def __init__(self, context):
        self.context = context

    def build(self, options):
        ValidatorsPresent.call(options, 'event')
        context = ContextMerger.call(self.context, options.get('context'))
        context = ContextSanitizer.call(context)
        options.update({'sent_at': timestamp(), 'context': context})

        return Command(method='post', path='track', data=options)
