import cv2
import numpy as np
import operator
import progressbar
import xml.etree.ElementTree as ET

class Slide:
	def __init__(self, order_id, time_sec, time, slide_name):
		self.order_id = order_id
		self.time_sec = time_sec
		self.time = time
		self.slide_name = slide_name
		
	def __str__(self):
		return f"orderId: {self.order_id} timeSec: {self.time_sec} time: {self.time} slideName: {self.slide_name}"
		
	def __repr__(self):
		return self.__str__()
	
	
slides = []

for child in ET.parse('38926829.xml').getroot().iter('slide'):
	order_id = int(child.find('orderId').text)
	time_sec = int(child.find('timeSec').text)
	time = int(child.find('time').text)
	slide_name = child.find('slideName').text
	
	slide = Slide(order_id, time_sec, time, slide_name)
	
	slides.append(slide)
	
slides = sorted(slides, key=operator.attrgetter('order_id'))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('slides.mp4', fourcc, 1.0, (1024, 576))

for i in progressbar.progressbar(range(0, len(slides)-1)):
	frame_count = slides[i + 1].time_sec - slides[i].time_sec
	frame = cv2.imread(f"slides/{slides[i].slide_name}.jpg")
	for j in range(frame_count):
		out.write(frame)

out.release()
	