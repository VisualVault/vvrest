import datetime


def get_token_expiration(expires):
    """
    :param expires: int, seconds value
    :return: datetime
    """
    date = datetime.datetime.utcnow()
    expiration_date = date + datetime.timedelta(seconds=expires)

    return expiration_date
