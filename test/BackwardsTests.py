from domain.backwardsChainingEngine import BackwardsChainingEngine

__author__ = 'Joaquin'


def test_load_rules():
    bw_chaining_engine = BackwardsChainingEngine()
    assert len(bw_chaining_engine.rules) == 5
    assert bw_chaining_engine.rules[0].conditions[0] == "dolor-panza"
    print "Test load rules OK"


def test_conditions_matched():
    bw_chaining_engine = BackwardsChainingEngine()
    knowledge_base = bw_chaining_engine.get_consequences("epilepsia")
    assert knowledge_base == ['dolor-cabeza', 'fiebre', 'dolor-panza', 'mareos', 'convulsiones', 'epilepsia']
    print knowledge_base



test_load_rules()
test_conditions_matched()
