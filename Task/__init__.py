from otree.api import *
import numpy.random as rnd
import random
import pandas as pd

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'Task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 33  # Adjusted to match the number of unique trials
    NUM_PROUNDS = 3
    lAttrID = ['p', 's', 'c']
    lAttrNames = ['Price', 'Sustainability', 'Label']
    lColNames = ['Product A', 'Product B']
    BetweenTrialMessages = {
        "1": f"Now you will have {NUM_PROUNDS} practice rounds.",
        str(NUM_PROUNDS + 1): "The practice rounds are over."
    }
    imgLeafs = "global/figures/leafs/leaf_"
    imgLabels = "global/figures/labels/label_"
    imgPrices = "global/figures/prices/n_"
    imgProducts = "global/figures/products/product_"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sChoice = models.StringField()
    dRT_dec = models.FloatField()
    dRT_conf = models.FloatField()
    P1 = models.IntegerField()
    P2 = models.IntegerField()
    S1 = models.IntegerField()
    S2 = models.IntegerField()
    Q1 = models.IntegerField()
    Q2 = models.IntegerField()
    sNames = models.LongStringField(blank=True)
    sDT = models.LongStringField(blank=True)
    sStartDec = models.StringField()
    sEndDec = models.StringField()
    sStartCross = models.StringField()
    sEndCross = models.StringField()
    sBetweenBtn = models.StringField()
    Product1 = models.IntegerField()
    Product2 = models.IntegerField()


# Add this PARTICIPANT_FIELDS definition to include the custom field
PARTICIPANT_FIELDS = ['lPos', 'iSelectedTrial', 'trials', 'sTreatment']


def creating_session(subsession):
    if subsession.round_number == 1:
        players = subsession.get_players()
        for player in players:
            p = player.participant

            # Select trial for payment
            p.iSelectedTrial = random.randint(C.NUM_PROUNDS + 1, C.NUM_ROUNDS)

            # Generate 30 trials with specified combinations
            trials = generate_trials()

            # Assign the trials to the participant
            p.trials = trials

    for player in subsession.get_players():
        p = player.participant
        player.sBetweenBtn = random.choice(['left', 'right'])

        if player.round_number <= C.NUM_PROUNDS:
            # Practice Trials
            lValues = {
                1: [1, 2, 1, 1, 1, 1],
                2: [4, 5, 1, 2, 1, 1],
                3: [8, 7, 1, 1, 1, 2]
            }.get(player.round_number, [1, 1, 1, 1, 1, 1])
            p.sTreatment = 'Practice'
            player.Product1, player.Product2 = 1, 2  # Practice products
        else:
            # Normal Trials
            trial_index = player.round_number - C.NUM_PROUNDS - 1
            trial = p.trials[trial_index]
            p.sTreatment = trial['condition']
            lValues = trial['values']
            lValues = [int(value) for value in lValues]  # Convert values to integers
            player.Product1, player.Product2 = trial['products']

        player.P1, player.P2, player.S1, player.S2, player.Q1, player.Q2 = lValues


def generate_trials():
    # Define the valid combinations
    combinations = [
        # TruePrice and Label
        {'values': [8, 8, 2, 1, 1, 2], 'condition': 'TruePrice', 'products': (1, 2)},
        {'values': [8, 8, 3, 1, 2, 1], 'condition': 'TruePrice', 'products': (3, 4)},
        {'values': [8, 8, 3, 2, 2, 1], 'condition': 'TruePrice', 'products': (5, 6)},
        {'values': [8, 8, 2, 2, 2, 1], 'condition': 'TruePrice', 'products': (1, 2)},
        
        # TruePrice and Sustainability
        {'values': [8, 7, 2, 1, 1, 1], 'condition': 'TruePrice', 'products': (3, 4)},
        {'values': [9, 7, 2, 1, 1, 1], 'condition': 'TruePrice', 'products': (5, 6)},
        {'values': [9, 8, 2, 1, 1, 1], 'condition': 'TruePrice', 'products': (1, 2)},
        {'values': [7, 8, 2, 3, 1, 1], 'condition': 'TruePrice', 'products': (3, 4)},
        {'values': [9, 7, 3, 2, 1, 1], 'condition': 'TruePrice', 'products': (5, 6)},
        {'values': [9, 8, 3, 2, 1, 1], 'condition': 'TruePrice', 'products': (1, 2)},
        
        # PlainPrice and Label
        {'values': [5, 5, 2, 1, 2, 1], 'condition': 'PlainPrice', 'products': (3, 4)},
        {'values': [5, 5, 3, 1, 2, 1], 'condition': 'PlainPrice', 'products': (5, 6)},
        {'values': [5, 5, 3, 2, 2, 1], 'condition': 'PlainPrice', 'products': (1, 2)},
        {'values': [5, 5, 2, 2, 1, 2], 'condition': 'PlainPrice', 'products': (3, 4)},

        # PlainPrice and Sustainability
        {'values': [5, 4, 2, 1, 1, 1], 'condition': 'PlainPrice', 'products': (5, 6)},
        {'values': [6, 4, 2, 1, 1, 1], 'condition': 'PlainPrice', 'products': (1, 2)},
        {'values': [6, 5, 2, 1, 1, 1], 'condition': 'PlainPrice', 'products': (3, 4)},
        {'values': [5, 4, 3, 2, 1, 1], 'condition': 'PlainPrice', 'products': (5, 6)},
        {'values': [4, 6, 2, 3, 1, 1], 'condition': 'PlainPrice', 'products': (1, 2)},
        {'values': [6, 5, 3, 2, 1, 1], 'condition': 'PlainPrice', 'products': (3, 4)},
        
        # PriceRating and Label
        {'values': [2, 2, 2, 1, 1, 2], 'condition': 'PriceRating', 'products': (5, 6)},
        {'values': [2, 2, 3, 1, 1, 2], 'condition': 'PriceRating', 'products': (1, 2)},
        {'values': [2, 2, 3, 2, 1, 2], 'condition': 'PriceRating', 'products': (3, 4)},
        {'values': [2, 2, 2, 2, 2, 1], 'condition': 'PriceRating', 'products': (5, 6)},

        # PriceRating and Sustainability
        {'values': [2, 1, 2, 1, 1, 1], 'condition': 'PriceRating', 'products': (1, 2)},
        {'values': [3, 1, 2, 1, 1, 1], 'condition': 'PriceRating', 'products': (3, 4)},
        {'values': [3, 2, 2, 1, 1, 1], 'condition': 'PriceRating', 'products': (5, 6)},
        {'values': [2, 1, 3, 2, 1, 1], 'condition': 'PriceRating', 'products': (1, 2)},
        {'values': [3, 1, 3, 2, 1, 1], 'condition': 'PriceRating', 'products': (3, 4)},
        {'values': [2, 3, 2, 3, 1, 1], 'condition': 'PriceRating', 'products': (5, 6)},
    ]

    # Shuffle combinations to ensure random order
    random.shuffle(combinations)

    return combinations


def attributeList(lValues, lPos, condition, product_pair):
    lAttributes = []
    lOrder = []

    # Add product pair at the top without the 'Product' name
    lAttributes.append({
        'id': 'Product',
        'name': '',
        'lValues': [f"{C.imgProducts}{product_pair[0]}.png", f"{C.imgProducts}{product_pair[1]}.png"]
    })

    for i in range(len(C.lAttrID)):
        id = C.lAttrID[i]
        name = C.lAttrNames[i]
        lOrder.append(lPos.index(id))
        lPaths = []
        for v in lValues[i]:
            if id == "s":
                lPaths.append(f"{C.imgLeafs}{v}.png")
            elif id == "p":
                lPaths.append(f"{C.imgPrices}{v}.png")  # Use imgPrices for all price conditions
            else:
                lPaths.append(f"{C.imgLabels}{v}.png")

        Attr = {
            'id': id,
            'name': name,
            'lValues': lPaths,
        }
        lAttributes.append(Attr)

    lFinal = [lAttributes[0]] + [lAttributes[x + 1] for x in lOrder]
    return lFinal


class Message(Page):
    template_name = 'global/Message.html'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_PROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            MessageText='The practice rounds are over. <br> The experiment will start now.'
        )


class Decision(Page):
    form_model = 'player'
    form_fields = ['sStartDec', 'sEndDec', 'dRT_dec', 'sNames', 'sDT', 'sChoice']

    @staticmethod
    def vars_for_template(player: Player):
        p = player.participant
        lPos = random.sample(C.lAttrID, len(C.lAttrID))  # Randomize order of attributes per round
        p.lPos = lPos
        condition = p.sTreatment
        lValues = [
            [player.P1, player.P2],
            [player.S1, player.S2],
            [player.Q1, player.Q2]
        ]
        product_pair = (player.Product1, player.Product2)
        return dict(
            lAttr=attributeList(lValues, lPos, condition, product_pair),
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Log the values to ensure they are being captured correctly
        print('Before next page values:', {
            'sNames': player.sNames,
            'sDT': player.sDT,
            'sChoice': player.sChoice
        })


class FixCross(Page):
    form_model = 'player'
    form_fields = ['sStartCross', 'sEndCross']
    template_name = 'global/FixCross.html'


class SideButton(Page):
    form_model = 'player'
    form_fields = ['sStartCross', 'sEndCross']
    template_name = 'global/SideButton.html'

    @staticmethod
    def js_vars(player: Player):
        return dict(
            sPosition=player.sBetweenBtn
        )





page_sequence = [SideButton, Decision, Message]

# Ensure that SESSION_CONFIGS includes the app
SESSION_CONFIGS = [
    dict(
        name='task',
        display_name='Task',
        num_demo_participants=1,
        app_sequence=['Task']
    ),
]
