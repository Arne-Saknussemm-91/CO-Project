pc = 0  #program counter

r_address = {
  "x0": "00000",
  "x1": "00001",
  "zero": "00000",
  "ra": "00001",
  "sp": "00010",
  "gp": "00011",
  "tp": "00100",
  "t0": "00101",
  "t1": "00110",
  "t2": "00111",
  "s0/fp": "01000",
  "s1": "01001",
  "a0": "01010",
  "a1": "01011",
  "a2": "01100",
  "a3": "01101",
  "a4": "01111",
  "a5": "01111",
  "a6": "10000",
  "a7": "10001",
  "s2": "10010",
  "s3": "10011",
  "s4": "10100",
  "s5": "10101",
  "s6": "10110",
  "s7": "10111",
  "s8": "11000",
  "s9": "11001",
  "s10": "11010",
  "s11": "11011",
  "t3": "11100",
  "t4": "11101",
  "t5": "11110",
  "t6": "11111",
  "x2": "00010",
  "x3": "00011",
  "x4": "00100",
  "x5": "00101",
  "x6": "00110",
  "x7": "00111",
  "x8": "01000",
  "x9": "01001",
  "x10": "01010",
  "x11": "01011",
  "x12": "01100",
  "x13": "01101",
  "x14": "01110",
  "x15": "01111",
  "x16": "10000",
  "x17": "10001",
  "x18": "10010",
  "x19": "10011",
  "x20": "10100",
  "x21": "10101",
  "x22": "10110",
  "x23": "10111",
  "x24": "11000",
  "x25": "11001",
  "x26": "11010",
  "x27": "11011",
  "x28": "11100",
  "x29": "11101",
  "x30": "11110",
  "x31": "11111"
}

r_ins = {
    "add": {
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0000000"
    },
    "xor": {
        "opcode": "0110011",
        "funct3": "100",
        "funct7": "0000000"
    },
    "sub": {
        "opcode": "0110011",
        "funct3": "000",
        "funct7": "0100000"
    },
    "slt": {
        "opcode": "0110011",
        "funct3": "010",
        "funct7": "0000000"
    },
    "sltu": {
        "opcode": "0110011",
        "funct3": "011",
        "funct7": "0000000"
    },
    "sll": {
        "opcode": "0110011",
        "funct3": "001",
        "funct7": "0000000"
    },
    "srl": {
        "opcode": "0110011",
        "funct3": "101",
        "funct7": "0000000"
    },
    "or": {
        "opcode": "0110011",
        "funct3": "110",
        "funct7": "0000000"
    },
    "and": {
        "opcode": "0110011",
        "funct3": "111",
        "funct7": "0000000"
    },
    "lw": {
        "opcode": "0000011",
        "funct3": "010"
    },
    "addi": {
        "opcode": "0010011",
        "funct3": "000"
    },
    "sltiu": {
        "opcode": "0010011",
        "funct3": "011"
    },
    "jalr": {
        "opcode": "1100111",
        "funct3": "000"
    }
}

i_ins = {
    "lw": {
        "opcode": "0000011",
        "funct3": "010"
    },
    "addi": {
        "opcode": "0010011",
        "funct3": "000"
    },
    "jalr": {
        "opcode": "1100111",
        "funct3": "000"
    }
}

s_ins = {
    "sw": {"opcode": "0100011", "funct3": "010"}}

b_ins = {
    "beq": {
        "opcode": "1100011",
        "funct3": "000"
    },
    "bne": {
        "opcode": "1100011",
        "funct3": "001"
    },
    "bge": {
        "opcode": "1100011",
        "funct3": "010"
    },
    "blt": {
        "opcode": "1100011",
        "funct3": "100"
    }
}

u_ins = {
    "lui": {"opcode": "0110111"},"auipc": {"opcode": "0010111"}}

j_ins = {
    "jal": {"opcode": "1101111"}}

def is_R_type(ins):
    if len(ins) == 4:
        if ins[pc] in r_ins:
            if ins[1] in r_address:
                if ins[2] in r_address:
                    if ins[3] in r_address:
                        return True
    else:
        return False

def is_I_type(ins):
    if len(ins) == 4:
        return True
    elif ins[pc] in i_ins:
        return True
    else:
        return False

def is_S_type(ins):
    return ins in s_ins

def is_B_type(ins):
    return ins in b_ins

def is_U_type(ins):
    return ins in u_ins

def is_J_type(ins):
    return ins in j_ins

def is_label(ins):
    return ins[0] == ":"

def is_var(ins):
    return ins[0] == "var"

def is_reg(ins):
    return ins in r_address

def assembly_to_binary(instruction):
    ins = [i.strip() for i in instruction.replace(',', ' ').split()]
    if is_R_type(ins):
        answer = ""
        answer += r_ins[ins[0]]["funct7"]
        answer += r_address[ins[3]]
        answer += r_address[ins[2]]
        answer += r_ins[ins[0]]["funct3"]
        answer += r_address[ins[1]]
        answer += r_ins[ins[0]]["opcode"]
        return answer
    elif is_I_type(ins):
        d

with open("file1.txt", "r") as file:
    instructions = file.readlines()

print(assembly_to_binary(instructions[0]))
