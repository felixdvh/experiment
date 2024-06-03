
from os import environ

SESSION_CONFIGS = [
    dict(
        name='task',
        app_sequence=['Task'],
        num_demo_participants=1,
        treatment = 'random',
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
        treatment = 'random',
    ),
    dict(
        name='Session',
        app_sequence=['InformedConsent','Instructions','Task','Questionnaire'],
        num_demo_participants=1,
        treatment = 'random', # Randomize between-subject treatment. 
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'lPos',                 # Position of attributes 
    'iSelectedTrial',       # Trial selected for payment
    'bTimeout',             # Participant timed-out
    'sTreatment',           # Treatment name
]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '5401288888583'
