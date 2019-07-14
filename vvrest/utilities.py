import datetime
from .constants import TOKEN_EXPIRY_TIMEZONE
from pytz import timezone


def get_token_expiration(expires):
    """
    :param expires: int, seconds value
    :return: datetime
    """
    tz = timezone(TOKEN_EXPIRY_TIMEZONE)
    utc_now = datetime.datetime.now(tz)
    expiration_date = utc_now + datetime.timedelta(seconds=expires)

    return expiration_date
