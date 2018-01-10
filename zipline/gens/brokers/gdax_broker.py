#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod, abstractproperty
from zipline.gens.brokers.broker import Broker
import pandas as pd
import sys, traceback

from logbook import Logger

log = Logger('GDAXBroker')

class GDAXBroker(Broker):
    def __init__(self, tws_uri, account_id=None):
        log.info('GdaxBroker init {}'.format(tws_uri))

    def subscribe_to_market_data(self, asset):
        log.info('subscribe_to_market_data')

    @property
    def subscribed_assets(self):
        return []

    @property
    def positions(self):
        return []

    @property
    def portfolio(self):
        return []

    @property
    def account(self):
        return []

    @property
    def time_skew(self):
        return pd.Timedelta(0)

    def order(self, asset, amount, style):
        pass

    def is_alive(self):
        return True

    @property
    def orders(self):
        return {}

    @property
    def transactions(self):
        # traceback.print_stack()
        return {}

    def cancel_order(self, order_param):
        pass

    def get_last_traded_dt(self, asset):
        log.info('get_last_traded_dt {}'.format(asset))
        return []

    def get_spot_value(self, assets, field, dt, data_frequency):
        log.info('get_spot_value {} {} {} {}'.format(assets, field, dt, data_frequency))

    def get_realtime_bars(self, assets, frequency):
        log.info('get_realtime_bars')
