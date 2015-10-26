from functools import partial

__author__ = 'joaquin'


class Slot:

    def __init__(self, name, value=None):

        def f():
            pass

        self.name = name
        self.value = value
        self.if_added = f
        self.if_removed = f
        self.if_needed = f

    def get_name(self):
        return self.name

    def set_if_needed(self, if_needed):
        self.if_needed = partial(if_needed, self)

    def set_if_added(self, if_added):
        self.if_added = partial(if_added, self)

    def set_if_removed(self, if_removed):
        self.if_removed = partial(if_removed, self)

    def get_value(self):
        #trigger if-needed-procedure (must be defined from outside) in case value null
        if not self.value:
            return self.if_needed()
        return self.value

    def set_value(self, value):
        self.if_added()
        self.value = value
        return self.value

    def delete_value(self):
        self.if_removed()
        self.value = None


class Frame:

    def __init__(self, name):
        self.name = name
        self.slots = {}
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def add_slot(self, slot):
        self.slots[slot.get_name()] = slot

    def get_slot_value(self, slot_name):
        if slot_name in self.slots:
            return self.slots[slot_name].get_value()
        elif self.parent:
            return self.parent.get_slot_value(slot_name)
        return None

    def set_slot_value(self, slot_name, new_value):
        slot = self.slots[slot_name]
        slot.set_value(new_value)

    def remove_slot_value(self, slot_name):
        slot = self.slots[slot_name]
        slot.delete_value()

    def get_slots(self):
        return self.slots.values


frame1 = Frame("cabras")
fecha_de_revision = Slot("fecha_revision")


def if_added(slot):
    print slot.value + " value added"


def if_removed(slot):
    print slot.value + " being removed"


def if_needed(slot):
    slot.value = "ayer"
    print slot.value + " provided"

fecha_de_revision.set_if_added(if_added)
fecha_de_revision.set_if_removed(if_removed)
fecha_de_revision.set_if_needed(if_needed)

frame1.add_slot(fecha_de_revision)

frame_parent = Frame("parent of cabras")
frame1.set_parent(frame_parent)

spoderman = Slot("spoderman", "y u do dis")
frame_parent.add_slot(spoderman)

frame1.get_slot_value("fecha_revision")
frame1.set_slot_value("fecha_revision", "hoy")
frame1.remove_slot_value("fecha_revision")

print frame1.get_slot_value("spoderman")
