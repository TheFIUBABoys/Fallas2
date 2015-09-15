__author__ = 'Lucas'
class Rule:
    def __init__(self):
        self.conditions = []
        self.consequence = ""

    @staticmethod
    # Format: cause_1,cause_2, ... ,cause_n:consequence
    def rule_from_string(raw_rule):
        rule = Rule()
        conditions_consecuence = raw_rule.split(":")
        conditions = conditions_consecuence[0]
        rule.consequence = conditions_consecuence[1]
        rule.conditions = conditions.split(",")
        return rule

