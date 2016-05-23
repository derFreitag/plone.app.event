from Products.Five.browser import BrowserView
from plone.event.interfaces import IEventAccessor
from plone.event.interfaces import IOccurrence


class EventView(BrowserView):

    @property
    def data(self):
        return IEventAccessor(self.context)

    def __call__(self):
        if IOccurrence.providedBy(self.context):
            # The transient Occurrence objects cannot be edited. disable the
            # edit border for them.
            self.request.set('disable_border', True)
        return self.index()  # render me.
