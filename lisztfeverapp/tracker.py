import re
from urllib.parse import urlparse
import logging

logger = logging.getLogger("info")

class WebLogs:

    def save_to_calendar(self, user_id, event_id):

        try:

            logger.info({
                'user_id': user_id,
                'action': 'save to calender',
                'source': 'web',
                'payload': event_id
            })

        except NameError:

            logger.info("save to calendar logger errror")

    def delete_event(self, user_id, event_id):

        try:

            logger.info({
                'user_id': user_id,
                'action': 'delete event',
                'source': 'web',
                'payload': event_id
            })

        except NameError:

            logger.info("save to calendar logger errror")

    def listen_music(self, user_id, artist_id):

        try:

            logger.info({
                'user_id': user_id,
                'action': 'listen music',
                'source': 'web',
                'payload': artist_id
            })

        except NameError:

            logger.info('listen music logger error')

    def user_click(self, user_id, url, ref):

        try:

            ref = re.search('ref=(.*)&', urlparse(ref).query)
            ref = ref.group(1)

            logger.info({
                'user_id': user_id,
                'action': 'click',
                'source': 'web',
                'payload': url,
                'ref': ref
            })

        except NameError:

            logger.info('user click logger error')

    def search(self, user_id, genre_artist):

        try:

            logger.info({
                'user_id': user_id,
                'action': 'search',
                'source': 'web',
                'payload': genre_artist
            })

        except NameError:

            logger.info('search logger error')

    def concert_dates(self, user_id, artist_id):

        try:

            logger.info({
                'user_id': user_id,
                'action': 'concert dates',
                'source': 'web',
                'payload': artist_id
            })

        except NameError:

            logger.info('search logger error')
