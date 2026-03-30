# I've tested upper() and replace(,) functions and made an example.
text = " python is fun "
#Avoiding spaces by slicing
text = text[1:14]
text = text.upper()
#Replacement
text = text.replace("FUN", "awesome")
print(text)