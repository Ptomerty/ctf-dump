#!/usr/bin/env python3
import struct, sys, ctypes, mmap
import random
obj_unk2 = {'push':{'arg_count':1,'opcode':0x01,},'pop':{'arg_count':1,'opcode':0x02,},'cmp':{'arg_count':2,'opcode':0x03,},'je':{'arg_count':1,'opcode':0x04,},'jmp':{'arg_count':1,'opcode':0x05,},'call':{'arg_count':1,'opcode':0x05,},'jle':{'arg_count':1,'opcode':0x06,},'jge':{'arg_count':1,'opcode':0x07,},'jl':{'arg_count':1,'opcode':0x08,},'jg':{'arg_count':1,'opcode':0x09,},'mov':{'arg_count':2,'opcode':0x0c,},'xor':{'arg_count':2,'opcode':0x0d,},'add':{'arg_count':2,'opcode':0x0e,},'sub':{'arg_count':2,'opcode':0x0f,},'end':{'arg_count':1,'opcode':0x10,},'read_write_mem':{'arg_count':1,'opcode':0x11,},'nop':{'arg_count':0,'opcode':0x12,},'load':{'arg_count':2,'opcode':0x13,},'store_indirect':{'arg_count':2,'opcode':0x14,},'exit':{'arg_count':0,'opcode':0x15,},'construct_c_func':{'arg_count':0,'opcode':0x25,}}
memory = [0]*(2**(16))
obj_registers = {'ax':0,'bx':0,'cx':0,'dx':0,'ip':0,'sp':0,'bp':0,'cond_flag':0}
def error(reason):
  print('Bad memory condition')
  return exit(1)
def func_struct_unpack(func_arg):
  if isinstance(func_arg, list):
    func_arg = bytes(func_arg)
  return struct.unpack('<H', func_arg)[0]
def get_data(value):
  if isinstance(value, int):
    return value
  func_tup1, func_tup2 = value
  if func_tup1 == 1:
    return func_tup2
  if func_tup1 == 17:
    return obj_registers['ax']
  if func_tup1 == 18:
    return obj_registers['bx']
  if func_tup1 == 19:
    return obj_registers['cx']
  if func_tup1 == 20:
    return obj_registers['dx']
  if func_tup1 == 33:
    return obj_registers['ip']
  if func_tup1 == 34:
    return obj_registers['sp']
  if func_tup1 == 35:
    return obj_registers['bp']
  if func_tup1 == 49:
    return func_struct_unpack(memory[func_tup2:func_tup2 + 2])
  return error('wrong_type')
def pack_and_save_to_mem(func_arg1, value):
  func_intarg1 = '\x00'
  if value >= 256:
    func_intarg1 = struct.pack('<H', value)
  else:
    func_intarg1 = bytes([value])
  func_arg1 = get_data(func_arg1)
  int_counter = 0
  for int_counter2 in func_intarg1:
    memory[func_arg1 + int_counter] = int_counter2
    int_counter += 1
def get_memory_from_register(func_arg1, count=2):
  func_arg1 = get_data(func_arg1)
  return memory[func_arg1:func_arg1 + 2]
def set_register(func_arg1, value):
  func_tup1, func_tup2 = func_arg1
  if func_tup1 in [1, 49]:
    pack_and_save_to_mem(func_tup2, value)
  elif func_tup1 == 17:
    obj_registers['ax'] = value
  elif func_tup1 == 18:
    obj_registers['bx'] = value
  elif func_tup1 == 19:
    obj_registers['cx'] = value
  elif func_tup1 == 20:
    obj_registers['dx'] = value
  elif func_tup1 == 33:
    obj_registers['ip'] = value
  elif func_tup1 == 34:
    obj_registers['sp'] = value
  elif func_tup1 == 35:
    obj_registers['bp'] = value
def main(ROM):
  counter = 0
  for byte in ROM:
    memory[counter] = byte
    counter += 1
  counter += 16 
  obj_registers['ip'] = func_struct_unpack(memory[0:2])
  obj_registers['bp'] = counter
  obj_registers['sp'] = counter
  while True:
    instr_obj = memory[obj_registers['ip']]
    instruction = None
    # ('registers: '+repr(obj_registers))
    for arg1, arg2 in obj_unk2.items():
      if instr_obj == arg2['opcode']:
        instr_obj = arg2
        instruction = arg1
        break
    if not instruction:
      error('invalid_instruction')
      return
    arg_count = instr_obj['arg_count']
    # ('instruction: '+repr(instr_obj))
    asm_args = []
    for int_counter2 in range(arg_count):
      func_int_arg7 = memory[obj_registers['ip'] + 2 + (4 * int_counter2):obj_registers['ip'] + 2 + (4 * int_counter2) + 4]
      func_int_arg8 = func_struct_unpack(func_int_arg7[0:2])
      func_int_arg7 = func_struct_unpack(func_int_arg7[2:4])
      asm_args.append((func_int_arg8, func_int_arg7))
    obj_registers['ip'] += 2 + (4 * arg_count)
    # ('args: '+repr(asm_args))
    # print(instruction + ' '+ repr(asm_args))
    if instruction == 'mov':
      set_register(asm_args[0], get_data(asm_args[1]))
    elif instruction == 'add':
      set_register(asm_args[0], get_data(asm_args[0]) + get_data(asm_args[1]))
    elif instruction == 'sub':
      set_register(asm_args[0], get_data(asm_args[0]) - get_data(asm_args[1]))
    elif instruction == 'xor':
      set_register(asm_args[0], get_data(asm_args[0]) ^ get_data(asm_args[1]))
    elif instruction == 'nop':
      pass
    elif instruction == 'cmp':
      func_int_arg8 = int(get_data(asm_args[0]))
      func_int_arg9 = int(get_data(asm_args[1]))
      if func_int_arg8 == func_int_arg9:
        obj_registers['cond_flag'] = 1
      if func_int_arg8 < func_int_arg9:
        obj_registers['cond_flag'] = 2
      if func_int_arg8 > func_int_arg9:
        obj_registers['cond_flag'] = 3
    elif instruction == 'jmp':
      obj_registers['ip'] = get_data(asm_args[0])
    elif instruction == 'jg':
      if obj_registers['cond_flag'] == 3:
        obj_registers['ip'] = get_data(asm_args[0])
    elif instruction == 'jl':
      if obj_registers['cond_flag'] == 2:
        obj_registers['ip'] = get_data(asm_args[0])
    elif instruction == 'je':
      if obj_registers['cond_flag'] == 1:
        obj_registers['ip'] = get_data(asm_args[0])
    elif instruction == 'jle':
      if obj_registers['cond_flag'] in [2, 1]:
        obj_registers['ip'] = get_data(asm_args[0])
    elif instruction == 'jge':
      if obj_registers['cond_flag'] in [3, 1]:
        obj_registers['ip'] = get_data(asm_args[0])
    elif instruction == 'push':
      pack_and_save_to_mem(obj_registers['sp'], get_data(asm_args[0]))
      obj_registers['sp'] += 2 
    elif instruction == 'pop':
      set_register(asm_args[0], func_struct_unpack(get_memory_from_register(obj_registers['sp'])))
      obj_registers['sp'] -= 2 
    elif instruction == 'end':
      return(get_data(asm_args[0]))
    elif instruction == 'load':
      set_register(asm_args[0], func_struct_unpack(get_memory_from_register(get_data(asm_args[1]))))
    elif instruction == 'store_indirect':
      pack_and_save_to_mem(asm_args[0], get_data(asm_args[1]))
    elif instruction == 'read_write_mem':
      print("memory at stack pointer {1} is {0}".format(memory[obj_registers['sp']], obj_registers['sp']))
      print("memory at instr pointer {1} is {0}".format(memory[obj_registers['ip']], obj_registers['ip']))
      print(bytes(memory[1398:]).replace(b'\x00', b''))
      ax_reg = obj_registers['ax']
      bx_reg = obj_registers['bx']
      cx_reg = obj_registers['cx']
      if ax_reg == 1:
        for i in range(cx_reg):
          temp = memory[bx_reg + i]
          memory[bx_reg + i] = ord(sys.stdin.read(1)) # ord(sys.stdin.read(1))
          print("memory at location {0} changed from {1} to {2}".format(bx_reg + i, temp, memory[bx_reg + i]))
      elif ax_reg == 2:
        sys.stdout.write(''.join([chr(i) for i in memory[bx_reg:bx_reg + cx_reg]]))
    elif instruction == 'exit':
      exit()
    elif instruction == 'construct_c_func':
      id_of_rest_of_mem = id(memory[obj_registers['ip']:]) + 48 # this is running shellcode i hate it
      func_int_arg14 = bytes(memory[obj_registers['ip']:]).replace(b'\x00', b'')
      print(func_int_arg14)
      mmap_obj = mmap.mmap(-1, mmap.PAGESIZE, prot=mmap.ACCESS_READ|mmap.ACCESS_WRITE)
      c_func_prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) # int func(int)
      void_mmap_obj = ctypes.c_void_p.from_buffer(mmap_obj) # (void *) (mmap region)
      full_c_function = c_func_prototype(ctypes.addressof(void_mmap_obj)) # itn func((void *) (mmaped region))
      mmap_obj.write(func_int_arg14)
      func_int_arg15 = full_c_function(id_of_rest_of_mem)
      del void_mmap_obj
      mmap_obj.close()
    # if abs(obj_registers['sp'] - 1192) < 10:
    
    for reg, val in obj_registers.items():
      obj_registers[reg] = val % 0xffff
    # ('registers: '+repr(obj_registers))
    # ('-'*60)
  return
if __name__ == '__main__':
  ROM=b'\x92\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x01\x00.\x00\x15\x00\x0c\x00\x12\x00\x12\x00\x01\x00\x00\x00\x05\x00\x01\x00b\x00\x05\x00\x01\x00.\x00\x01\x00!\x00!\x00\x01\x00#\x00#\x00\x01\x00\x11\x00\x11\x00\x01\x00\x12\x00\x12\x00\x01\x00\x13\x00\x13\x00\x01\x00\x14\x00\x14\x00\x0c\x00#\x00#\x00"\x00"\x00\x05\x00\x01\x00b\x00\x02\x00\x14\x00\x14\x00\x02\x00\x13\x00\x13\x00\x02\x00\x12\x00\x12\x00\x02\x00\x11\x00\x11\x00\x02\x00#\x00#\x00\x02\x00!\x00!\x00\x05\x00\x01\x00b\x00\x10\x00\x01\x00\x00\x00\x0c\x00#\x00#\x00\x01\x00\x8c\x00\x05\x00\x01\x00\xa2\x00\x0c\x00\x14\x00\x14\x00"\x00"\x00\x0e\x00\x14\x00\x14\x00\x01\x00\xff\x00\x14\x00"\x00"\x00\x01\x00h\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00t\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00t\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00p\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00s\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00:\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00/\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00/\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00a\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00a\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00r\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00o\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00n\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00e\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00s\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00a\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00u\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00.\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00c\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00o\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00m\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00/\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00f\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00i\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00l\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00e\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00s\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00/\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00o\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00b\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00j\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00e\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00c\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00t\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00i\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00v\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00e\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00l\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00y\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00-\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00w\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00r\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00o\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00n\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00g\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00.\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00p\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00n\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x01\x00g\x00\x0e\x00"\x00"\x00\x01\x00\x01\x00\x0c\x00\x11\x00\x11\x00\x01\x00\x01\x00\x0c\x00\x12\x00\x12\x00\x14\x00\x14\x00\x0c\x00\x13\x00\x13\x00\x01\x00\x01\x00\x11\x00\x01\x00\x01\x00\x13\x00\x13\x00\x13\x00\x14\x00\x14\x00\x03\x00\x13\x00\x13\x00\x01\x00>\x00\x04\x00\x01\x00\x0e\x05\x03\x00\x13\x00\x13\x00\x01\x00<\x00\x04\x00\x01\x00\x1e\x05\x03\x00\x13\x00\x13\x00\x01\x00+\x00\x04\x00\x01\x00.\x05\x03\x00\x13\x00\x13\x00\x01\x00-\x00\x04\x00\x01\x00R\x05\x03\x00\x13\x00\x13\x00\x01\x00?\x00\x04\x00\x01\x00v\x05\x05\x00\x01\x00\x8a\x04\x0e\x00"\x00"\x00\x01\x00\x01\x00\x05\x00\x01\x00\x8a\x04\x0f\x00"\x00"\x00\x01\x00\x01\x00\x05\x00\x01\x00\x8a\x04\x13\x00\x13\x00\x13\x00"\x00"\x00\x0e\x00\x13\x00\x13\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x13\x00\x13\x00\x05\x00\x01\x00\x8a\x04\x13\x00\x13\x00\x13\x00"\x00"\x00\x0f\x00\x13\x00\x13\x00\x01\x00\x01\x00\x14\x00"\x00"\x00\x13\x00\x13\x00\x05\x00\x01\x00\x8a\x04\x05\x00\x01\x00\x8a\x04'
  main(ROM)