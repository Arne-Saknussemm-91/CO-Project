import sys
from collections import OrderedDict

def bin_c(b, n):
  nbits = n.bit_length() + 1

  binary = f"{n & ((1 << nbits) - 1):0{nbits}b}"
  if n >= 0:
    binary = (b - nbits) * '0' + binary
    return binary
  else:
    binary = (b - nbits) * '1' + binary
    return binary


pc = 0  #program counter

#marking the type of functions
type_r = ["add", "xor", "sub", "slt", "sltu", "slt", "sll", "srl", "or", "and"]

type_i = ["lw", "addi", "sltiu", "jalr"]

type_s = ["sw"]

type_b = ["beq", "bne", "bge", "bgeu", "blt", "bltu"]

type_u = ["auipc", "lui"]

type_j = ["jal"]

register = [
    "x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11",
    "x12", "x13", "x14", "x15", "x16", "x17", "x18", "x19", "x20", "x21",
    "x22", "x23", "x24", "x25", "x26", "x27", "x28", "x29", "x30", "x31"
]

r_address = {
    "x0": "00000",
    "x1": "00001",
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

pc = 0

def type_r_check(instruction):
  if (instruction[pc] in type_r):
    global pc
    pc += 1
    return True

  else:
    return False

def type_i_check(instruction):
  if (instruction[pc] in type_i):
    global pc
    pc += 1
    return True
  else:
    return False

def type_s_check(instruction):
  if (instruction[pc] in type_s):
    global pc
    pc += 1
    return True
  else:
    return False

def type_b_check(instruction):
  if (instruction[pc] in type_b):
    global pc
    pc += 1
    return True
  else:
    return False

def type_u_check(instruction):
  if (instruction[pc] in type_u):
    global pc
    pc += 1
    return True
  else:
    return False

def type_j_check(instruction):
  if (instruction[pc] in type_j):
    global pc
    pc += 1
    return True
  else:
    return False



def type_r_format(instruction):
  if (instruction[pc] in type_r):
    if (instruction[1] in type_r):
      return True
    else:
      return False
  else:
    return False

  
def is_typeA(instruction: str) -> bool:
    instruction = instruction.split()
    if len(instruction) != 4:
        return False
    for j, i in enumerate(instruction):
        instruction[j] = i.strip()

    if instruction[0] in OP_code_typeA.keys():
        if instruction[1] == "FLAGS":
            print("ERROR: Illegal use of FLAGS register")
            exit()
        elif instruction[1] in reg_address.keys():
            if instruction[2] == "FLAGS":
                print("ERROR: Illegal use of FLAGS register")
                exit()
            elif instruction[2] in reg_address.keys():
                if instruction[3] == "FLAGS":
                    print("ERROR: Illegal use of FLAGS register")
                    exit()
                elif instruction[3] in reg_address.keys():
                    return True
                else:
                    print("ERROR: Typos in register name")
                    exit()
            else:
                print("ERROR: Typos in register name")
                exit()

        else:
            print("ERROR: Typos register name")
            exit()
    return False
def type_i_format(instruction):
  if (instruction[pc] in type_i):
    if (instruction[1] in type_i):
      return True
    else:
      return False
  else:
    return False


#----------------------------------------------------------------------
#function to check if the instruction is a type S format
def type_s_format(instruction):
  if (instruction[pc] in type_s):
    if (instruction[1] in type_s):
      return True
    else:
      return False
  else:
    return False


#----------------------------------------------------------------------
#function to check if the instruction is a type B format
def type_b_format(instruction):
  if (instruction[pc] in type_b):
    if (instruction[1] in type_b):
      return True
    else:
      return False
  else:
    return False


#----------------------------------------------------------------------
#function to check if the instruction is a type U format
def type_u_format(instruction):
  if (instruction[pc] in type_u):
    if (instruction[1] in type_u):
      return True
    else:
      return False
  else:
    return False


#----------------------------------------------------------------------
#function to check if the instruction is a type J format
def type_j_format(instruction):
  if (instruction[pc] in type_j):
    if (instruction[1] in type_j):
      return True
    else:
      return False
  else:
    return False


#----------------------------------------------------------------------


def read(file):  #reading the instructions from the file
  f = open(file, "r")
  lines = f.readlines()
  for i in lines:
    if i is "/n" or "/t" or "":
      lines.remove(i)
    else:
      continue
  f.close()
  return lines


#----------------------------------------------------------------------


def write(file, data):  #writing the data to the file
  f = open(file, "w")
  for i in data:
    f.write(i)
  f.close()


#---------------------------------------------------------------------
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
#---------------------------------------------------------------------
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
#---------------------------------------------------------------------
s_ins = {"sw": {"opcode": "0100011", "funct3": "010"}}
#---------------------------------------------------------------------
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
#---------------------------------------------------------------------
u_ins = {"lui": {"opcode": "0110111"}, "auipc": {"opcode": "0010111"}}
#---------------------------------------------------------------------


instructions = []
operands = {}
c = []
c = read("file.txt")
for i in c:
  d = i.split(" ")
  instructions.append(d[0])
  j = d[1].split(",")
  operands[d[0]] = j


def r_instruction(instruction, operands):
  encoding = ""
  funct3 = r_ins[instruction]["funct3"]
  funct7 = r_ins[instruction]["funct7"]
  encoding += funct7 + r_address[operands[2]] + r_address[operands[
      1]] + funct3 + r_address[operands[0]] + r_ins[instruction]["opcode"]
  return encoding


#-------
def i_instruction(instruction, operands, imm_bin):
  a = ""
  for i in range(len(imm_bin) - 1, 0, -1):
    a += imm_bin[i]
  imm_bin = a

  funct3 = i_ins[instruction]["funct3"]
  encoding = ""
  encoding += imm_bin[0:11] + r_address[operands[2]] + funct3 + r_address[
      operands[1]] + r_address[operands[0]] + i_ins[instruction]["opcode"]
  operands.clear()
  return encoding


#---------
def s_instruction(instruction, operands, imm_bin):
  a = ""
  for i in range(len(imm_bin) - 1, 0, -1):
    a += imm_bin[i]
  imm_bin = a
  encoding = ""
  funct3 = s_ins[instruction]["funct3"]
  encoding += imm_bin[5:11] + r_address[operands[0]] + r_address[
      operands[2]] + funct3 + imm_bin[0:4] + s_ins[instruction]["opcode"]
  operands.clear()
  return encoding


#---------
def b_instruction(instruction, operands, imm_bin):
  a = ""
  for i in range(len(imm_bin) - 1, 0, -1):
    a += imm_bin[i]
  imm_bin = a
  encoding = ""
  funct3 = s_ins[instruction]["funct3"]
  encoding += imm_bin[12] + imm_bin[5:10] + r_address[operands[1]] + r_address[
      operands[0]] + funct3 + imm_bin[1:4] + imm_bin[11] + b_ins[instruction][
          "opcode"]
  #operands.clear()
  return encoding


#----------
def u_instruction(instruction, operands, imm_bin):
  a = ""
  for i in range(len(imm_bin) - 1, 0, -1):
    a += imm_bin[i]
  imm_bin = a
  encoding = ""
  encoding += imm_bin[12:31] + r_address[
      operands[0]] + u_ins[instruction]["opcode"]
  #operands.clear()
  return encoding


#------------
def j_instruction(instruction, operands, imm_bin):
  a = ""
  for i in range(len(imm_bin) - 1, 0, -1):
    a += imm_bin[i]
  imm_bin = a
  encoding = ""
  encoding += imm_bin[20] + imm_bin[1:10] + imm_bin[12:19] + r_address[
      operands[0]] + "1101111"


#for r type bin

if (type_r_check(i[0])):

  if (type_r_format(operands)):
    encoded_instruction = r_instruction(instructions, operands)
    print(encoded_instruction)
  else:
    print("invalid R type instruction")
elif (type_b_check(i[0])):
  if (type_b_check(i[0])):
    instruction = [i]
    operands = i[0:]
    if (type_r_check(operands)):
      encoded_instruction = r_instruction(instructions, operands)
      print(encoded_instruction)
    else:
      print("invalid B type instruction")
