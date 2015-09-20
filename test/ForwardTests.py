from domain.ForwardChainingEngine import ForwardChainingEngine

__author__ = 'Lucas'


def test_load_rules():
    fw_chaining_engine = ForwardChainingEngine()
    assert len(fw_chaining_engine.rules) == 3
    assert fw_chaining_engine.rules[0].conditions[0] == "dolor-panza"
    print "Test load rules OK"


test_load_rules()