# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor 
# Sample String : 'restart'
# Expected Result : 'resta$t'

def convert_str(stri):
	ch = stri[0]
	stri = stri.replace(ch, '$')
	stri = ch + stri[1:]

	return stri

stri = input("Enter your string:")
print(convert_str(stri))
