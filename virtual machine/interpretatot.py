command_codes = {
    "get_data": 1,
    "multiply": 2,
    "sum": 3,
    "compare": 4,
    "equal": 5,
    "not_equal": 6,
    "output": 7,
    "exit": 8
}

file_stream = open("program.txt")
text_of_program = file_stream.read()
memory = text_of_program.split()
commands = list(command_codes.keys())

for i in range(0, len(memory)):
    if commands.count(memory[i]) != 0:
        memory[i] = command_codes[memory[i]]
    else:
        try:
            memory[i] = int(memory[i])
        except ValueError:
            memory[i] = 0

while len(memory) <= 120:
    memory.append(-1)

print(memory)

ip = 0
reg = 0

while True:
    match memory[ip]:
        case 1:
            memory[memory[ip + 2]] = memory[ip + 1]
            ip += 3
        case 2:
            memory[memory[ip + 3]] = memory[memory[ip + 1]] * memory[memory[ip + 2]]
            ip += 4
        case 3:
            memory[memory[ip + 3]] = memory[memory[ip + 1]] + memory[memory[ip + 2]]
            ip += 4
        case 4:
            if memory[memory[ip + 1]] == memory[ip + 2]:
                reg = 1
            else:
                reg = 0
            ip += 3
        case 5:
            if reg == 1:
                ip = memory[ip + 1]
            else:
                ip += 2
        case 6:
            if reg == 0:
                ip = memory[ip + 1]
            else:
                ip += 2
        case 7:
            print(memory[ip + 1])
            ip += 2
        case 8:
            break
        case _:
            print("mistake:", ip)
            break