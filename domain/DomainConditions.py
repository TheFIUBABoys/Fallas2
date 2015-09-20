__author__ = 'Lucas'


class DomainConditions:
    def __init__(self):
        self.domain_conditions = self.load_domain_conditions()

    @staticmethod
    def load_domain_conditions():
        conditions = []
        with open("resources/domainConditions") as f:
            for line in f:
                if line.rstrip() != "":
                    conditions.append((line.rstrip()))
        return conditions
