# https://app.codesignal.com/company-challenges/spacex/

def cpuEmulator(subroutine):
    registers = [0 for _ in range(43)]
    index = 0
    while index != len(subroutine):
        routine = subroutine[index].split(" ")
        instruction = routine[0]
        # MOV
        if instruction == "MOV":
            r1, r2 = routine[1].split(",")
            r2 = int(r2[2]) if r2[1:].startswith("0") else int(r2[1:])
            if r1.startswith("R"):
                r1 = int(r1[2]) if r1[1:].startswith("0") else int(r1[1:])
                registers[r2] = registers[r1]
            else:
                registers[r2] = int(r1)
            index += 1
        # ADD
        if instruction == "ADD":
            r1, r2 = routine[1].split(",")
            r1 = int(r1[2]) if r1.startswith("0") else int(r1[1:])
            r2 = int(r2[2]) if r2.startswith("0") else int(r2[1:])
            registers[r1] = (registers[r1] + registers[r2]) % 2**32
            index += 1
        # DEC
        if instruction == "DEC":
            r1 = routine[1]
            r1 = int(r1[2]) if r1.startswith("0") else int(r1[1:])
            registers[r1] -= 1
            if registers[r1] < 0:
                registers[r1] = (2**32) - 1
            index += 1
        # INC
        if instruction == "INC":
            r1 = routine[1]
            r1 = int(r1[2]) if r1.startswith("0") else int(r1[1:])
            registers[r1] += 1
            if registers[r1] > (2**32) - 1:
                registers[r1] = 0
            index += 1
        # INV
        if instruction == "INV":
            r1 = routine[1]
            r1 = int(r1[2]) if r1.startswith("0") else int(r1[1:])
            r1_value = registers[r1]
            registers[r1] = ~r1_value
            index += 1
        # JUMP
        if instruction == "JMP":
            r1 = int(routine[1]) - 1
            index = r1
        # JUMP R00 = 0
        if instruction == "JZ":
            r1 = int(routine[1]) - 1
            if registers[0] == 0:
                index = r1
            else:
                index += 1
        if instruction == "NOP":
            if instruction == subroutine[-1]:
                break
            else:
                index += 1
    return str(registers[42] & 0xFFFFFFFF)


# Test

#subroutine =["MOV 5,R00", "MOV 10,R01", "JZ 7", "ADD R02,R01", "DEC R00", "JMP 3", "MOV R02,R42"] #"50"
#subroutine = ["MOV 32,R00", "MOV 1,R41", "JZ 8", "MOV R41,R42", "ADD R41,R42", "DEC R00", "JMP 3", "NOP"] #"2147483648"
#subroutine = ["MOV 32,R00", "MOV 1,R41", "JZ 7", "ADD R41,R41", "DEC R00", "JMP 3", "NOP", "MOV R41,R42"] #"0 "
subroutine = ["INV R41", "ADD R42,R41"] #"4294967295"

print(cpuEmulator(subroutine))
