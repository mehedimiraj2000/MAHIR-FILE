import base64
import zlib
import os as ERROR

logo = """[ _______  _______          _________ _______ 
(       )(  ___  )|\     /|\__   __/(  ____ )
| () () || (   ) || )   ( |   ) (   | (    )|
| || || || (___) || (___) |   | |   | (____)|
| |(_)| ||  ___  ||  ___  |   | |   |     __)
| |   | || (   ) || (   ) |   | |   | (\ (   
| )   ( || )   ( || )   ( |___) (___| ) \ \__
|/     \||/     \||/     \|\_______/|/   \__/
                                              
==========================
🔻UCS MAHIR TOOL🔺
==========================="""

def main():
    ERROR.system("clear")
    print(logo)
    print(" [1] > DECODE ZLIB ")
    print(" [2] > DECODE B64 ")
    print(" [3] > DECODE BASE64 + MAHIR ")
    print("=========================")
    choice = input("CHOICE :")
    if choice == '1':
        dec_zlib()
    elif choice == '2':
        dec_b64()
    elif choice == '3':
        dec_base64_zlib()
    else:
        print("Invalid choice")

def dec_zlib():
    ERROR.system("clear")
    print(logo)
    print(" Example >>  /sdcard/file_icd.py")
    print("============================")
    code = input(" input file: ")
    try:
        with open(code, 'rb') as decode:
            compressed_data = decode.read()
            decompressed_data = zlib.decompress(compressed_data)
            decompressed_str = decompressed_data.decode('utf-8')
        print(f"Decompressed string: {decompressed_str}")
        with open("Dec_Done.py", "a") as output_file:
            output_file.write("# Dec by saju x\n")
            output_file.write(decompressed_str)
    except zlib.error as e:
        print(f"Zlib decompression error: {e}")
    except Exception as e:
        print(f"Error during decompression: {e}")

def dec_b64():
    ERROR.system("clear")
    print(logo)
    print(" Example >>  /sdcard/file_enc.py")
    print("============================")
    code = input(" input file: ")
    try:
        with open(code, 'rb') as decode:
            encoded_data = decode.read()
            decoded_data = base64.b64decode(encoded_data)
            decoded_str = decoded_data.decode('utf-8')
        print(decoded_str)
        with open("Dec_Done.py", "a") as output_file:
            output_file.write("# Dec by saju x\n")
            output_file.write(decoded_str)
    except base64.binascii.Error as e:
        print(f"Base64 decoding error: {e}")
    except Exception as e:
        print(f"Error during base64 decoding: {e}")

def dec_base64_zlib():
    ERROR.system("clear")
    print(logo)
    print(" Example >>  /sdcard/file_icd.py")
    print("============================")
    code = input(" input file: ")
    try:
        with open(code, 'rb') as decode:
            encoded_data = decode.read()
            
            # Fix padding if needed
            missing_padding = len(encoded_data) % 4
            if missing_padding:
                encoded_data += b'=' * (4 - missing_padding)
                
            try:
                base64_decoded_data = base64.b64decode(encoded_data)
            except base64.binascii.Error as e:
                print(f"Base64 decoding error: {e}")
                return

            try:
                decompressed_data = zlib.decompress(base64_decoded_data)
            except zlib.error as e:
                print(f"Zlib decompression error: {e}")
                return

            decompressed_str = decompressed_data.decode('utf-8')
            print(decompressed_str)
            with open("Dec_Done.py", "a") as output_file:
                output_file.write("# Dec by saju x\n")
                output_file.write(decompressed_str)
    except Exception as e:
        print(f"Error during combined base64 and zlib decoding: {e}")

main()
