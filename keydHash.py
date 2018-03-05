import binascii


def input_message():
    print "Encryption Begin..."
    message_text = "what do you want from"
    message_bin = bin(int(binascii.hexlify(message_text),16))[2:]
    padding_box(message_bin)
    #import pdb;pdb.set_trace()

def padding_box(message_bin):
    msg_len_bin = bin(len(message_bin))[2:]
    msg_pad_begin = str(message_bin) + '1'
    message_len = len(message_bin)
    padding  =  448 - (message_len+1) % 512
    padded_message = message_bin.ljust(message_len + padding, '0')
    msg_suffix_pad = msg_len_bin.zfill(64)
    final_padded_message = padded_message + msg_suffix_pad
    #import pdb;pdb.set_trace()
    compression_box(final_padded_message)                                           #calling compression box here
    print "padding_box"

def compression_box(final_padded_message):
    print "compression box starts here !!!!"
    raw_message = final_padded_message
    message_schedule_list = []
    w_list = []
    x = 0
    y = 32
    initial_value = ['67452301', 'EFCDAB89', '98BADCFE', '10325476', 'C3D2E1F0']    # initialvalue H^-1
    for i in range(0, 16):                                                          # Divison of padded message
        wex_bits = raw_message[x:y]
        message_schedule_list.append(wex_bits)
        x = y + 1
        y = x + 32

    for w_in in range(0, 79):
        if w_in <= 15:
            w_list.append(message_schedule_list[w_in])
        elif w_in > 15:
            w_func = (int(w_list[w_in-16], 2)^int(w_list[w_in-14], 2)^int(w_list[w_in-8], 2)^int(w_list[w_in-3], 2))<<1
            w_list.append(bin(w_func)[2:34])
   #import pdb;pdb.set_trace()
    stage1(w_list, initial_value)

def stage1(raw_msg_list, initial_value):                   #t = 1
    #f1 = (B^C)V(~B^D)
    rounds = 0
    init_val_bin = []
    temp_list = []
    k1 = "5A827999"
    k1_bin = bin(int(k1, 16))[2:].zfill(32)
    for i in initial_value:
        init_val_bin.append(bin(int(i, 16))[2:])

    for j_bit in range(0, 19):
        f1 = (int(init_val_bin[1], 2) & int(init_val_bin[2], 2))
        f2 = (~(int(init_val_bin[1], 2))) & int(init_val_bin[3], 2)
        f_func_1 = f1 | f2
        sum_func = (f_func_1 + int(init_val_bin[0], 2)<<5) + int(k1_bin, 2) + int(raw_msg_list[j_bit], 2)
        temp_list = init_val_bin
        init_val_bin[0] = bin(sum_func)[2:34]
        init_val_bin[1] = temp_list[0]
        init_val_bin[2] = bin(int(temp_list[1], 2)<<30)[2:34]
        init_val_bin[3] = temp_list[2]
        init_val_bin[4] = temp_list[3]
    print init_val_bin
    stage2(raw_msg_list, init_val_bin)
   # import pdb;pdb.set_trace()

def stage2(raw_msg_list, init_val_bin):                    #t = 2
    pass
    #f2 = B^C^D
    k2 = '6ED9EBA1'
    k2_bin = bin(int(k2, 16))[2:].zfill(32)

    for i_bit in range(20, 39):
        f_func_2 = int(init_val_bin[1], 2) ^ int(init_val_bin[2], 2) ^ int(init_val_bin[3], 2)
        sum_func2 = f_func_2 + (int(init_val_bin[0], 2)<<5) + int(k2_bin, 2) + int(raw_msg_list[i_bit], 2)
        temp_list = init_val_bin
        init_val_bin[0] = bin(sum_func2)[2:34]
        init_val_bin[1] = temp_list[0]
        init_val_bin[2] = bin(int(temp_list[1], 2)<<30)[2:34]
        init_val_bin[3] = temp_list[2]
        init_val_bin[4] = temp_list[3]
    print init_val_bin
    stage3(raw_msg_list, init_val_bin)
       # import pdb;pdb.set_trace()

def stage3(raw_msg_list, init_val_bin):                   #t = 3
    #f3 = (B&C)or(B&D)or(C&D)
    k3 = '8F1BBCDC'
    k3_bin = bin(int(k3, 16))[2:].zfill(32)

    for k_bit in range(40, 59):
        f_func_3 = (int(init_val_bin[1], 2) & int(init_val_bin[2], 2)) | (int(init_val_bin[1], 2) & int(init_val_bin[3], 2))|(int(init_val_bin[2], 2) & int(init_val_bin[3], 2))
        sum_func3 = f_func_3 + (int(init_val_bin[0], 2)<<5) + int(k3_bin, 2) + int(raw_msg_list[k_bit], 2)
        temp_list = init_val_bin
        init_val_bin[0] = bin(sum_func3)[2:34]
        init_val_bin[1] = temp_list[0]
        init_val_bin[2] = bin(int(temp_list[1], 2)<<30)[2:34]
        init_val_bin[3] = temp_list[2]
        init_val_bin[4] = temp_list[3]
    print init_val_bin
    stage4(raw_msg_list, init_val_bin)
    #import pdb;pdb.set_trace()
    pass

def stage4(raw_msg_list, init_val_bin):                   #t = 4
    #f4 = B^C^D
    k4 = 'CA62CAD6'
    k4_bin = bin(int(k4, 16))[2:].zfill(32)

    for l_bit in range(60, 79):
        f_func_4 = int(init_val_bin[1], 2) ^ int(init_val_bin[2], 2) ^ int(init_val_bin[3], 2)
        sum_func4 = f_func_4 + (int(init_val_bin[0], 2)<<5) + int(k4_bin, 2) + int(raw_msg_list[l_bit], 2)
        temp_list = init_val_bin
        init_val_bin[0] = bin(sum_func4)[2:34]
        init_val_bin[1] = temp_list[0]
        init_val_bin[2] = bin(int(temp_list[1], 2)<<30)[2:34]
        init_val_bin[3] = temp_list[2]
        init_val_bin[4] = temp_list[3]
    print init_val_bin


input_message()

