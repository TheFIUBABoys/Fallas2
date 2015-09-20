from domain.DomainConditions import DomainConditions
from domain.Rule import Rule

__author__ = 'Joaquin'


class BackwardsChainingEngine:
    def __init__(self):
        self.rules = self.load_rules()
        self.domain_conditions = DomainConditions()

    @staticmethod
    def load_rules():
        rules = []
        with open("resources/rules") as f:
            for line in f:
                if line.rstrip() != "":
                    rules.append(Rule.rule_from_string(line.rstrip()))
        return rules

    def get_consequences(self, hypothesis):
        initial_conditions = self.domain_conditions.domain_conditions

        return self._get_consequences(initial_conditions, hypothesis)

    def _get_consequences(self, knowledge_base, hypothesis):

        if hypothesis in knowledge_base:
            return knowledge_base

        for rule in self.rules:
            if rule.matches_consequence(hypothesis):
                for condition in rule.conditions:
                    if condition not in knowledge_base:
                        knowledge_base = self._get_consequences(knowledge_base, condition)
                if rule.matches_conditions(knowledge_base):
                    knowledge_base.append(hypothesis)
                    return knowledge_base
        return knowledge_base



