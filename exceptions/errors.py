"""Кастомные классы обработки ошибок."""


class APIException(Exception):
    """Ошибик в работе API."""
    ...


class ServiceException(Exception):
    """Ошибки в работе сервиса курса валют."""
    ...
