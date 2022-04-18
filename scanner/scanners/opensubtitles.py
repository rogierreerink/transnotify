from scanner.scanner import Scanner
from scanner.result import Result
from scanner.type import Type
from log.log import Level
from globals import getGlobal

from typing import List
from datetime import datetime
import requests
import urllib
import json


API_URI = 'https://rest.opensubtitles.org'
API_USERAGENT = 'TemporaryUserAgent'


class OpenSubtitles(Scanner):
    """
    The OpenSubtitles scanner.
    """

    def scan(self, filename: str) -> List[Result]:
        """
        Scan OpenSubtitles.org for the given filename and return the results.
        """
        url = API_URI + '/search/query-' + urllib.parse.quote(filename) \
            + ''
        req = requests.get(url, headers={
            'X-User-Agent': API_USERAGENT
        })

        if req.status_code != 200:
            getGlobal('log').write(
                Level.ERROR, f'Failed to get results from \'{url}\' ({req.status_code})')
            return list()

        jsonResults = json.loads(req.text)[:1]
        results = list()
        for jsonResult in jsonResults:
            if (jsonResult['MovieKind']) == 'movie':
                result = Result(Type.MOVIE)
                result.title = jsonResult['MovieName']
                result.date = datetime.strptime(jsonResult['MovieYear'], '%Y')
                results.append(result)

            elif (jsonResult['MovieKind']) == 'episode':
                result = Result(Type.SERIES)
                result.title = jsonResult['MovieName']
                result.season = int(jsonResult['SeriesSeason'])
                result.episode = int(jsonResult['SeriesEpisode'])
                results.append(result)

            else:
                getGlobal('log').write(
                    Level.ERROR, f'OpenSubtitles media type not recognized ({jsonResult["MovieKind"]})')

        return results
