from os import environ

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
        treatment='random',
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'lPos',
    'iSelectedTrial',
    'bTimeout',
    'sTreatment',
]
SESSION_FIELDS = []

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5401288888583'

ROOMS = [
    dict(
        name='experimentfelix',
        display_name='Experiment Felix Room',
        use_secure_urls=True,  # Automatically generate secure URLs for participants
    ),
]

OTREE_PRODUCTION = environ.get('OTREE_PRODUCTION', '1') == '1'

# Static files settings
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

# Optional: Enable Sentry for error tracking
OTREE_SENTRY_DSN = environ.get('OTREE_SENTRY_DSN')
