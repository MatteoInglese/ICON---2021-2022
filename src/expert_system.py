# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 10:06:12 2022

@author: lncln
"""

from experta import *
from question_system import ask

def start_exsys():
    engine = DisDetectionEngine()
    engine.reset()
    engine.run()
    
class DisDetectionEngine(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        yield Fact(asking=True)


    #PRESENCE OF FAVORABLE ATMOSPHERIC CONDITIONS FOR DISEASES
    @Rule(Fact(asking=True))
    def ask_rainy(self):
        self.declare(Fact(is_rainy=ask("Ci sono state piogge abbondanti e frequenti nelle ultime settimane?")))

    @Rule(Fact(asking=True))
    def ask_rain_season(self):
        self.declare(Fact(is_rain_season=ask("Sei nella stagione delle piogge?")))

    @Rule(Fact(asking=True))
    def ask_temperature(self):
        self.declare(Fact(is_warm=ask("Le temperature sono particolarmente calde per il periodo dell'anno?")))

    @Rule(Fact(asking=True))
    def ask_drought(self):
        self.declare(Fact(is_drought=ask("Si sono verificati episodi di siccità nelle ultime settimane?")))

    @Rule(Fact(asking=True))
    def asj_humidity(self):
        self.declare(Fact(is_humid=ask("C'é stata molta umidità nelle ultime settimane?")))

    @Rule(AND(OR(Fact(is_rainy=True), Fact(is_rain_season=True)), OR(Fact(is_warm=True), Fact(is_drought=True)), Fact(is_humid=True)))
    def has_atm_cond_presence(self):
        self.declare(atm_cond_presence=True)


    #PRESENCE OF DISEASE SYMPTOM ON LEAFS
    @Rule(Fact(asking=True))
    def ask_basic_symp_leaf(self):
        self.declare(Fact(basic_symp_leaf=ask("Le foglie presentano macchie di qualche tipo?")))


    #COFFEE LEAF RUST
    @Rule(AND(Fact(atm_cond_presence=True), Fact(basic_symp_leaf=True)))
    def ask_basic_rust(self):
        self.declare(Fact(basic_rust=ask("Le macchie sono di colore giallo/arancione?")))

    @Rule(Fact(basic_rust=True))
    def ask_pustules(self):
        self.declare(Fact(has_pustules=ask("Le foglie presentano delle pustole?")))

    @Rule(Fact(basic_rust=True))
    def ask_back_leaf_symptom(self):
        self.declare(Fact(has_back_leaf_symptom=ask("Sono presenti macchie giallo-arancio o rosso-arancio sul retro delle foglie?")))

    @Rule(AND(Fact(basic_rust=True), Fact(has_pustules=True), Fact(has_back_leaf_symptom=True)))
    def leaf_rust(self):
        self.declare(has_leaf_rust=True)


    #BROWN EYE SPOT DISEASE
    @Rule(AND(Fact(atm_cond_presence=True), Fact(basic_symp_leaf=True), Fact(has_leaf_rust=False)))
    def ask_basic_brown(self):
        self.declare(Fact(has_basic_brown=ask("Le macchie sono di colore marrone all'esterno e grigie all'interno?")))

    @Rule(Fact(has_basic_brown=True))
    def ask_eye_symptom(self):
        self.declare(Fact(has_eye_symptom=ask("Hanno una forma che ricorda un occhio?")))

    @Rule(Fact(has_basic_brown=True))
    def ask_defoliate(self):
        self.declare(Fact(has_defoliation=ask("C'è un numero di foglie cadute prematuramente più alto del normale?")))

    @Rule(AND(Fact(has_eye_symptom=True), Fact(has_defoliation=True)))
    def brown_eye_disease(self):
        self.declare(Fact(has_brown_eye_disease=True))


    #BLACK ROT
    @Rule(AND(Fact(atm_cond_presence=True), Fact(basic_symp_leaf=True), Fact(has_leaf_rust=False), Fact(has_brown_eye_disease=False)))
    def ask_basic_black(self):
        self.declare(Fact(has_basic_black=ask("Le foglie sono di colore marrone scuro o nere per la maggior parte della loro superficie?")))

    @Rule(Fact(has_basic_black=True))
    def ask_drops(self):
        self.declare(Fact(has_leaves_and_berry_drops=ask("Hai notato un gran numero di foglie e bacche cadute prematuramente?")))

    @Rule(Fact(has_leaves_and_berry_drops=True))
    def black_rot(self):
        self.declare(Fact(has_black_rot=True))


    #DISPLAYING RESULTS
    @Rule(Fact(atm_cond_presence=True))
    def print_atm(self):
        print("Le condizioni atmosferiche favoriscono l'insorgere di malattie foliari.")

    @Rule(Fact(has_leaf_rust=True))
    def print_rust(self):
        print("Rilevata presenza della ruggine foliare del caffé.")

    @Rule(Fact(has_brown_eye_disease=True))
    def print_brown_eye(self):
        print("Rilevata presenza della malattia dell'occhio marrone.")

    @Rule(Fact(has_black_rot=True))
    def print_black_rot(self):
        print("Rilevata presenza di marciume foliare.")

    @Rule(AND(Fact(has_leaf_rust=False),Fact(has_brown_eye_disease=False),Fact(has_black_rot=False)))
    def print_no_diseases(self):
        print("Non è stata rilevata alcuna malattia foliare.")