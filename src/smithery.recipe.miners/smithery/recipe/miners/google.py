"""
Google-miners are recipes that extract data and metadata from Google services.
"""

from csv import writer
from datetime import datetime
from re import compile
from urlparse import unquote

from gdata.calendar.service import CalendarService, CalendarEventQuery

from .base import Miner


class BaseGoogleCalendar(Miner):
    def setup_service(self):
        service = CalendarService()
        service.email = self.options['email']
        service.password = self.options['password']
        service.source = 'bopen-smithery.recipe.miners:google_calendar-0.1'
        service.ProgrammaticLogin()
        return service

    def event_details(self, event):
        event_rows = [] 
        for who in event.who:
            # skip calendar fake users
            if who.email.endswith('group.calendar.google.com'):
                continue
            if self.user_regex.search(who.email):
                event_rows.append([event.title.text, event.summary, event.when[0].start_time[:19], event.when[0].end_time[:19], who.email, who.attendee_status.value])
        return event_rows

    def install(self):
        service = self.setup_service()

        self.user_regex = compile(self.options.get('user_regex', '.*'))

        feed = service.GetOwnCalendarsFeed()
        csv_filename = self.options.get('csv_filename', 'temp.csv')
        csvwriter = writer(open(csv_filename, 'wb'))
        # keep the header in sync with event_details
        csvwriter.writerow(['project', 'title', 'summary', 'start_time', 'end_time', 'who'])
        for i, calendar in enumerate(feed.entry):
            # is there no other way to get the 'user' of a feed?
            user = unquote(calendar.content.src.split('/')[5])
            print '%s. %r\t%r\t%r\t%r' % (i, calendar.title.text, calendar.timezone.value, calendar.hidden.value, user)
            query = CalendarEventQuery(user)
            if 'start_min' in self.options:
                query.start_min = self.options['start_min']
            if 'start_max' in self.options:
                query.start_max = self.options['start_max']
            query.max_results = self.options.get('max_results', '500')
            events_feed = service.CalendarQuery(query)
            assert len(events_feed.entry) < int(query.max_results)
            for event in events_feed.entry:
                for event_row in self.event_details(event):
                    csvwriter.writerow([calendar.title.text] + event_row)
        self.buildout.namespace['google_calendar'] = {'csv_filename': csv_filename}
        return tuple()

class GoogleCalendar(BaseGoogleCalendar):
    pass
