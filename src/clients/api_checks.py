#src/clients/api_checks.py
from typing import Tuple, Optional
import requests


class URLHealth:
    def __init__(self, url: str):
        self.url = url
        self._cached_response: Optional[requests.Response] = None
        self._request_made = False


    def _head_response(self) -> requests.Response:
        return requests.head(self.url, allow_redirects=True, timeout=5)

    def _get_response(self) -> requests.Response:
        return requests.get(self.url, allow_redirects=True, timeout=5)


    def _safe_request(self) -> requests.Response | None:
        if self._request_made:
            return self._cached_response

        try:
            r = self._head_response()
            if r.status_code == 405:  # HEAD not allowed
                r = self._get_response()
            if 200 <= r.status_code < 400:
                self._cached_response = r
            else:
                self._cached_response = None
        except requests.RequestException:
            self._cached_response = None

        self._request_made = True
        return self._cached_response


    def is_alive(self) -> bool:
        return self._safe_request() is not None


    def response_basics(self) -> Tuple[int, str]:
        if (r:=self._safe_request()) is not None:
            return r.status_code, r.reason
        else:
            return 0, f"\n[DEV LOG]\tURL Health Check is failed for {self.url}"


# Usage:
# url_info.is_alive()
# url_info.response_basics()
