import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = True
    POSTGRES_URL = "femmyte-server.postgres.database.azure.com"  # TODO: Update value
    POSTGRES_USER = "femmyte@femmyte-server"  # TODO: Update value
    POSTGRES_PW = "Library%401234"  # TODO: Update value
    POSTGRES_DB = "techconfdb"  # TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(
        user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    # TODO: Update value
    SERVICE_BUS_CONNECTION_STRING = 'Endpoint=sb://femmytebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=NNpmrGj0p25FDBcuxSIWA3NtxlSPsjjM6k/7ASK0sLQ='
    SERVICE_BUS_QUEUE_NAME = 'notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'sanyaoluadefemi@gmail.com'
    # Configuration not required, required SendGrid Account
    SENDGRID_API_KEY = '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'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
