from graphviz import Digraph
from sets import Set

__author__ = 'lucas'


class SemanticNetwork:
    def __init__(self):
        self.dot = Digraph(comment='Graph')
        self.adjacency_matrix = {}
        self.edge_labels = {}
        self.load_domain_conditions()
        self.startingNode = ""
        self.computed_relations = {}

    def load_domain_conditions(self):
        with open("../resources/semanticNetworkData") as f:
            for line in f:
                line = line.split("\n")[0]
                if line.rstrip() != "":
                    values = line.split(",")
                    start = values[0]
                    end = values[1]
                    label = values[2]
                    if not start in self.adjacency_matrix:
                        self.adjacency_matrix[start] = [end]
                    else:
                        self.adjacency_matrix[start].append(end)
                    self.edge_labels[(start, end)] = label
                    self.dot.node(start)
                    self.dot.node(end)
                    self.dot.edge(start, end, label)
                    # self.dot.render('test-output/round-table.gv', view=True)

    def get_conclusions_for(self, startingNode):
        self.startingNode = startingNode
        self.computed_relations = {}
        node_set = Set([startingNode])
        return self.get_conclusions_recur(node_set)

    def get_conclusions_recur(self, node_set):
        new_node_set = Set(node_set)
        changed = False
        print node_set
        for node in node_set:
            if node in self.adjacency_matrix:
                old_len = len(new_node_set)
                for item in self.adjacency_matrix[node]:
                    new_node_set.add(item)
                    if len(new_node_set) != old_len:
                        changed = True
                        self.computed_relations[item] = self.edge_labels[(node, item)]

        if changed:
            return self.get_conclusions_recur(new_node_set)

        final_info = []
        for item in new_node_set:
            if item == self.startingNode:
                continue
            if item in self.adjacency_matrix.keys():
                end = self.adjacency_matrix[item]
                for target in end:
                    if (item, target) in self.edge_labels:
                        if self.get_conclusion_string(item) not in final_info:
                            final_info.append(self.get_conclusion_string(item))
            else:
                if self.get_conclusion_string(item) not in final_info:
                    final_info.append(self.get_conclusion_string(item))
        return final_info

    def get_conclusion_string(self, item):
        return self.startingNode + self.computed_relations[item] + " " + item


n = SemanticNetwork()
print n.get_conclusions_for("dog")
