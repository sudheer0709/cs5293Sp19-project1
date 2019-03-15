CS5293Sp19-project1:

This project is about to redact the sensitive information present in a text based on the given flags and concepts. As part of this project, we are asked to redact the names, addresses,
genders,dates,phone numbers and concepts.

redact_names():
In this function , names present in a text are redacted. TO do so, I have used spacy package to redact by taking entity.labels_  attribute as 'PERSON'.After finding the names in text,then
it is replaced by a character █ with the length of the name.

redact_gender():
In this function, genders are redacted which are present in the given test. A list of genders are predefined with various values such as 'MEN','WOMEN','HE','SHE' etc and then compared by 
entity.label_ attribute 'GENDER' and then replaced with a character █ with the length of the gender.

redact_phone():
In this function, phone numbers are redacted by using a regular expression for various possibilities of phone numbers and then replaced with a character █ with the length of the number.

redact_addresses():
In this function, addresses are redacted by using spacy package with 'FAC' attribute. This function redacts all kinds of addresses such as street, city, state, country etc and then 
replaced with the given character.

redact_dates():
In this function,dates are redacted by using spacy package with 'DATE' attribute and then replaced by the given character.

redact_concept():
In this function, a package called thesaurus is being used to find the synonyms of a given word. Based on the given concept word, all the synonyms in the text are identified and then redact
ed with the given character. I have used concept as 'prominent' and it redacts similar word in my text file such asoutstanding ,salient. 

output():
a new file is created with 'filename'redacted.txt and stored the entire redacted data in this file.

stats():
stats function is created to log the information regarding all the redacting functions and stored in a text file. In this file,redacted words,redacted word length and type of redacted word
are stored in a list and then put in dataframe then converted into a text file.


sysargv,glob is used to store all the text files in a list and then by parsing each text in the list,all the above functions are applied on the test file to redact sensitive information.









# cs5293Sp19-project1
