#! /usr/bin/perl

###############################################################################
###############################################################################
#
# To find words from a dictionary in a wordsearch puzzle
#
#	by Andrew Hardwick, http://duramecho.com
#    Released under GPL.
#
###############################################################################
###############################################################################
# Version 1, 2005/1/16
# Version 2, 2005/1/17
#  Removed words with spaces remover (specific to particular first puzzle).
#  Removed CCing to STDOUT.
#  Renamed output files.
# Version 3, 2016/7/18
#  Corrected #! line.
###############################################################################
###############################################################################
# How To Use:
#  Put the wordsearch grid in a plain text file called Wordsearch.txt.
#   No spaces between letters in a row.
#   Rows separated by linebreaks. No blank lines between rows.
#  Put the list of legitimate words in a file called Dictionary.txt separated
#   by linebreaks. It is not necessary for the words to be in alphabetical
#   order & unique but if they are then it will run slightly quicker.
#  Ensure the line breaks in those text files are in the local operating
#   system's format.
#  Run the program.
#   All found words in the grid will be put in a file called Strings.txt.
#   All found words in the grid that were in the dictionary will also be put in
#    a file called Words.txt.
#  Warning: it overwrites the files Strings.txt & Words.txt.
###############################################################################
###############################################################################

# Include libraries
use Cwd;		# To find current directory
use strict;		# Disenable automatic variables

###############################################################################
# Main rountine
###############################################################################

{	# Get the grid from the file
	open(WordsearchFile,'<Wordsearch.txt')or
			die("Cannot open Wordsearch.txt to read.\n");
	my(@Grid);
	while(<WordsearchFile>)
	{	chomp;
		push(@Grid,[split('')]);}
	close(WordsearchFile);
	
	# Get dimensions
	my $YSize=scalar(@Grid);
	unless($YSize)
	{	die("Empty grid.\n");}
	my $XSize=scalar(@{$Grid[0]});
	foreach (@Grid)
	{	unless(scalar(@$_)==$XSize)
		{	die("Grid not rectangular.\n");}}
	
	# Get all possible words
	my($XStart,$YStart,$X,$Y,$D,$XD,$YD,$Word,@Words,%Locations);
	# Iterate over all starting letters & all directions
	for($XStart=0;$XStart<$XSize;$XStart++)
	{	for($YStart=0;$YStart<$YSize;$YStart++)
		{	for($D=0;$D<9;$D++)
			{	# Create the direction vector
				$XD=int($D/3)-1;
				$YD=$D%3-1;
				unless($XD||$YD)
				{	next;}
				# Extract words of all lengths
				$X=$XStart;
				$Y=$YStart;
				$Word='';
				while($X<$XSize&&$X>=0&&$Y<$YSize&&$Y>=0)
				{	$Word.=lc($Grid[$Y][$X]);
					push(@Words,$Word);
					if(length($Word)>1)
					{	$Locations{$Word}.=
								'('.($XStart+1).','.($YStart+1).','.
								('U','','D')[$YD+1].
								('L','','R')[$XD+1].')';}
					else
					{	if($D==0)	# Only record once as directionless
						{	$Locations{$Word}.=
									'('.($XStart+1).','.($YStart+1).')';}}
					$X+=$XD;
					$Y+=$YD;}}}}
	print scalar(@Words)," letter lines found.\n";

	# Sort the words & remove duplicates
	@Words=sort(@Words);
	my $c;
	for($c=0;$c<scalar(@Words);$c++)
	{	if($c&&$Words[$c]eq$Words[$c-1])
		{	splice(@Words,$c--,1);}}
	print scalar(@Words)," unique strings found (Strings.txt).\n";

	# Output all found words to a file
	open(StringsFile,'>Strings.txt')or
			die("Cannot open Strings.txt to write.\n");
	foreach $Word (@Words)
	{	print StringsFile "$Word $Locations{$Word}\n";}
	close(StringsFile);

	# Get list of legitimate words (NB this is not a memory efficient method)
	open(DictionaryFile,'<Dictionary.txt')or
			die("Cannot open Dictionary.txt to read.\n");
	my @Dictionary;
	while(<DictionaryFile>)
	{	chomp;
		push(@Dictionary,lc($_));}
	close(DictionaryFile);
	@Dictionary=sort(@Dictionary);

	# Make a sub list of all the recognised words
	my @WordsRecognised;
	my $PosDictionary=0;
	my $PosWords=0;
	while($PosWords<scalar(@Words)&&$PosDictionary<scalar(@Dictionary))
	{	if($Words[$PosWords]gt$Dictionary[$PosDictionary])
		{	$PosDictionary++;}
		elsif($Words[$PosWords]lt$Dictionary[$PosDictionary])
		{	$PosWords++;}
		else
		{	# Yippie! Found one
			push(@WordsRecognised,$Words[$PosWords]);
			$PosWords++;
			$PosDictionary++;}}
	print scalar(@WordsRecognised)," unique words found (Words.txt).\n";

	# Output all recognised found words to a file
	open(WordsFile,'>Words.txt')or
			die("Cannot open Words.txt to write.\n");
	foreach $Word (@WordsRecognised)
	{	print WordsFile "$Word $Locations{$Word}\n";}
	close(WordsFile);}
	
###############################################################################
