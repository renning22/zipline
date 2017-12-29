from datetime import time
from pandas.tseries.offsets import CustomBusinessDay
from pytz import timezone
from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities
from zipline.utils.calendars import register_calendar
from zipline.utils.calendars import TradingCalendar
from zipline.utils.memoize import lazyval
import pandas as pd

# A bunch of imports removed for the sake of clarity
class TwentyFourSevenCalendar(TradingCalendar):
    """
    Exchange calendar for 24/7 trading.

    Open Time: 12am, UTC
    Close Time: 11:59pm, UTC

    """
    @property
    def name(self):
        return "TWENTYFOURSEVEN"

    @property
    def tz(self):
        return timezone("UTC")

    @property
    def open_time(self):
        return time(0, 0)

    @property
    def close_time(self):
        return time(23,59)

    @lazyval
    def day(self):
        return CustomBusinessDay(
            weekmask='Mon Tue Wed Thu Fri Sat Sun',
        )

start_session = pd.Timestamp('2016-01-01', tz='utc')
end_session = pd.Timestamp('2017-12-01', tz='utc')
assets = ['BTC_USD']

register_calendar(
    'TWENTYFOURSEVEN',
    TwentyFourSevenCalendar(
        start=start_session,
        end=end_session
    )
)
register(
    'custom-csvdir-bundle',
    csvdir_equities(["minute"], '/home/ningr/Documents/csvdir'),
    calendar_name='TWENTYFOURSEVEN',
    minutes_per_day=1440,
    # start_session=start_session,
    # end_session=end_session
)
