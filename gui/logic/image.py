class Image:

    def __init__(self, height, width, objects):
        self.height = height
        self.width = width
        self.objects = objects

    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getObjects(self):
        return self.objects
    
    def setHeight(self, height):
        self.height = height
    
    def setWidth(self, width):
        self.width = width
    
    def setObjects(self, objects):
        self.objects = objects

