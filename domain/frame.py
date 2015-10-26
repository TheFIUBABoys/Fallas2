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
        if not self.value:
            return self.if_needed()
        return self.value

    def set_value(self, value):
        self.value = value
        self.if_added()
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


frame_conferencia = Frame("Conferencia")
frame_conferencia.add_slot(Slot("Fecha"))
frame_conferencia.set_slot_value("Fecha", "22/12/2015")

frame_conferencia_distribucion = Frame("Conferencia: Distribucion")
frame_conferencia_distribucion.add_slot(Slot("Tema"))
frame_conferencia_distribucion.set_slot_value("Tema", "Distribucion")

frame_conferencia_desarrollo = Frame("Conferencia: Desarrollo")
frame_conferencia_desarrollo.add_slot(Slot("Tema"))
frame_conferencia_distribucion.set_slot_value("Tema", "Desarrollo")


frame_conferencia_distribucion1 = Frame("Conferencia: Distribucion #1")
slot_participantes = Slot("Participantes")

def if_added(participante):
    if participante.value == "Juancho":
        frame_participante_juancho.set_slot_value("Agenda", "Conferencia el " + frame_conferencia_distribucion1.get_slot_value("Fecha"))
        print "Agendado para Juancho: " + frame_participante_juancho.get_slot_value("Agenda")

slot_participantes.set_if_added(if_added)
frame_conferencia_distribucion1.add_slot(Slot("Lugar"))
frame_conferencia_distribucion1.add_slot(slot_participantes)

frame_conferencia_distribucion.set_parent(frame_conferencia)
frame_conferencia_desarrollo.set_parent(frame_conferencia)
frame_conferencia_distribucion1.set_parent(frame_conferencia_distribucion)


frame_participante_juancho = Frame("Juancho")
frame_participante_juancho.add_slot(Slot("Agenda"))

frame_conferencia_distribucion1.set_slot_value("Lugar", "3er Piso")
frame_conferencia_distribucion1.set_slot_value("Participantes", "Juancho")


print "Conferencia de desarrollo #1"
print "\t" + frame_conferencia_distribucion1.get_slot_value("Fecha")
print "\t" + frame_conferencia_distribucion1.get_slot_value("Tema")
print "\t" + frame_conferencia_distribucion1.get_slot_value("Lugar")
print "\t" + frame_conferencia_distribucion1.get_slot_value("Participantes")

print "Agenda de Juancho"
print "\t" + frame_participante_juancho.get_slot_value("Agenda")
