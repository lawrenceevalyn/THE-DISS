# Reminder to self: the way R works is that you essentually run the code yourself,
# line by line, rather than following the python workflow of running whole "programs".
# Think of this as a place to keep scratch notes, rather than a program,
# and copy output from the console to long-term storage.

library(gender)

data = "ECCO-1789-sample.csv"

# gender_df(data, name_col = "Author", year_col = "Standardized Year",
#           method = c("napp"))


gender("madison", method = "demo", years = 1985)
