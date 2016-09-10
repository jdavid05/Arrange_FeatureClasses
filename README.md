# Arrange_FeatureClasses
Python 2.7.3 script to rearrange fields in a File Geodatabase

Field Organizer V. 0.2 (Last update: Sep. 7, 2016)

Author: J. Davidson
Purpose: This Python script is used to change the order of fields in an Esri ArcGIS Desktop 10.x feature class. Currently, because I made this in a couple of hours while at work, the program only supports feature classes. However, it would be easy to alter to make it support tables as well. Also, the program saves the output as a different file to ensure original data is not damaged, but, this also could be changed to suit needs.
In a nutshell, the program outputs a CSV file with all of the fields in the feature class, you can then reorganize the fields and rearrange them to suit your needs in the CSV. Once they have been reorganized, you can finish the program and a new feature class template will be created with the new field order. You can optionally append the data from the old FC to the new FC, just type 'Y' when prompted.
This program does not yet have error checking.

Instructions:

	1) Run the program by double clicking it.

	2) When prompted, enter the path to the database including the database folder name.
		e.g. C:\SampleFolder\SampleDatabase.gdb    --  please ensure you use '\' (backslashes) seperators NOT '/' (forward slashes).

	3) When prompted, enter the name of the feature class.

	4) When prompted if you would like to add fields, enter 'Y' if you would like to add fields or 'N' if you would not.
		If you are adding fields:
		(i  ) When prompted, enter the number of fields you would like to add.
		(ii ) When prompted, enter the name of the field (no spaces or special characters)
		(iii) When prompted, enter the alias of the field (spaces are allowed, but, no special characters)
		(iv ) When prompted, enter the field type ("TEXT', 'FLOAT', DOUBLE', 'SHORT', 'LONG', or 'DATE' are supported)
		(v  ) If the field type is TEXT, you will be prompted for field length, otherwise, you are finished.
		(vi ) Complete the same steps for each field you will be making.

	5) When prompted, if you would like to rearrange any fields enter 'Y', otherwise enter 'N'.
		if you are rearranging fields:
		(i  ) When prompted, enter a name for the output feature class (no spaces or special characters)
		(ii ) When prompted, enter a name for the csv file you will be using to rearrange the fields.
		(iii) Locate the csv file (it is saved in the folder from which you ran the script) and open it with excel.
		(vi ) Cut and insert fields as neccessary
			NOTE: Do not add or delete fields at this stage.
			NOTE: If appending data later, do not change field names at this stage.
		(v  ) Save and close the csv file and press enter in the command prompt from which the script is running.
	
	6) Wait while the fields are added to the feature class.

	7) When prompted, enter 'Y' if you would like to append the data from the input dataset to the output dataset or 'N' if you would not.

	8) The program has finished!

Current Version 0.2 (Sept 7, 2016):

	Added the ability to append data when a new feature class is created.
	
	Added excel functionality to make it easier\faster to rearrange fields.

Previous versions:

	version 0.1 (Sept 6, 2016):

		Able to create fields
	
		Able to rearrange fields (through entering the numbers corresponding to each field on the screen) (time-consuming).

