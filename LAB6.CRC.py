def crc32(input_data):
    crc = 0xFFFFFFFF
    polynom = 0x04C11DB7
    for i in input_data:
        crc = crc ^ i
        if crc & 1:
            crc = (crc >> 1) ^ polynom
        else:
            crc = crc >> 1

    return crc ^ 0xFFFFFFFF


data = input("Введите ваше сообщение: ").encode("utf-8")
print(hex(crc32(data)))
