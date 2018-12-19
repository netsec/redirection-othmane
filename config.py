"""
    Module for config , vars
"""
from envparse import Env

env = Env(
    ELASTICSEARCH_HOST=str,
    ELASTICSEARCH_USER=dict(cast=str, default='elastic'),
    ELASTICSEARCH_PASSWORD=str,
    ELASTICSEARCH_SSL=dict(cast=bool, default=True),
    MAILGUN_API_KEY=str,
    EMAIL_DOMAIN=str,
    EMAIL_USER=dict(cast=str, default='root'),
    TO=dict(cast=list, default='drovn@protonmail.com'),
    PAGE_SMS=dict(cast=bool, default=True),
    IPTOEARTH_API_KEY=str,
)


# Elastic search configuration -------

# HOST = "https://50426d843cdebb6e6250157f00cb88ce.eu-west-1.aws.found.io:9243"

# host of the cluster
ELASTICSEARCH_HOST = env('ELASTICSEARCH_HOST')

# the user of the cluster
ELASTICSEARCH_USER = env('ELASTICSEARCH_USER')

# the password of the cluster
ELASTICSEARCH_PASSWORD = env('ELASTICSEARCH_PASSWORD')

# use ssl in auth to the cluster
ELASTICSEARCH_SSL = env('ELASTICSEARCH_SSL')

# End -------

# Email send provider configuration

EMAIL_API_KEY = env('MAILGUN_API_KEY')

EMAIL_DOMAIN = env('EMAIL_DOMAIN')

EMAIL_USER = env('EMAIL_USER')

TO = env('TO')

PAGE_SMS = env('PAGE_SMS')

IP_TO_EARTH_KEY = env('IPTOEARTH_API_KEY')
