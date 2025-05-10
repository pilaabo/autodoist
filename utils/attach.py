import json
import logging
from typing import Union

import allure

_Log = Union[logging.Logger, logging.LoggerAdapter]


def _pretty(data):
    if data in (None, b"", ""):
        return "<empty>"
    try:
        parsed = json.loads(data if isinstance(data, str) else str(data))
        return json.dumps(parsed, ensure_ascii=False, indent=2)
    except Exception:
        return data if isinstance(data, str) else str(data)


def _push_to_allure(text: str, name: str) -> None:
    allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)


def log_and_attach_request(
        req,
        *,
        logger: _Log | None = None,
        level: int = logging.INFO,
        title: str = "HTTP request",
) -> None:
    logger = logger or logging.getLogger(__name__)
    parts = [
        f"{req.method} {req.url}",
        "--- Headers ---",
        *(f"{k}: {v}" for k, v in req.headers.items()),
        "--- Body ---",
        _pretty(req.body),
    ]
    text = "\n".join(map(str, parts))

    # 1) В лог
    logger.log(level, "%s\n%s", title, text)
    # 2) В Allure
    _push_to_allure(text, title)


def log_and_attach_response(
        resp,
        *,
        logger: _Log | None = None,
        level: int = logging.INFO,
        title: str = "HTTP response",
) -> None:
    logger = logger or logging.getLogger(__name__)
    parts = [
        f"HTTP {resp.status_code}",
        "--- Headers ---",
        *(f"{k}: {v}" for k, v in resp.headers.items()),
        "--- Body ---",
        _pretty(resp.content),
    ]
    text = "\n".join(map(str, parts))
    logger.log(level, "%s\n%s", title, text)
    _push_to_allure(text, title)
