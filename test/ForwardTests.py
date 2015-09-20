from domain.forwardChainingEngine import ForwardChainingEngine

__author__ = 'Lucas'


def test_load_rules():
    fw_chaining_engine = ForwardChainingEngine()
    assert len(fw_chaining_engine.rules) == 5
    assert fw_chaining_engine.rules[0].conditions[0] == "dolor-panza"
    print "Test load rules OK"


def test_conditions_matched():
    fw_chaining_engine = ForwardChainingEngine()
    consequences = fw_chaining_engine.get_consequences()
    assert len(consequences) == 2
    assert consequences[0] == "gastroenteritis"
    assert consequences[1] == "gripe"
    print "Test get consequences OK"



test_load_rules()
test_conditions_matched()
