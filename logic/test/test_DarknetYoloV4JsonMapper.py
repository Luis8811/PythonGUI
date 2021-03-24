# Test of mapping a JSON obtained with Darknet (YoloV4)
import sys, os
sys.path.append('d:\\Back-end\\Django y Python\\Python_code\\GUI_TFM_Normandi\\PythonGUI\\logic\\json_darknet_mapper')
print(sys.path)
print("Testing OS")
newPath = sys.path[0]
pos = newPath.rfind(os.sep + "test")
newPath2 = newPath[:pos]
print(newPath2)
from frame import DarknetYoloV4JsonMapper, Frame, ObjectFromFrame

# Testing
print('TESTING MAPPING OF JSON FROM DARKNET (YOLOV4)')
pathToJsonYolov4 = 'PythonGUI\\logic\\test\\images\\image1.json'
listOfFramesForTest = DarknetYoloV4JsonMapper.getFramesFromJSON(pathToJsonYolov4)
DarknetYoloV4JsonMapper.printFrames(listOfFramesForTest)