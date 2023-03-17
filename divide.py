#! /usr/bin/env python2

####################################################################################################
# This file is part of Convenient Guides for GIMP 2.10.
#
# Convenient Guides for GIMP 2.10 is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your option)
# any later version.
# 
# Convenient Guides for GIMP 2.10 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with Convenient Guides
# for GIMP 2.10. If not, see <https://www.gnu.org/licenses/>.
####################################################################################################

from gimpfu import *

###############################
### Implement the Functions ###
###############################

# Both vertical and horizontal division
def vhdivide(image, drawable, nvh):
    vdivide(image, drawable, nvh)
    hdivide(image, drawable, nvh)

# Vertical division
def vdivide(image, drawable, nv):
    # Get image width
    img_width = pdb.gimp_image_width(image)
    # Calculate the gap between consecutive guides
    hgap = img_width / nv
    for i in range(nv+1):
        pdb.gimp_image_add_vguide(image, i*hgap)

# Horizontal division
def hdivide(image, drawable, nh):
    # Get image height
    img_width = pdb.gimp_image_height(image)
    # Calculate the gap between consecutive guides
    vgap = img_width / nh
    for i in range(nh+1):
        pdb.gimp_image_add_hguide(image, i*vgap)

##############################
### Register the Functions ###
##############################

register(
    "VerticalDivide",
    "Vertically divide into equal parts. Note that the number of parts must be a divisor of the image width, otherwise the guides won't be placed properly.",
    "Vertically divide into equal parts. Note that the number of parts must be a divisor of the image width, otherwise the guides won't be placed properly.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Divide/Vertically Divide into Equal Parts",
    "*",
    [
        (PF_INT32, "nv", "Number of Parts: ", 4),
    ],
    [],
    vdivide
)

register(
    "HorizontalDivide",
    "Horizontally divide into equal parts. Note that the number of parts must be a divisor of the image height, otherwise the guides won't be placed properly.",
    "Horizontally divide into equal parts. Note that the number of parts must be a divisor of the image height, otherwise the guides won't be placed properly.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Divide/Horizontally Divide into Equal Parts",
    "*",
    [
        (PF_INT32, "nh", "Number of Parts: ", 4),
    ],
    [],
    hdivide
)

register(
    "VerticalAndHorizontalDivide",
    "Vertically and horizontally divide into equal parts. Note that the number of parts must be a divisor of both the width and the height of the image, otherwise the guides won't be placed properly.",
    "Vertically and horizontally divide into equal parts. Note that the number of parts must be a divisor of both the width and the height of the image, otherwise the guides won't be placed properly.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Divide/Vertically and Horizontally Divide into Equal Parts",
    "*",
    [
        (PF_INT32, "nvh", "Number of Parts: ", 4),
    ],
    [],
    vhdivide
)

# idk but it doesn't work without this
main()