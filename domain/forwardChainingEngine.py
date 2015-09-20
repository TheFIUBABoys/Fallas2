from domain.DomainConditions import DomainConditions
from domain.Rule import Rule

__author__ = 'Lucas'


class ForwardChainingEngine:
    def __init__(self):
        self.rules = self.load_rules()
        self.domain_conditions = DomainConditions()

    @staticmethod
    def load_rules():
        rules = []
        with open("../resources/rules") as f:
            for line in f:
                if line.rstrip() != "":
                    rules.append(Rule.rule_from_string(line.rstrip()))
        return rules

    def get_consequences(self):
        initial_conditions = self.domain_conditions.domain_conditions
        consequences = []
        for rule in self.rules:
            if rule.matches_conditions(initial_conditions):
                consequences.append(rule.consequence)
        return consequences



