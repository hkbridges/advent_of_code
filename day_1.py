file_path = "input.txt"
zero_counter = []

def get_instructions():
    lines_list_stripped = []
    lines_list = []
    with open(file_path, "r") as file:
        lines_list_raw = file.readlines()

    for line in lines_list_raw:
        lines_list_stripped.append(line.strip())

    for entry in lines_list_stripped:
        l_entry = entry.replace("L","-")
        r_entry = l_entry.replace("R", "")
        lines_list.append(int(r_entry))

    return lines_list

def handle_negative_instruction(instruction):
    while instruction <= -100:
        zero_counter.append(0)
        instruction += 100
    return instruction

def handle_positive_instruction(instruction):
    while instruction >= 100:
        zero_counter.append(0)
        instruction -= 100
    return instruction

def door_code():
    position = 50
    instructions_list = get_instructions()
    for instruction in instructions_list:
        if instruction <= -100:
            instruction = handle_negative_instruction(instruction)
        if instruction >= 100:
            instruction = handle_positive_instruction(instruction)

        start_position = position
        position += instruction

        if position == 0:
            zero_counter.append(0)

        if position >= 100:
            position -= 100
            if start_position != 0:
                zero_counter.append(0)
        elif position < 0:
            position += 100
            if start_position != 0:
                zero_counter.append(0)


    print(len(zero_counter))