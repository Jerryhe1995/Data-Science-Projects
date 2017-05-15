#CSV "Basic Data Sets" Due 02/13/2017 11:55 PM
#Kevin Gomes and Jie He
#Dr. Lutz Hamel
#CSC 392

###############################################################################
#                                 Program                                     #
###############################################################################
#This program gathers much info from CSV datasets.
#It gathers the min, max, average, and mode of data, as well as plots both the
#numerical and categorical data.

import pandas
import matplotlib.pyplot as plot
def main():
    print ('Please type in "done" without the quotes when you are finished.')
    path = input('Please enter the relative file path, including file name, of your data set(or specifically highway1.csv / breslow.csv): ')
    print ('')
    if str(path) != 'done':
        func(str(path))
        main()
    else:
        print ('I hope you found your data helpful! Have a nice day!')

def func(path):
    highway = pandas.read_csv(path)
    print ('There are ' +  str(highway.shape[0]) + ' rows in this data set.')
    print ('There are '+  str(highway.shape[1]) + ' columns in this data set.')

    numericalCount = 0 #How many numerical fields we have
    numFields = [] #What index are these fields at?
    catCount = 0 #How many categorical fields
    catFields = [] #What index are these fields at?
    j = 0 #For the index

    #Get all kinds of data, and store the indicies into our arrays.
    for i in highway.columns:
        if highway[i].dtype == 'float64' or highway[i].dtype == 'int64':
            numericalCount += 1
            numFields += [j]
        else:
            catCount += 1
            catFields += [j]
        j += 1

    columnNames = highway.columns.values.tolist() #Gives us all column names in a list

    counts = (numericalCount, catCount)
    print ('Of all fields, ' + str(counts[0]) + ' is/are numerical, ' + str(counts[1]) + ' is/are categorical.')
    if (counts[0] > 0) and counts[1] > 0: #Do we have both numerical and categorical
        print ('There is both numerical and categorical data in this dataset.')
    elif (counts[0] > 0): #Just numerical
        print ('There is only numerical data in this dataset')
    else: #Otherwise...
        print ('There is only categorical data in this dataset')

    #Find if there is an ID column at the beginning
    i = 0
    idFound = False
    while i < len(highway) and idFound == False:
        i += 1
        if i - highway.iloc[i - 1, 0] == 0:
            idFound = True
            print ('There is a useless ID column in this data set, the index is'+ str(i))

    #Compute mode of categorical columns
    print('\nThe mode of the categorical data is as follows:')
    if catCount > 0:
        for i in catFields:
            print (str (highway[columnNames[i]].mode()))
            print()
    print()

    #Compute min, max, and mean of numerical columns
    # if numericalCount > 0:
    #     for i in numFields:
    #         print ('Column: "' + str(columnNames[i]) + '" Minimum value: ' + str(highway[columnNames[i]].min()))
    #         print ('Column: "' + str(columnNames[i]) + '" Maximum value: ' + str(highway[columnNames[i]].max()))
    #         print ('Column: "' + str(columnNames[i]) + '" Mean |average: ' + str(highway[columnNames[i]].mean()))
    #         print('')
    #NOTE: The alternative to these 2 loops is highway.describe(), but I like to set it up my way.
    print (highway.describe())
    #Plot our histogram of numerical data
    highway.hist()
    plot.show()

    #Now our barchart of categorical data
    for i in catFields:
        cat = highway[columnNames[i]].astype('category')
        cat.value_counts().plot(kind = 'bar')
        plot.show()

main()
