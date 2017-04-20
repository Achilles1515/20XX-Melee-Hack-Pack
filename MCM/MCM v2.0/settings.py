# Written in Python v2.7.9 by DRGN of SmashBoards (Daniel R. Cappel).
# Version 2.0
# Find the official thread here for usage and other documentation: 
# http://smashboards.com/threads/melee-code-manager-easily-add-codes-to-your-game.416437/

# These are hex ranges that indicate safe areas for custom code. The regions in this first list are the same between all  
# game versions, hence the name, "common" Code regions. Between each set of parenthesis, you have the start
# of a region, followed by the end of that region. If you would like the program to ignore one of these regions,
# then you may erase it from this list. (However, I recommend making a copy of the line first, in case you make a mistake or
# would like to undo it later. Then, just comment out the backup line by preceding it with a '#'.)
#
# Remember that each entry needs to be followed by a comma, except for the last one.
#
# If you'd like to remove all of these regions, you still need to preserve the variable here. Just make it equal to an empty 
# pair of brackets, i.e. "commonCodeRegions = []"
#
# You may also add regions. Just be sure that you know what you're doing and have tested it, and that no regions overlap with one another!

commonCodeRegions = [( 0x32C998, 0x332834 ), ( 0x407540, 0x408F00 ), ( 0x18DCC0, 0x197B2C )]						# 0xCC, 0xCC, 0xCC 			= 0x264
																											 # Total space of above: 0x1898

# The regions below are used for the game's Debug Menu, which some users may not want to overwrite (hence the toggle option 
# already available in the program. Use that if you'd like to ignore this area).

v102DebugModeRegion = (0x3f7124, 0x3fac20) # Total space: 0x3AFC (same for all game versions)
v101DebugModeRegion = (0x3f6444, 0x3f9f40)
v100DebugModeRegion = (0x3f5294, 0x3f8d90)
vPALDebugModeRegion = (0x3f7ecc, 0x3fbae8)	


# The original purpose of the first 5 regions below (per game version) is for the unused 'USB Screenshot' function, described here:
# http://smashboards.com/threads/the-dol-mod-topic.326347/page-11#post-19130116
# 
# If they are used, then the following changes need to be made: 0x1a1b64 --> 60000000, 0x1a1c50 --> 60000000 (nops the branch links)
# The program will take care of those links above for you, so these notes are just in case you want to do something manually.
# 
# The 6th region is unused area containing text likely used for debugging the game, and has been tested to be safe for overwrites.
# Space:					0x1e8 					0x218 					0x110 					0x89c 					0x1b8 					0x1600			= 0x2564
v102CodeRegions = []
v101CodeRegions = []
v100CodeRegions = []
vPALCodeRegions = []


# The value below affects the Code Offset Converter in the Tools tab. If set to False, the search will be much slower, but 
# will also have a little better chance of finding a match.
quickSearch = True
