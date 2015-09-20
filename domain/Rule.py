__author__ = 'Lucas'


class Rule:
    def __init__(self):
        self.conditions = []
        self.consequence = ""

    @staticmethod
    # Format: cause_1,cause_2, ... ,cause_n:consequence
    def rule_from_string(raw_rule):
        rule = Rule()
        conditions_consequence = raw_rule.split(":")
        conditions = conditions_consequence[0]
        rule.consequence = conditions_consequence[1]
        rule.conditions = conditions.split(",")
        return rule

    def matches_conditions(self, conditions):
        for condition in self.conditions:
            if condition not in conditions:
                return False
        return True

    def matches_consequence(self, consequence):
        return consequence == self.consequence

