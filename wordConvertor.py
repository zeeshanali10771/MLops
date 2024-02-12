# In this code i will be writting the python code.


ones = (
   'Zero', 'One', 'Two', 'Three', 'Four',
   'Five', 'Six', 'Seven', 'Eight', 'Nine'
   )

twos = (
   'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
   )

tens = (
   'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
    'Seventy', 'Eighty', 'Ninety', 'Hundred'
   )

suffixes = (
   '', 'Thousand', 'Million', 'Billion'
   )

def fetch_words(number, index):
   if number == '0': return 'Zero'

   number = number.zfill(3)
   hundreds_digit = int(number[0])
   tens_digit = int(number[1])
   ones_digit = int(number[2])

   words = '' if number[0] == '0' else ones[hundreds_digit]

   if words != '':
       words += ' Hundred '

   if tens_digit > 1:
       words += tens[tens_digit - 2]
       words += ' '
       words += ones[ones_digit]
   elif(tens_digit == 1):
       words += twos[((tens_digit + ones_digit) % 10) - 1]
   elif(tens_digit == 0):
       words += ones[ones_digit]

   if(words.endswith('Zero')):
       words = words[:-len('Zero')]
   else:
       words += ' '

   if len(words) != 0:
       words += suffixes[index]

   return words
