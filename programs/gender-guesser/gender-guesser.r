# Reminder to self: the way R works is that you essentually run the code yourself,
# line by line, rather than following the python workflow of running whole "programs".
# Think of this as a place to keep scratch notes, rather than a program,
# and copy output from the console to long-term storage.

library(gender) # re-run these every time to get everything necessary installed
install_genderdata_package()
devtools::install_github("ropensci/genderdata")

names = c("john", "madison")

ECCOnames = c("Charles", "Society", "William", "René-Louis", "James", "John", "Edward", "Philip", "Hainault", "Junius", "Septimus", "Herodian", "John", "Benjamin", "Samuel", "Whitwell", "William", "Augustus", "Francis", "William", "Olaudah", "Candid", "John", "Charles", "William", "John", "Great", "Andrew", "Charles", "John", "Society", "John", "Western", "Elhanan", "John", "William", "Joshua", "Ann", "Charlotte")

gender(ECCOnames, method = "napp", years = 1789)
# if this makes an empty tibble, it's probably fine, but I'm asking for something it has no data for (probably because the date is too early)
# ipums can go as early as 1789
# napp can go as early as 1758, but doesn't know the name "John" until 1769

