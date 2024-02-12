# In this code i will be writting the python code.

def convert_to_words(number):
   length = len(str(number))
   if length > 12:
       return 'This program supports a maximum of 12 digit numbers.'

   count = length // 3 if length % 3 == 0 else length // 3 + 1
   copy = count
   words = []

   for i in range(length - 1, -1, -3):
       words.append(fetch_words(
           str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))

       count -= 1

   final_words = ''

   for s in reversed(words):
       final_words += (s + ' ')

   return final_words

if __name__ == '__main__':
   number = int(input('Enter any number: '))
   print('%d in words is: %s' %(number, convert_to_words(number)))
