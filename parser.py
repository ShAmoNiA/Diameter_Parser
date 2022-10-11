# from asyncio.windows_events import NULL
# import os

# def bit_to_hex(bit):
#     return int(bit/4)

# def slicer(list,data):
#     indices = [0]
#     for item in list:
#         indices.append(bit_to_hex(item))
#     return [data[i:j] for i,j in zip(indices, indices[1:]+[None])]

# def vendor_flag(parts):
#     hex_str = "0x"+parts[1][0:1]
#     integer = int(hex_str, 16)
#     return (format(integer, '0>4b')[0] == "1")

# dir_path = os.path.dirname(os.path.realpath(__file__))
# data = open(dir_path+'\sampleDiameter.txt','r').read()

# version = 8 #bit
# message_length = 24 + version
# Command_flags = 8 + message_length 
# command_code = 24 + Command_flags
# application_ID = 32 + command_code
# hbh_ID = 32 + application_ID
# ete_ID = 32 + hbh_ID

# parts = slicer([version,message_length,Command_flags,command_code,application_ID,hbh_ID,ete_ID],data)

# f = open(dir_path+'\diameter_parse.txt', 'w')
# f.write("version : "+parts[0]+" ("+str(int("0x"+parts[0], 16))+")"+"\n")
# f.write("message length : "+parts[1]+" ("+str(int("0x"+parts[1], 16))+")"+"\n")
# f.write("Command flags : "+parts[2][0:1]+" ("+str(int("0x"+parts[2][0:1], 16))+")"+"\n")
# f.write("Command code : "+parts[3]+" ("+str(int("0x"+parts[3], 16))+")"+"\n")
# f.write("application ID : "+parts[4]+" ("+str(int("0x"+parts[4], 16))+")"+"\n")
# f.write("hop-by-hop ID : "+parts[5]+" ("+str(int("0x"+parts[5], 16))+")"+"\n")
# f.write("end-to-end ID : "+parts[6]+" ("+str(int("0x"+parts[6], 16))+")"+"\n\n")

# data = parts[7] #remove message header from data

# while(True):
#     AVP_code = 32 #bit
#     AVP_flags = 8 + AVP_code
#     AVP_length = 24 + AVP_flags

#     parts = slicer([AVP_code,AVP_flags,AVP_length],data)

#     f.write("AVP code : "+parts[0]+" ("+str(int("0x"+parts[0], 16))+")"+"\n")
#     f.write("AVP flags : "+parts[1][0:1]+" ("+str(int("0x"+parts[1][0:1], 16))+")"+"\n")
#     f.write("AVP length : "+parts[2]+" ("+str(int("0x"+parts[2], 16))+")"+"\n")

#     real_length_byte = int("0x"+parts[2], 16)  #bit
#     if (real_length_byte % 4 != 0):
#         real_length = (real_length_byte - (real_length_byte % 4) + 4)*8
#     else :
#         real_length = real_length_byte * 8

#     data = parts[3] #remove previous AVP

#     if(vendor_flag(parts)):
#         vendor_ID = 32
#         AVP_length += vendor_ID
#         indices = [0,bit_to_hex(vendor_ID)]
#         parts = [data[i:j] for i,j in zip(indices, indices[1:]+[None])]
#         f.write("vendor_ID : "+parts[0]+" ("+str(int("0x"+parts[0], 16))+")"+"\n")
#         data = parts[1]


#     indices = [0,int((real_length - AVP_length)/4)]
#     parts = [data[i:j] for i,j in zip(indices, indices[1:]+[None])]

#     f.write("Data : "+parts[0]+"\n")
#     f.write("*****\n")

#     data = parts[1]
    
#     if(data == ""):
#         break

print( int("1MOyoQIABAAAAAAAAAAAAAAABABxAAAAu58oY5+pCA==", 32))