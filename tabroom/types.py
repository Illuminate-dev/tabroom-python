from enum import Enum

from .models import Event


class DebateEvent(Enum):
    LINCOLN_DOUGLAS = Event(id=102, name="Lincoln Douglas")
    POLICY = Event(id=103, name="Policy")
    PUBLIC_FORUM = Event(id=104, name="Public Forum")
    WORLDS_SCHOOLS = Event(id=105, name="Worlds Schools")
    DRAMATIC_INTERP = Event(id=204, name="Dramatic Interp")
    DUO_INTERP = Event(id=206, name="Duo Interp")
    EXTEMP = Event(id=202, name="Extemp")
    HUMOROUS_INTERP = Event(id=205, name="Humorous Interp")
    INFORMATIVE_SPEAKING = Event(id=208, name="Informative Speaking")
    ORAL_INTERP_OF_LITERATURE = Event(id=216, name="Oral Interp of Literature")
    ORIGINAL_ORATORY = Event(id=203, name="Original Oratory")
    PROGRAM_ORAL_INTERP = Event(id=207, name="Program Oral Interp")
    CONGRESSIONAL_DEBATE = Event(id=301, name="Congressional Debate")
