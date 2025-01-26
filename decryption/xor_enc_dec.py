import os
import sys







# Encrypt or decrypt a file using XOR with a key string
def xor_decrypt(input_file, output_file, key):
    with open(input_file, 'rb') as f_in:
        data = f_in.read() 

    key_bytes = key.encode('utf-8')  # Convert the string key to bytes
    key_length = len(key_bytes)

    # Apply XOR byte by byte loop through key bytes
    output_data = bytearray()
    for i, byte in enumerate(data):
        key_byte = key_bytes[i % key_length]  
        output_data.append(byte ^ key_byte) 
    # Write to output file
    with open(output_file, 'wb') as f_out:
        f_out.write(output_data) 


def main():
    key = "replace_me" 
    # Used to get current path, this script was used to decrypt files in a folder.
    folder_path = os.getcwd()

    for filename in os.listdir(folder_path):
        # full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if it is a file (not a subdirectory)
        if os.path.isfile(file_path):
            filename, file_extension = os.path.splitext(filename)
            print(file_extension)
            #print(filename)
            #sys.exit()

            # If file ext matches decrypt the file.
            if file_extension == ".ext goes here":
                decrypted_filename= f"decrypted-{filename}"
                filename = f"{filename}.{file_extension}"
                print(f"Decrypting: {filename}")
                xor_decrypt(filename, decrypted_filename, key)
                print(f"Saved as: {decrypted_filename}")

   

if __name__ == "__main__":
    main()


















