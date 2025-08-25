from enum import Enum

class ElementState(str, Enum):
# Inheritance from str makes enum members strings rather than Enum objects
    VISIBLE = "visible"
    HIDDEN = "hidden"
    ATTACHED = "attached"
    DETACHED = "detached"
