# Reference notes for working with RStudio


To change the working directory in RStudio, select main menu Session >> Set Working Directory >>

After your working directory is set, you can import data from .csv, .txt, etc. One basic command for importing data into R is read.csv()

''' sand <- read.csv("sand_example.csv")

To export data from R, use the command write.csv() function. Since we have already set our working directory, R automatically saves our file into the working directory.

''' write.csv(sand, file = "sand_example2.csv")


Function	Description
read.csv()	imports csv data
write.csv()	exports csv data
print()		prints the entire object (avoid with large tables)
head()		prints the first 6 lines of your data
str()		shows the data structure of an R object
names()		lists the column names (i.e., headers) of your data
ls()		lists all the R objects in your workspace directory


## packages
To use a package, you must first install it and then load it. These steps can be done at the command line or using the Packages Tab.




### Helpful links
* http://ncss-tech.github.io/stats_for_soil_survey/chapters/1_introduction/1_introduction.html#4_rstudio:_an_integrated_development_environment_(ide)_for_r