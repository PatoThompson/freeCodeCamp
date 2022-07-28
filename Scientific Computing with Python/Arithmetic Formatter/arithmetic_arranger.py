def arithmetic_arranger(problems,results=None):

    # First, we check if there are too many problems. The limit is five.
    arranged_problems = ''
    number_of_problems = int(len(problems))
    if number_of_problems > 5:
        msg = 'Error: Too many problems.'
        return msg
    
    # Then we split each problem into it's constituent parts and check for errors: only addition and substraction allowed and each operand should have a max of four digits in width.
    operand1 = []
    operator = []
    operand2 = []
    for item in problems:
        parts = item.split()
        if len(parts[0]) > 4:
            msg = 'Error: Numbers cannot be more than four digits.'
            return msg
        if len(parts[2]) > 4:
            msg = 'Error: Numbers cannot be more than four digits.'
            return msg
        if parts[1] != '+' and parts[1] != '-':
            msg = "Error: Operator must be '+' or '-'."
            return msg
        operand1.append(parts[0])
        operator.append(parts[1])
        operand2.append(parts[2])
    
    # After that, we format the strings
    first_row_list = []
    second_row_list = []
    dashes_row_list = []

    for i in range(number_of_problems):
        if len(operand1[i]) > len(operand2[i]):
            formatted_operand1 = '  ' + operand1[i]
            first_row_list.append(formatted_operand1)
            filler = len(formatted_operand1) - len(operand2[i]) - 1 # -1 is the operator
            formatted_operand2 = operator[i] + ' '*filler + operand2[i]
            second_row_list.append(formatted_operand2)
        if len(operand1[i]) < len(operand2[i]):
            formatted_operand2 = operator[i] + ' ' + operand2[i]
            second_row_list.append(formatted_operand2)
            filler = len(formatted_operand2) - len(operand1[i])
            formatted_operand1 = ' '*filler + operand1[i]
            first_row_list.append(formatted_operand1)
        if len(operand1[i]) == len(operand2[i]):
            formatted_operand1 = '  ' + operand1[i]
            first_row_list.append(formatted_operand1)
            formatted_operand2 = operator[i] + ' ' + operand2[i]
            second_row_list.append(formatted_operand2)
        dashes = '-'*len(formatted_operand2)
        dashes_row_list.append(dashes)

    # And we calculate the results and check for errors
    results_list = []
    results_row_list = []
    for i in range(number_of_problems):
        try:    
            if operator[i] == '+':
                x = int(operand1[i]) + int(operand2[i])
                results_list.append(str(x))
            if operator[i] == '-':
                x = int(operand1[i]) - int(operand2[i])
                results_list.append(str(x))
        except:
            msg = 'Error: Numbers must only contain digits.'
            return msg
        filler = len(dashes_row_list[i]) - len(results_list[i])
        formatted_result = ' '*filler + str(results_list[i])
        results_row_list.append(formatted_result)
    
    # Finally, we assemble everything

    spaces = '    '
    first_row = spaces.join(first_row_list) + '\n'
    second_row = spaces.join(second_row_list) + '\n'
    dashes_row = spaces.join(dashes_row_list)
    results_row = '\n' + spaces.join(results_row_list)

    arranged_problems = first_row + second_row + dashes_row

    # And if asked for results we proceed to add them to the final string
    if results == True:
        arranged_problems = first_row + second_row + dashes_row + results_row

    return arranged_problems