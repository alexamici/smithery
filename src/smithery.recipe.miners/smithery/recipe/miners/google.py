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
    headers = ['project', 'title', 'summary', 'start_time', 'end_time', 'who', 'attendee_status', 'uid']
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
            # skip crap events (observed and unexplained)
            if who.attendee_status is None:
                print 'Skip: anomalous attendee %r in event %r (no attendee_status)' % (who.email, event.title.text)
                continue
            if self.user_regex.search(who.email):
                try:
                    uid = event.uid.value
                except:
                    uid = event.id.text
                event_rows.append(
                    [event.title.text,
                    event.summary,
                    event.when[0].start_time[:19],
                    event.when[0].end_time[:19],
                    who.email,
                    who.attendee_status.value,
                    uid])
        return event_rows

    def install(self):
        service = self.setup_service()

        self.user_regex = compile(self.options.get('user_regex', '.*'))

        feed = service.GetOwnCalendarsFeed()
        csv_filename = self.options.get('csv_filename', 'temp.csv')
        csvwriter = writer(open(csv_filename, 'wb'))
        # keep the header in sync with event_details
        csvwriter.writerow(self.headers)
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
            print ' %r' % (len(events_feed.entry),)
            assert len(events_feed.entry) < int(query.max_results)
            for event in events_feed.entry:
                # skip recurrent event because they are too ambiguous
                if event.recurrence:
                    print 'Skip: recurrent event %r' % event.title.text
                    continue
                for event_row in self.event_details(event):
                    csvwriter.writerow([calendar.title.text] + event_row)
        self.buildout.namespace['google_calendar'] = {'csv_filename': csv_filename}
        return tuple()

class GoogleCalendar(BaseGoogleCalendar):
    """Exports Google Calendar events data into a CSV file suitable for further processing"""
    headers = BaseGoogleCalendar.headers + ['hours', 'day', 'month', 'year', 'isoweekdate', 'isoweek']
    def event_details(self, event):
        event_rows = super(GoogleCalendar, self).event_details(event)
        for event_row in event_rows:
            if len(event.when[0].start_time) == 10: # whole day
                start_time = datetime.strptime(event.when[0].start_time, '%Y-%m-%d')
                end_time = datetime.strptime(event.when[0].end_time, '%Y-%m-%d')
                # FIXME: multi-day events are 8 hours!!!!
                hours = 8.
            else:
                start_time = datetime.strptime(event.when[0].start_time[0:19], '%Y-%m-%dT%H:%M:%S')
                end_time = datetime.strptime(event.when[0].end_time[0:19], '%Y-%m-%dT%H:%M:%S')
                duration = (end_time - start_time)
                hours = duration.seconds / 3600. + duration.days * 8.
            event_row.append(hours)
            day = start_time.isoformat()[:10]
            event_row += [day, day[:7], day[:4]]
            isoweekdate = '%d-W%02d-%d' % datetime.strptime(day, '%Y-%m-%d').isocalendar()
            event_row += [isoweekdate, isoweekdate[:8]]
        return event_rows
