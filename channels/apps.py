# We import this here to ensure the reactor is installed very early on
# in case other packages accidentally import twisted.internet.reactor
# (e.g. raven does this).
from django.apps import AppConfig


class ChannelsConfig(AppConfig):

    name = "channels"
    verbose_name = "Channels"
