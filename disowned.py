#!/usr/bin/env python3

from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from fpdf import FPDF
import ffmpeg

#TODO: Implement ffmpeg extracting
#magick montage -background #FFF -gravity East -geometry '1185x750+150+150' frame0000.png frame0001.png frame0002.png frame0004.png montage2.png
#magick composite -gravity center overlay.png montage2.png final.png

pdf = FPDF()
pdf.set_auto_page_break(0)
for image in imagelist:
    pdf.add_page()
    pdf.image(image,0,0,2970,2100)
    pdf.output("./output/flipbook.pdf", "F")

