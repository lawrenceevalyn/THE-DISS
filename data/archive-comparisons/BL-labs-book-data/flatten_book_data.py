# NB this will flatten the data. Some fields (author, pdf, imgs) have extra data that will be lost if you include them in this data.
# the "author" field has a variety of nuances that will be lost for example (creator, editor, etc)
# Intended for use with https://dx.doi.org/10.21250/DB21
# MIT Licence 2016 

import json, csv

EXPORTFILENAME = "flattened_book_data.csv"

FIELDS = ['datefield', 'shelfmarks', 'title', 'publisher', 'edition', 'flickr_url_to_book_images', 'place', 'issuance',
          'authors', 'identifier', 'corporate', 'date',
          #'imgs', 'pdf', 
         ]

def flatten(item):
  try:
    for i in item.itervalues():
      for value in flatten(i):       
        yield value
  except AttributeError as e:
    # what was passed is not a dict
    for value in item:
      yield value
      
with open("book_data.json", "r") as bkd:
  doc = json.load(bkd)
  with open(EXPORTFILENAME, "w") as exfh:
    outdoc = csv.DictWriter(exfh, fieldnames = FIELDS)
    outdoc.writerow({x:x for x in FIELDS})
    for idx,row in enumerate(doc):
      line_of_data = {}
      for f in FIELDS:
        if isinstance(row[f], str):
          line_of_data[f] = row[f].encode("utf-8")
        elif isinstance(row[f], list):
          line_of_data[f] = u",".join(x for x in row[f]).encode("utf-8")
        else:
          line_of_data[f] = u",".join(flatten(row[f])).encode("utf-8")
          
      outdoc.writerow(line_of_data)
      if not (idx + 1) % 1000:
        print("Processing row {0}".format(idx+1))