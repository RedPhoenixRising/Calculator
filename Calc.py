def perform_calculation(operand, int1 : int, int2 : int):
    if operand == "+":
        return int1 + int2
    elif operand == "-":
        return int1 - int2
    elif operand == "x":
        return int1 * int2
    elif operand == "/":
        return int1 / int2

running_total = 0
calc_dict = []

with open("/Users/redphoenix/Documents/Python/Python Fundamentals/FizzBuzz/replaceCalcs.txt",'r') as f:
    instructions = f.read().splitlines()
    i=0
    line_to_goto = 0
    num_inst = len(instructions)

    instr_dict = {}

    while i < num_inst:

        #Check if the statement has been seen before, if not store it
        instruction = instructions[line_to_goto]
        if instruction in instr_dict:
            print(line_to_goto + 1)
            print(instruction)
            print(i)
            exit()
        else:
            instr_dict[instruction] = instruction

        instruction_parts = instruction.split(" ")
        operation = instruction_parts[0]
        print(instruction_parts)
        #now check for operation type

        if operation == 'remove':
            line_number = int(instruction_parts[1])
            index = line_number - 1
            str_val = instructions[index]
            if index < len(instructions):
                del instructions[index]
                print("Removed " + str_val)
        elif operation == 'replace':
            line_number_to_replace = int(instruction_parts[1])
            replacement_line = int(instruction_parts[2])
            index_line_number_to_replace = line_number_to_replace -1
            index_replacement_line = replacement_line - 1
            new_calc = instructions[index_replacement_line]
            instructions[index_line_number_to_replace] = new_calc
            print("Replacing ", instructions[index_line_number_to_replace], " with ", new_calc)
        elif operation == 'goto':
            if len(instruction_parts) == 2:
                line_to_goto = int(instruction_parts[1])
                line_to_goto -= 1
            elif len(instruction_parts) == 5:
                line_to_goto = int(perform_calculation(instruction_parts[2], int(instruction_parts[3]), int(instruction_parts[4])))
                line_to_goto -= 1
        
        i+=1





