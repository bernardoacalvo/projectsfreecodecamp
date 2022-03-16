#Author: Bernardo Calvo

MAX_PROBLEMS = 5
MAX_DIGITS = 4
OPERATOR_SPACE = 2

ERROR_MANY_PROB = "Error: Too many problems."
ERROR_OPERATOR = "Error: Operator must be '+' or '-'."
ERROR_NUM_DIGITS = "Error: Numbers must only contain digits."
ERROR_MORE_DIGITS = "Error: Numbers cannot be more than four digits."

PROBLEMS_SEPARATOR = "    "

def arithmetic_arranger(problems, showRes=False):
  if len(problems) > MAX_PROBLEMS:
    return ERROR_MANY_PROB

  formats = list()  # [[num1, operator, num2], [num1, operator, num2], ...]

  for str in problems:
    [num1, operator, num2] = str.split();

    #errors
    if operator != '+' and operator != '-':
      return ERROR_OPERATOR
    if not num1.isdigit() or not num2.isdigit():
      return ERROR_NUM_DIGITS
    if len(num1) > MAX_DIGITS or len(num2) > MAX_DIGITS :
      return ERROR_MORE_DIGITS  

    formats.append(format(num1, operator, num2, showRes))

  
  formatLines = list()  # [[line1], [line2], ...]   line1 = [num1, num1, ...]

  numOfLines = len(formats[0])
  for i in range(numOfLines):
    auxList = list()
    for p in formats:
      auxList.append(p[i])
    formatLines.append(auxList)

  txt = ''
  i = 0
  for line in formatLines:
    txt += PROBLEMS_SEPARATOR.join(line)
    if i < numOfLines-1:
      txt += '\n' 
      i += 1

  return txt

def format(num1, operator, num2, showRes):
  maxLen = max(len(num1), len(num2))+OPERATOR_SPACE
  res = [num1.rjust(maxLen), operator + ' ' + num2.rjust(maxLen-OPERATOR_SPACE), "".rjust(maxLen, '-')]
  if showRes:
    num1 = int(num1)
    num2 = int(num2)
    res.append(str((num1+num2) if operator == '+' else (num1-num2)).rjust(maxLen))
  return res

print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True))  #example
