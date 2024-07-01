import os
import dj_database_url
from os import environ

# Session configurations
SESSION_CONFIGS = [
    dict(
        name='Task',
        app_sequence=['Task'],
        num_demo_participants=1,
        treatment='random',
    ),
    dict(
        name='Questionnaire',
        app_sequence=['Questionnaire'],
        num_demo_participants=1,
    ),
    dict(
        name='Instructions',
        app_sequence=['Instructions'],
        num_demo_participants=1,
        treatment='random',
    ),
    dict(
        name='Session',
        app_sequence=['InformedConsent', 'Instructions', 'Task', 'Questionnaire'],
        num_demo_participants=1,
        treatment='random',  # Randomize between-subject treatment
    ),
]

# Default configuration for sessions
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

# Participant-specific fields
PARTICIPANT_FIELDS = [
    'lPos',                 # Position of attributes
    'iSelectedTrial',       # Trial selected for payment
    'bTimeout',             # Participant timed out
    'sTreatment',           # Treatment name
]

# Session-specific fields
SESSION_FIELDS = []

# Language code (ISO-639)
LANGUAGE_CODE = 'en'

# Real world currency code
REAL_WORLD_CURRENCY_CODE = 'USD'

# Whether to use points system
USE_POINTS = True

# Admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Introduction HTML for demo page
DEMO_PAGE_INTRO_HTML = """ """

# Secret key for Django
SECRET_KEY = environ.get('DJANGO_SECRET_KEY', 'default-secret-key')

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{os.path.join(os.path.dirname(__file__), 'db.sqlite3')}",
        conn_max_age=600,  # Keep database connections open for 10 minutes
        ssl_require=True   # Require SSL for PostgreSQL on Heroku
    )
}

# Debug mode configuration
DEBUG = os.environ.get('OTREE_PRODUCTION', '0') == '0'  # Disable debug if OTREE_PRODUCTION is set to '1'

# Configure logging for production
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
