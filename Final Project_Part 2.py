# A program to visualize translated amino acid sequence from DNA sequence
# of human FAT3 gene
# Authors: Minh Huyen Nguyen 
# Date: 04/23/2017

import turtle

width = 1200
cols = width //6
height = 600
rows = height // 100

def bar(tortoise, index, rf):
    '''
    Draw a colored bar over codon starting at position index in
    reading frame rf.  Put the turtle's tail up and down to
    handle line breaks properly

    Parameters:
    tortoise: a Python turtle
    index: the index of the codon
    rf: number of reading frame

    Return value: None
    
    '''
    tortoise.up()
    tortoise.goto(index % cols, index // cols + (rf + 1) / 5)
    tortoise.down()
    tortoise.forward(1)
    tortoise.up()
    tortoise.goto((index + 1) % cols, (index + 1) // cols + (rf + 1) / 5)
    tortoise.down()
    tortoise.forward(1)
    tortoise.up()
    tortoise.goto((index + 2) % cols, (index + 2) // cols + (rf + 1) / 5)
    tortoise.down()
    tortoise.forward(1)

def AA_drawing(dna, rf, tortoise):
    '''
    A function to translate DNA sequence to amino acid sequence in reading
    frame rf = 0,1,2 (forward only)

    Parameters:
    dna = DNA sequence
    rf = number of reading frame
    tortoise = a Python turtle

    Return value: None
    
    '''
    non_polar = ['GCT','GCC', 'GCA', 'GCG','TTA','TTG', 'CTT', 'CTC', 'CTA', 'CTG', 'GTT', 'GTC','GTA', 'GTG'
                 'CCT','CCC','CCA','CCG','ATT','ATC','ATA', 'TTT','TTC', 'TGG', 'ATG']
    polar = ['GGT','GGC','GGA','GGG','TCT','TCC','TCA','TCG','AGT','AGC',
             'ACT','ACC', 'ACA','ACG', 'TGT', 'TAT', 'AAT','AAC', 'CAA','CAG']
    acidic = ['GAT','GAC','GAA', 'GAG']
    basic = ['AAA','AAG', 'CAT','CAC',  'CGT', 'CGC', 'CGA', 'CGG'] 
    start_pos = 0
    end_pos = 0
    for i in range (rf, len(dna)-2, 3):
        tortoise.pencolor('red')
        bar(tortoise, i, rf)
    for i in range (rf, len(dna)-2, 3):
        codon = dna[i:i+3]
        if codon in polar:
            start_pos = i
            tortoise.pencolor('blue')
            bar(tortoise, start_pos, rf)
        if codon in acidic:
            start_pos = i
            tortoise.pencolor('yellow')
            bar(tortoise, start_pos, rf)
        if codon in basic:
            start_pos = i
            tortoise.pencolor('purple')
            bar(tortoise, start_pos, rf)
        elif codon == 'TAA'or codon == 'TGA' or codon == 'TAG':
            end_pos = i+2
            tortoise.pencolor('black')
            bar(tortoise, end_pos, rf)
        else:
            bar(tortoise, i, rf)

def viewer_aa(dna):
    '''
    A dunction displays sequence of amino acid in 3 forward reading frames.

    Parameters:
    dna = DNA sequence

    Return value: None
    
    '''
    tortoise = turtle.Turtle()
    screen = tortoise.getscreen()
    screen.setup(width, height)
    screen.setworldcoordinates(0, 0, cols, rows) 
    screen.tracer(100)
    tortoise.hideturtle()
    tortoise.speed(0)
    tortoise.up()
	
	# Draw amino acid string in window.
    for index in range(len(dna)):
        tortoise.goto(index % cols, index // cols)
        tortoise.write(dna[index])
		
	# Find ORFs in forward reading frames 0, 1, 2.
	
    tortoise.width(5)
    for index in range(3):
        AA_drawing(dna, index, tortoise)

    screen.update()
    screen.exitonclick()
			
def main():
    # Read DNA from a file and draw amino acid sequence
    inputFile = open('DNA_FAT3.txt', 'r')
    dna = inputFile.read()
    viewer_aa(dna)

main()
