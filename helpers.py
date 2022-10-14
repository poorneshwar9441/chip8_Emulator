from BitVector import BitVector

def First_N_Bits(num,start,end,size1):
    bits = BitVector(intVal = num,size = size1)
    bit_vec = []
    for i in range(start,end):
        bit_vec.append(bits[i])
        
    return int(BitVector(bitlist = bit_vec))
        
        
        
def Merge_Instructions(inst1,inst2):
    bits1 = BitVector(intVal = inst1,size = 8)
    bits2 = BitVector(intVal = inst2,size = 8)
    
    bit_vec = []
    for i in range(8):
        bit_vec.append(bits1[i])
        
    for i in range(8):
        bit_vec.append(bits2[i])
        
    return BitVector(bitlist = bit_vec)
        

    