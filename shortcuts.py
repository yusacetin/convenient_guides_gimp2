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

# These options already exist under the default guides menu (Image->Guides) but I want to have them under
# my menu as well, you know, for convenience.

from gimpfu import *

# Remove all guides
def clear_guides(image, drawable):
    pdb.script_fu_guides_remove(image, drawable)

register(
    "ClearGuides",
    "Remove all guides.",
    "Remove all guides.",
    "Yusha Chetin",
    "Yusha Chetin",
    "2023",
    "<Image>/Convenient-Guides/Remove All Guides",
    "*",
    [],
    [],
    clear_guides
)

main()