#####################################################
# Author: J. Davidson                               #
# Purpose: Reorganize featurec class fields based on#
#           user specified order.                   #
# Created: Sept. 6, 2016                            #
# Updates required:                                 #
#   - Currently only works for Feature classes.     #
#   - Currently the user must specify all fields for#
#       code not to spring an error (no effect on   #
#       output).                                    #
#   - Would be better if fields were rearranged in  #
#       an excel file rather than on screen (could  #
#       copy and paste rather than type numbers).   #
# Updated:                                          #
# Updater:                                          #
# Purpose:                                          #
#####################################################

import arcpy
from arcpy import env
import os
import string
import csv

# Define the tool for adding fields.
def addField(pathway1, gdb1):
    '''
    Set the workspace to the pathway the user entered.
    Ask the user how many fields they would like to add.
    For each field the user will be adding:
        ask the user for the field name.
        ask the user for the field alias.
        ask the user for the field type.
        If the field type is text:
            run the Add Field module for text fields
        Otherwise:
            run the Add Field module for nontext fields.
    '''
    arcpy.env.workspace = pathway1
    
    noFields = raw_input("How many fields would you like to add? ")
    for field in range(int(noFields)):
        fieldName = raw_input("Please enter the name of the field: ")
        fieldAlias = raw_input("Please enter the Alias for the field: ")
        fieldType = raw_input("Please entere the field type: ")
        if fieldType.upper() == 'TEXT':
            fieldLength = raw_input("Please enter the field length: ")
            arcpy.AddField_management(gdb1,
                                      fieldName,
                                      fieldType.upper(),
                                      "",
                                      "",
                                      fieldLength,
                                      fieldAlias)
        else:
            arcpy.AddField_management(gdb1,
                                      fieldName,
                                      fieldType.upper(),
                                      "",
                                      "",
                                      "",
                                      fieldAlias)

# Define the rearrange fields tool.
def rearrangeFields(pathway1, gdb1, newFC):
    '''
    Set the workspace to the pathway the user entered.
    Create a list of all the existing fields.
    
    Create empty lists to hold the fields of interest.
    '''
    arcpy.env.workspace = pathway1
    existingFields = arcpy.ListFields(gdb1)
    
    fieldList = []      # List of field names.
    fieldTypes = []     # List of field types.
    fieldLengths = []   # List of field lengths.
    fieldAlias = []     # List of field aliases.
    fieldCount = 0          # Number of fields.
    finalFieldList = []     # List of ordered fields.
    finalFieldType = []     # List of ordered field types.
    finalFieldLength = []   # List of ordered field lengths.
    finalFieldAlias = []    # List of ordered field aliases.
    '''
    For each existing field:
        increment the field count by 1.
        append the field properties to the corresponding field lists.
        print a list of the fields
    '''
    for field in existingFields:
        fieldCount = fieldCount+1           # Increment the count by 1.
        fieldList.append(field.name)        # Add field name to list.
        fieldAlias.append(field.aliasName)  # Add field alias to list.
        fieldLengths.append(field.length)   # Add field length to list.
        fieldTypes.append(field.type)       # Add field type to list.
        print str(fieldCount) + ". " + field.name     # Print the count beside the field name.
    '''
    Ask the user to name the csv file output.
    Write the output lists to a csv file.
    Ask the user to reorder the lists and then press enter to continue.
    '''
    book1 = raw_input("What would you like to name the temporary csv file used to reorder the lists? ")
    if book1[-4:] != '.csv':
        book1 += '.csv'
    with open(book1, 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        counter = 0
        for field in range(fieldCount):
            result = [str(fieldList[counter]), str(fieldAlias[counter]), str(fieldLengths[counter]), str(fieldTypes[counter])]
            writer.writerow(result)
            counter = counter + 1
    print '''Complete the steps below before continuing:
    1) Go to the csv file and copy and paste the rows until they are in the order you would like.
        Note: The csv file is saved in the same folder as this script.
    2) Once the fields are in the order you want, save and close the csv file.
    3) Press ENTER to continue'''
    raw_input("Press ENTER to continue")

    with open(book1, 'rb') as csvfile2:
        reader = csv.reader(csvfile2, dialect='excel')
        
        for row in reader:
            count2 = 0
            print row
            count2 = count2 + 1
            finalFieldList.append(row[0])
            finalFieldAlias.append(row[1])
            finalFieldLength.append(row[2])
            finalFieldType.append(row[3])
                
            
##    '''
##    Ask the user for the desired field order.
##    Separate the fields by commas.
##    '''
##    print "Please enter the order you want the fields to be displayed using the field's numbers seperated by commas (no spaces)."
##    print "\te.g. 1,3,2,5,4"
##    stringFieldOrder = raw_input("")
##    entry = stringFieldOrder.split(",")
##    '''
##    For each value in the ordered fields:
##        Append the appropriate data to each list.
##    '''
##    for value in entry:
##        finalFieldList.append(fieldList[int(value)-1])
##        finalFieldType.append(fieldTypes[int(value)-1])
##        finalFieldLength.append(fieldLengths[int(value)-1])
##        finalFieldAlias.append(fieldAlias[int(value)-1])
    '''
    Ask the user to enter the name of the output class.
    Get the shapetype of the input feature class.
    Create the new feature class.
    '''
    
    desc = arcpy.Describe(gdb1)
    shapetype = desc.shapeType
    spatial = str(desc.hasSpatialIndex)
    arcpy.CreateFeatureclass_management(pathway1, newFC, "POINT")
    '''
    Add the fields to the new feature class
    '''
    for number in range(2,fieldCount):
        if number != 1 and number != 2:
            arcpy.AddField_management(newFC,
                                      finalFieldList[number-1],
                                      finalFieldType[number-1],
                                      "",
                                      "",
                                      finalFieldLength[number-1],
                                      finalFieldAlias[number-1])
            print "Added field " + str(finalFieldList[number-1]) + " to " + newFC + "."
    print 'Finished adding fields.'

def appendData(pathway1, gdb1, newFC):
    arcpy.Append_management(gdb1, newFC, 'NO_TEST')

if __name__ == '__main__':
    '''
    Ask the user for the path to the File GDB.
    Ask the user for the name of the feature class or table.
    Ask the user if they would like to add fields to the feature class
    Ask the user if they would like to rearrange the fields in the feature class.
    If the user would like to add fields:
        run the tool to add fields.
    If the user would like to rearrange fields:
        run the tool to rearrange fields.
    '''
    pathway1 = raw_input("Please enter the path to the database holding the table with rows to be reordered: ")
    gdb1 = raw_input("Please enter the name of the feature class you would like to edit: ")
    addField1 = raw_input("Will you be adding any fields to the feature class (Y/N)? ")
    if addField1.upper() == 'Y':
        addField(pathway1, gdb1)
    rearrangeFields1 = raw_input("Will you be rearranging fields in " + gdb1 + " (Y/N)? ")
    if rearrangeFields1.upper() == 'Y':
        newFC = raw_input("What would you like to name the output feature class with the new field arrangement? ")
        rearrangeFields(pathway1, gdb1, newFC)
        appendData1 = raw_input("Would you like to append the data from the input dataset to created dataset (Y/N)? ")
        if appendData1 == 'Y':
            appendData(pathway1, gdb1, newFC)
            print "The data has been appended to the new dataset."
        else:
            print "No data was appended to the new dataset."
    print "The program has FINISHED (yay!)"
    print "Please note, this version of the program does not add domains to the fields in the created dataset."
    print "You must add the domains to each field manually (if applicable)."
    
