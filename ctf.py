import os
from collections import Counter
from PIL import Image


def split_image():
    should_square = False
    should_quiet=False
    im = Image.open("ctf.png")
    im_width, im_height = im.size
    row_width = int(im_width / 3)
    row_height = int(im_height / 3)
    name, ext = os.path.splitext("ctf.png")
    name = os.path.basename(name)
    if should_square:
        min_dimension = min(im_width, im_height)
        max_dimension = max(im_width, im_height)
        if not should_quiet:
            print("Resizing image to a square...")
            print("Determining background color...")
        bg_color = determine_bg_color(im)
        if not should_quiet:
            print("Background color is... " + str(bg_color))
        im_r = Image.new("RGBA" if ext == "png" else "RGB",
                         (max_dimension, max_dimension), bg_color)
        offset = int((max_dimension - min_dimension) / 2)
        if im_width > im_height:
            im_r.paste(im, (0, offset))
        else:
            im_r.paste(im, (offset, 0))
        if not should_quiet:
            print("Exporting resized image...")
        outp_path = name + "_squared" + ext
        outp_path = os.path.join(r"C:\Users\CatHouse13\Documents\Intern\ITPSS\CTF\Project4", outp_path)
        im_r.save(outp_path)
        im = im_r
        row_width = int(max_dimension / 3)
        row_height = int(max_dimension / 3)
    n = 0
    for i in range(0, 3):
        for j in range(0, 3):
            box = (j * row_width, i * row_height, j * row_width +
                   row_width, i * row_height + row_height)
            # code for shuffling or rotating the croped image
            outp = im.crop(box).rotate(180)
            outp_path = name + "_" + str(n) + ext
            outp_path = os.path.join(r"C:\Users\CatHouse13\Documents\Intern\ITPSS\CTF\Project4", outp_path)
            if not should_quiet:
                print("Exporting image tile: " + outp_path)
            outp.save(outp_path)
            n += 1

def determine_bg_color(im):
    im_width, im_height = im.size
    rgb_im = im.convert('RGBA')
    all_colors = []
    areas = [[(0, 0), (im_width, im_height / 10)],
             [(0, 0), (im_width / 10, im_height)],
             [(im_width * 9 / 10, 0), (im_width, im_height)],
             [(0, im_height * 9 / 10), (im_width, im_height)]]
    for area in areas:
        start = area[0]
        end = area[1]
        for x in range(int(start[0]), int(end[0])):
            for y in range(int(start[1]), int(end[1])):
                pix = rgb_im.getpixel((x, y))
                all_colors.append(pix)
    return Counter(all_colors).most_common(1)[0][0]

def reverse_split():
    path_to_merge = ""

def main():
    split_image() # splitting image into a certain columns and rows

if __name__ == "__main__":
    main()