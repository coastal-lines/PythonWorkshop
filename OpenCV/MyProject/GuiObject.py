from CommonHelpMethods import CommonHelpMethodsClass

class GuiObject():
    def __init__(self, name, parent, x, y, w, h, img):
        self.name = name
        self.parent = parent
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img