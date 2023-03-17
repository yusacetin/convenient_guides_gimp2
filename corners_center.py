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

# Guides to both the center and the corners
def center_and_corners(image, drawable):
    center(image, drawable)
    corners(image, drawable)

# Guides to center
def center(image, drawable):
    # Get image half width and half height
    img_half_width = pdb.gimp_image_width(image)/2
    img_half_height = pdb.gimp_image_height(image)/2
    # Draw the center guides
    pdb.gimp_image_add_hguide(image, img_half_height)
    pdb.gimp_image_add_vguide(image, img_half_width)

# Guides to corners
def corners(image, drawable):
    # Get image width and height
    img_width = pdb.gimp_image_width(image)
    img_height = pdb.gimp_image_height(image)
    # Draw guides on the top left corner
    pdb.gimp_image_add_hguide(image, 0)
    pdb.gimp_image_add_vguide(image, 0)
    # Draw guides on the top right corner
    pdb.gimp_image_add_hguide(image, 0)
    pdb.gimp_image_add_vguide(image, img_width)
    # Draw guides on the bottom left corner
    pdb.gimp_image_add_hguide(image, img_height)
    pdb.gimp_image_add_vguide(image, 0)
    # Draw guides on the bottom right corner
    pdb.gimp_image_add_hguide(image, img_height)
    pdb.gimp_image_add_vguide(image, img_width)

##############################
### Register the Functions ###
##############################

register(
    "GuidesToCorners",
    "Add guides to all corners.",
    "Add guides to all corners.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Guides to Corners",
    "*",
    [],
    [],
    corners
)

register(
    "GuidesToCenter",
    "Add guides to image center.",
    "Add guides to image center.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Guides to Center",
    "*",
    [],
    [],
    center
)

register(
    "GuidesToCenterAndCorners",
    "Add guides to image center and corners.",
    "Add guides to image center and corners.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Guides to Center and Corners",
    "*",
    [],
    [],
    center_and_corners
)

# idk but it doesn't work without this
main()