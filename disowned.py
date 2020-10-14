#!/usr/bin/env python3

from fpdf import FPDF
from math import ceil
from shutil import copyfile
import os
import subprocess
import ffmpeg

#TODO: Implement ffmpeg extracting

frame_list = os.listdir("tmp/frames/")
blank_frames = 4 - len(frame_list)%4

# Add blank frames to the list and folder for the pages to format properly
for frame in range(0, blank_frames):
    frame_id = (len(frame_list))
    frame_list.append("p{}.png".format(frame_id))
    copyfile("resources/pixel.jpg", "tmp/frames/p{}.png".format(frame_id))

# Sort the list, prepare number of pages
frame_list.sort()
number_of_pages = int(len(frame_list)/4)

# Make the inital .jpg pages
for page in range(0, number_of_pages):
    print("Page number " + str(page))
    cmd = "montage -gravity East -geometry '1185x750+150+150' tmp/frames/{} tmp/frames/{} tmp/frames/{} tmp/frames/{} tmp/pages/{}.jpg".format(
        frame_list[0], frame_list[1], frame_list[2], frame_list[3], page
    )
    subprocess.run(cmd, shell=True)
    del frame_list[0:4]

# Overlay the borders to the pages
for page in range(0, number_of_pages):
    cmd = "composite -gravity center resources/overlay.png tmp/pages/{page}.jpg tmp/pages/{page}.jpg".format(
        page = page
    )
    subprocess.run(cmd, shell=True)

# Output the results in a single pdf
pdf = FPDF()
pdf.set_auto_page_break(0)
for page in range(0, number_of_pages):
    pdf.add_page(orientation = "L")
    pdf.image("tmp/pages/{}.jpg".format(page), 0, 0, 297, 210)
pdf.output("./output/flipbook.pdf", "F")
