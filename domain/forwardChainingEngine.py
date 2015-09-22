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
        self.get_consequences_recur(self.rules)
        return self.domain_conditions.domain_conditions

    def get_consequences_recur(self, rules):
        matched = False
        non_matched_rules = []
        for rule in rules:
            if rule.matches_conditions(self.domain_conditions.domain_conditions):
                matched = True
                self.domain_conditions.domain_conditions.append(rule.consequence)
            else:
                non_matched_rules.append(rule)
        if matched:
            self.get_consequences_recur(non_matched_rules)
