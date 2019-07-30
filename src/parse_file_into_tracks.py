#!/usr/bin/python3
# 
#   A. Gnias
#   Created: 5/22/2019
#
#   general_functions.py - Functions supporting use of the Spotify API
# 
#   Requirements: OAuth Token value for Spotify API
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.3
#   Vim 8.0 [tabstop=3]


from sys import path
path.append("../")
from src.Track import Track


def parse_playlist(fname, delimiter=',') :
	"""
	Generates a list containing items of the form [artist, song]
	Input: text file name in cwd
	Output: populated list
	"""
	el = list()
	with open(fname,'r') as f :
		for line in f :
			contents = line.strip().split(delimiter)
			el.append(Track(contents[1].strip(), contents[0].strip()))
	f.close()
	return el