saiso = 0.25
def decode_ir_raw(raw_data):
    # Tolerance function with 10% flexibility
    def within_tolerance(value, target):
        return abs(value - target) <= saiso * abs(target)

    # Extract header and footer
    header = raw_data[:2]  # 2 số đầu
    body = raw_data[2:-1]  # Các số giữa
    footer = raw_data[-1]  # Số cuối cùng

    # Debugging header and footer
    print(f"Header: {header}, Footer: {footer}")

    # Initialize decoded bits
    decoded_bits = []

    # Process the body in pairs
    for i in range(0, len(body), 2):
        # Pair of numbers
        pulse, space = body[i], body[i + 1]

        # Decode based on the rules
        if within_tolerance(pulse, 385) and within_tolerance(space, -380):
            decoded_bits.append("0")
        elif within_tolerance(pulse, 385) and within_tolerance(space, -1200):
            decoded_bits.append("1")
        else:
            print(f"Unrecognized pair: ({pulse}, {space})")  # Debugging
            return "Invalid IR signal"

    # Join bits into a binary string
    decoded_binary = "".join(decoded_bits)

    # Convert binary string to hexadecimal format (LSB-first order)
    hex_groups = []
    for i in range(0, len(decoded_binary), 8):  # Process 8 bits at a time
        byte = decoded_binary[i:i + 8]  # Extract 8 bits
        # byte = byte[::-1]  # Reverse the bits for LSB-first order
        hex_value = hex(int(byte, 2))  # Convert reversed binary to hex
        hex_groups.append(hex_value.upper())

    # Output results
    print("Decoded binary:", decoded_binary)
    print("Decoded hex:", ", ".join(hex_groups))
    print("Number of bits:", len(decoded_binary), "\n")

    return decoded_binary, hex_groups, len(decoded_binary)


# Example usage:
raw_signal = [
[
3194, -3131, 387, -413, 386, -441, 359, -440, 355, -1208, 357, -1207, 357, -443, 357, -442, 358, -441, 356, -445, 355, -442, 356, -1208, 357, -443, 356, -442, 355, -1208, 358, -1206, 362, -1204, 356, -1209, 355, -444, 356, -1207, 359, -441,  357, -1206, 359, -442, 356, -1206, 359, -416, 384, -441, 355, -443, 355, -444, 355, -444, 356, -442, 356, -443, 358, -442, 355, -443, 355, -443, 356, -443, 357, -442, 357, -445, 353, -417, 383, -441, 357, -442, 357, -415, 383, -443, 356, -442, 357,  -414, 390, -441, 352, -445, 354, -441, 357, -419, 382, -441, 356, -443, 357, -415, 384, -442, 358, -440, 357, -442, 357, -443, 355, -443, 357, -442, 359, -1207, 354, -417, 383, -442, 357, -443, 356, -442, 355, -444, 355, -444, 355, -444, 356, -442,  357, -442, 356, -443, 356, -416, 384, -442, 356, -417, 383, -442, 356, -445, 354, -1206, 357, -446, 354, -418, 381, -442, 356, -443, 356, -443, 356, -418, 381, -443, 356, -416, 383, -416, 382, -442, 357, -1207, 356, -444, 356, -1208, 357, -443, 356,  -442, 357, -447, 353, -417, 381, -1184, 379, -418, 382, -1207, 357, -444, 355, -418, 381, -1208, 358
],
[
3201, -3125, 395, -433, 363, -436, 364, -434, 364, -1202, 362, -1202, 363, -435, 363, -437, 363, -436, 365, -434, 366, -432, 365, -1200, 362, -438, 364, -434, 363, -1202, 388, -1177, 363, -1201, 364, -1201, 364, -435, 365, -1200, 365, -434,  365, -1200, 364, -434, 366, -1198, 364, -409, 392, -433, 365, -435, 365, -432, 365, -435, 365, -408, 391, -433, 364, -409, 393, -403, 420, -381, 390, -436, 365, -406, 393, -404, 394, -434, 364, -407, 395, -432, 388, -382, 396, -434, 363, -403, 397,  -404, 418, -380, 396, -432, 365, -434, 366, -406, 416, -409, 365, -434, 366, -433, 365, -435, 365, -404, 396, -432, 365, -406, 392, -410, 415, -380, 396, -1168, 395, -404, 420, -381, 393, -405, 394, -405, 395, -403, 395, -434, 366, -403, 419, -410,  389, -409, 365, -405, 395, -406, 394, -403, 418, -381, 395, -404, 396, -403, 420, -1145, 396, -404, 418, -379, 397, -432, 366, -402, 398, -401, 396, -404, 395, -402, 397, -405, 393, -402, 399, -405, 417, -1144, 420, -379, 396, -402, 420, -379, 397,  -401, 398, -401, 422, -377, 396, -1169, 396, -403, 420, -379, 396, -1168, 397, -401, 396, -1170, 421
]

]

for i in range(0,len(raw_signal),1):     
    print(f"{i+1}. ")
    decoded_result = decode_ir_raw(raw_signal[i])
