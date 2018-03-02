# A program to analyzing data of bladder cancer in human
# Author: Minh Huyen Nguyen
# Date: 04/16/2017

import matplotlib.pyplot as pyplot
import numpy as np

def readData_gender(filename):
    '''
    The function reads the Clincal data of Bladder Cancer patients
    data file from cbioportal

    Parameter:
    filename = a name of file (in strings)

    Return value: number of male and female patients
 
    '''
    bladder_cancer = open(filename, 'r', encoding = 'utf-8')
    line = bladder_cancer.readline()
    while line[0] == ('#'):
        line = bladder_cancer.readline()
        
    female = 0
    male = 0

    for line in bladder_cancer:
        row = line.split(',')
        if row[6] != '[Not Available]' and row[6] == 'MALE':
            male = male +1
        if row[6] != '[Not Available]' and row[6] == 'FEMALE':
            female = female +1

    return male, female

def readData_stage(filename):
    '''
    The function reads the Clincal data of Bladder Cancer patients
    data file from cbioportal
    
    Parameter:
    filename = a name of file (in strings)

    Return value: frequency of each cancer stage
 
    '''
    bladder_cancer = open(filename, 'r', encoding = 'utf-8')
    line = bladder_cancer.readline()
    while line[0] == ('#'):
        line = bladder_cancer.readline()

    stageI = 0
    stageII = 0
    stageIII = 0
    stageIV = 0

    for line in bladder_cancer:
        row = line.split(',')
        if row[57] != '[Not Available]' and row[57] == 'Stage I':
            stageI = stageI + 1
        if row[57] != '[Not Available]' and row[57] == 'Stage II':
            stageII = stageII + 1
        if row[57] != '[Not Available]' and row[57] == 'Stage III':
            stageIII = stageIII + 1
        if row[57] != '[Not Available]' and row[57] == 'Stage IV':
            stageIV = stageIV + 1
 
    return stageI, stageII, stageIII, stageIV

def readData_Minnesota(filename2):
    '''
    The function reads the bladder cancer data in the population of Minnesota
    from 1988-2013
    
    Parameter:
    filename = a name of file (in strings)

    Return value: list of incidence rate in male and female population with
    list of recorded year
    '''
    
    bladder_minnesota = open(filename2, 'r', encoding = 'utf-8')
    line = bladder_minnesota.readline()
    while line[0] == ('#'):
        line = bladder_minnesota.readline()

    year = []
    incidence_rate_male = []
    incidence_rate_female = []

    for line in bladder_minnesota:
        row = line.split(',')
        if row[2] == 'Male':
            year.append(int(row[0]))
            incidence_rate_male.append(float(row[6]))
        if row[2] == 'Female':
            incidence_rate_female.append(float(row[6]))

    return year, incidence_rate_male, incidence_rate_female


def readData_Minnesota2(filename2):
    '''
    The function reads the bladder cancer data in the population of Minnesota
    from 1988-2013
    
    Parameter:
    filename = a name of file (in strings)

    Return value: list of number of new cancers and total population in
    Minnesota 
 
    '''
    bladder_minnesota = open(filename2, 'r', encoding = 'utf-8')
    line = bladder_minnesota.readline()
    while line[0] == ('#'):
        line = bladder_minnesota.readline()

    new_cancer = []
    population = []

    for line in bladder_minnesota:
        row = line.split(',')
        if row[2] == 'Both combined':
            new_cancer.append(int(row[4]))
            population.append(int(row[5]))

    return new_cancer, population

def drawHist_gender(male, female):
    '''
    A function to plot the histogram of bladder cancer by gender

    Parameters:
    male: number of male patients
    female: number of female patients

    Return value: None

    '''
    count = []
    count.append(male)
    count.append(female)
    
    status = ['Male', 'Female']
    pos = np.arange(len(status))
    width = 0.5

    ax = pyplot.axes()
    ax.set_xticks(pos + (width/2))
    ax.set_xticklabels(status)

    pyplot.bar(pos, count, width, color = 'blue')
    pyplot.xlim([min(pos) - 0.5, max(pos) + 1.0])
    pyplot.title('Frequency of diagnosed patients by gender')
    pyplot.show()

male, female = readData_gender('data_bcr_clinical_data_patient.csv')

def drawHist_stage(stageI, stageII, stageIII, stageIV):
    '''
    A function to plot the frequency of cancer stages among patients

    Parameters:
    stageI: number of patients in stage I
    stageII: number of patients in stage II
    stageIII: number of patients in stage III
    stageIV: number of patients in stage IV

    Return value: None

    '''
    
    count_stage = []
    count_stage.append(stageI)
    count_stage.append(stageII)
    count_stage.append(stageIII)
    count_stage.append(stageIV)
    
    status = ['Stage I', 'Stage II', 'Stage III', 'Stage IV']
    pos = np.arange(len(status))
    width = 0.5

    ax = pyplot.axes()
    ax.set_xticks(pos + (width/2))
    ax.set_xticklabels(status)
    
    pyplot.bar(pos, count_stage, width, color = 'blue')
    pyplot.xlim([min(pos) - 0.5, max(pos) + 1.0])
    pyplot.title('Frequency of cancer stages among diagnosed patients')
    pyplot.show()

stageI, stageII, stageIII, stageIV = readData_stage('data_bcr_clinical_data_patient.csv')

def draw_minnesota(year, incidence_rate_male, incidence_rate_female):
    '''
    A function to plot incidence rate of bladder cancer by gender in Minnesota

    Parameters:
    year: list of recorded year
    incidence_rate_male: list of incidence rate in male population
    incidence_rate_female: list of incidence rate in female population

    Return value: None

    '''
    
    pyplot.plot(year, incidence_rate_male, label = 'Male')
    pyplot.plot(year, incidence_rate_female, label = 'Female')
    pyplot.legend(loc = 'center')
    pyplot.title('Incidence rate of bladder cancer in Minnesota from 1988-2013')
    pyplot.xlabel('Year')
    pyplot.ylabel('Incidence Rate (per 100,000)')
    pyplot.show()


year, incidence_rate_male, incidence_rate_female = readData_Minnesota('Bladder - Minnesota.csv')

def linearRegression(x,y):
    '''
    The function computes the slope and y-intercept of the least squares
    requession line.

    Parameters:
    x = a list of x coordinates
    y = a list of y coordinates

    Return value:
    The slope and y-intercept of a linear regression.

    '''
    n = len(x) # number of points
    sumx = 0 # sum of x coordinates
    sumy = 0
    sumxy = 0
    sumx_square = 0
    
    for index in range(n):
        sumx = sumx + x[index]
        sumy = sumy + y[index]
        sumxy = sumxy + (x[index]*y[index])
        sumx_square = sumx_square + (x[index]**2)

    m = (n*sumxy - sumx*sumy)/(n*sumx_square - (sumx)**2)
    b = (sumy - m*sumx)/n

    return m, b

def draw_minnesota2(new_cancer, population):
    '''
    The function to plot a linear correlation between number of new cancer and
    the total population in Minnesota from 1988-2013

    Parameters:
    new_cancer: number of new cancer over year
    population: number of total population over year

    Return value: None

    '''
    pyplot.scatter(new_cancer, population)
    m, b = linearRegression(new_cancer, population)
    minX = min(new_cancer)
    maxX = max(new_cancer)
    pyplot.plot([minX, maxX], [m * minX + b, m * maxX + b], color = 'red')   
    pyplot.xlabel('Number of new cancer')
    pyplot.ylabel('Population')
    pyplot.title('Number of new cancer vs Total population in Minnesota')
    pyplot.show()

new_cancer, population = readData_Minnesota2('Bladder - Minnesota.csv')

def main():
    drawHist_gender(male, female)
    drawHist_stage(stageI, stageII, stageIII, stageIV)
    draw_minnesota(year, incidence_rate_male, incidence_rate_female)
    draw_minnesota2(new_cancer, population)

main()
