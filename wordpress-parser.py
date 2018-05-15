#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('/Users/johnproppe/Desktop/cxm-final.xml')
root = tree.getroot()

f = open('/Users/johnproppe/Desktop/cxm-posts-category.csv', 'w')

csvwriter = csv.writer(f)

count = 0

head = ['Post Title','Post Link', 'Category']

csvwriter.writerow(head)

for item in root.iter('item'):
	row = []
	title = item.find('title').text
	row.append(title)
	link = item.find('link').text
	row.append(link)
	category = item.find('category').text
	row.append(category)
	csvwriter.writerow(row)
f.close()

tree.write('/Users/johnproppe/Desktop/cxm-final-cleaned.xml')