# -*- coding: utf-8 -*-
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
    def ask_drought(self):
        self.declare(Fact(is_drought=ask("Si sono verificati episodi di siccità nelle ultime settimane?")))

    @Rule(Fact(asking=True))
    def ask_humidity(self):
        self.declare(Fact(is_humid=ask("C'é stata molta umidità nelle ultime settimane?")))

    @Rule(AND(Fact(is_rainy=True), Fact(is_drought=True), Fact(is_humid=True)))
    def has_atm_cond_presence(self):
        self.declare(Fact(atm_cond_presence=True))

    @Rule(OR(Fact(is_rainy=False), Fact(is_drought=False), Fact(is_humid=False)))
    def has_not_atm_cond_presence(self):
        self.declare(Fact(atm_cond_presence=False))


    #PRESENCE OF DISEASE SYMPTOM ON LEAFS
    @Rule(Fact(asking=True))
    def ask_basic_symp_leaf(self):
        self.declare(Fact(basic_symp_leaf=ask("Le foglie presentano macchie di qualche tipo?")))

    @Rule(AND(Fact(atm_cond_presence=True), Fact(basic_symp_leaf=True)))
    def has_basic(self):
        self.declare(Fact(has_basic=True))

    @Rule(OR(Fact(atm_cond_presence=False), Fact(basic_symp_leaf=False)))
    def has_not_basic(self):
        self.declare(Fact(has_basic=False))

    @Rule(Fact(has_basic=False))
    def no_diseases(self):
        self.declare(Fact(has_leaf_rust=False))
        self.declare(Fact(has_brown_eye_disease=False))
        self.declare(Fact(has_black_rot=False))

    #COFFEE LEAF RUST
    @Rule(Fact(has_basic=True))
    def ask_basic_rust(self):
        self.declare(Fact(basic_rust=ask("Le macchie sono di colore giallo/arancione?")))

    @Rule(Fact(has_basic=False))
    def no_rust(self):
        self.declare(Fact(has_leaf_rust=False))

    @Rule(Fact(basic_rust=True))
    def ask_pustules(self):
        self.declare(Fact(has_pustules=ask("Le foglie presentano delle pustole?")))

    @Rule(Fact(basic_rust=True))
    def ask_back_leaf_symptom(self):
        self.declare(Fact(has_back_leaf_symptom=ask("Sono presenti macchie giallo-arancio o rosso-arancio sul retro delle foglie?")))

    @Rule(AND(Fact(basic_rust=True), Fact(has_pustules=True), Fact(has_back_leaf_symptom=True)))
    def leaf_rust(self):
        self.declare(Fact(has_leaf_rust=True))

    @Rule(OR(Fact(basic_rust=False), Fact(has_pustules=False), Fact(has_back_leaf_symptom=False)))
    def not_leaf_rust(self):
        self.declare(Fact(has_leaf_rust=False))


    #BROWN EYE SPOT DISEASE
    @Rule(AND(Fact(has_basic=True), Fact(has_leaf_rust=False)))
    def ask_basic_brown(self):
        self.declare(Fact(has_basic_brown=ask("Le macchie sono di colore marrone all'esterno e grigie all'interno?")))

    @Rule(Fact(has_basic_brown=True))
    def ask_eye_symptom(self):
        self.declare(Fact(has_eye_symptom=ask("Hanno una forma che ricorda un occhio?")))

    @Rule(Fact(has_basic_brown=False))
    def no_eye_symptom(self):
        self.declare(Fact(has_brown_eye_disease=False))

    @Rule(Fact(has_basic_brown=True))
    def ask_defoliate(self):
        self.declare(Fact(has_defoliation=ask("C'è un numero di foglie cadute prematuramente più alto del normale?")))

    @Rule(AND(Fact(has_eye_symptom=True), Fact(has_defoliation=True)))
    def brown_eye_disease(self):
        self.declare(Fact(has_brown_eye_disease=True))

    @Rule(OR(Fact(has_eye_symptom=False), Fact(has_defoliation=False)))
    def not_brown_eye_disease(self):
        self.declare(Fact(has_brown_eye_disease=False))


    #BLACK ROT
    @Rule(AND(Fact(has_basic=True), Fact(has_leaf_rust=False), Fact(has_brown_eye_disease=False)))
    def ask_basic_black(self):
        self.declare(Fact(has_basic_black=ask("Le foglie sono di colore marrone scuro o nere per la maggior parte della loro superficie?")))

    @Rule(Fact(has_basic_black=True))
    def ask_drops(self):
        self.declare(Fact(has_leaves_and_berry_drops=ask("Hai notato un gran numero di foglie e bacche cadute prematuramente?")))

    @Rule(Fact(has_leaves_and_berry_drops=True))
    def black_rot(self):
        self.declare(Fact(has_black_rot=True))

    @Rule(Fact(has_leaves_and_berry_drops=False))
    def not_black_rot(self):
        self.declare(Fact(has_black_rot=False))


    #DISPLAYING RESULTS
    @Rule(AND(Fact(has_leaf_rust=False),Fact(has_brown_eye_disease=False),Fact(has_black_rot=False), Fact(has_basic=True)))
    def print_basic(self):
        print("E' possibile che siano presenti malattie fogliari sconosciute.")
        self.reset()

    @Rule(AND(Fact(has_leaf_rust=False), Fact(has_brown_eye_disease=False), Fact(has_black_rot=False)))
    def print_no_basic(self):
        print("Le condizioni non sono compatibili con le malattie fogliari.")
        self.reset()

    @Rule(Fact(has_leaf_rust=True))
    def print_rust(self):
        print("Possibile presenza della ruggine foliare del caffé.")
        self.reset()

    @Rule(Fact(has_brown_eye_disease=True))
    def print_brown_eye(self):
        print("Possibile presenza della malattia dell'occhio marrone.")
        self.reset()

    @Rule(Fact(has_black_rot=True))
    def print_black_rot(self):
        print("Possibile presenza di marciume foliare.")
        self.reset()
