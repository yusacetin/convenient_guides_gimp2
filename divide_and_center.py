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

# Both vertical and horizontal
def vhdivide_and_center(image, drawable, nvh):
    vdivide_and_center(image, drawable, nvh)
    hdivide_and_center(image, drawable, nvh)

# Vertical
def vdivide_and_center(image, drawable, nv):
    # Get image width
    img_width = pdb.gimp_image_width(image)
    # Calculate the gap between consecutive guides
    hgap = img_width / nv
    # Calculate the margin necessary for the guide to be centered
    hmargin = hgap / 2
    for i in range(nv):
        pdb.gimp_image_add_vguide(image, hmargin + i*hgap)

# Horizontal
def hdivide_and_center(image, drawable, nh):
    # Get image height
    img_width = pdb.gimp_image_height(image)
    # Calculate the gap between consecutive guides
    vgap = img_width / nh
    # Calculate the margin necessary for the guide to be centered
    vmargin = vgap / 2
    for i in range(nh):
        pdb.gimp_image_add_hguide(image, vmargin + i*vgap)

##############################
### Register the Functions ###
##############################

register(
    "VerticalDivideAndCenter",
    "Place horizontal guides to the centers of parts of a vertical equal parts division operation. Note that two times the number of parts must be a divisor of the image width, otherwise the guides won't be placed properly.",
    "Place horizontal guides to the centers of parts of a vertical equal parts division operation. Note that two times the number of parts must be a divisor of the image width, otherwise the guides won't be placed properly.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Divide and Center/Guides to Centers of Equally Divided Vertical Parts",
    "*",
    [
        (PF_INT32, "nv", "Number of Parts: ", 4),
    ],
    [],
    vdivide_and_center
)

register(
    "HorizontalDivideAndCenter",
    "Place vertical guides to the centers of parts of a horizontal equal parts division operation. Note that two times the number of parts must be a divisor of the image height, otherwise the guides won't be placed properly.",
    "Place vertical guides to the centers of parts of a horizontal equal parts division operation. Note that two times the number of parts must be a divisor of the image height, otherwise the guides won't be placed properly.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Divide and Center/Guides to Centers of Equally Divided Horizontal Parts",
    "*",
    [
        (PF_INT32, "nh", "Number of Parts: ", 4),
    ],
    [],
    hdivide_and_center
)

register(
    "VerticalAndHorizontalDivideAndCenter",
    "Place vertical and horizontal guides to the centers of parts of an equal parts division operation. Note that two times the number of parts must be a divisor of both the width and the height of the image, otherwise the guides won't be placed properly.",
    "Place vertical and horizontal guides to the centers of parts of an equal parts division operation. Note that two times the number of parts must be a divisor of both the width and the height of the image, otherwise the guides won't be placed properly.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Divide and Center/Guides to Centers of Equally Divided Horizontal and Vertical Parts",
    "*",
    [
        (PF_INT32, "nvh", "Number of Parts: ", 4),
    ],
    [],
    vhdivide_and_center
)

# idk but it doesn't work without this
main()