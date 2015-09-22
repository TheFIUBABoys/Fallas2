from domain.Rule import Rule

__author__ = 'Lucas'


def test_parse_rule_one_cond():
    rule = Rule.rule_from_string("R1-asd:a")
    assert rule.conditions[0] == "asd"
    assert rule.consequence == "a"
    assert rule.name == "R1"


def test_parse_rule_several_conds():
    rule = Rule.rule_from_string("R2-asd,dsa,123:b")
    assert rule.conditions[0] == "asd"
    assert rule.conditions[1] == "dsa"
    assert rule.conditions[2] == "123"
    assert rule.consequence == "b"
    assert rule.name == "R2"


test_parse_rule_one_cond()
test_parse_rule_several_conds()
print "TESTS OK"
