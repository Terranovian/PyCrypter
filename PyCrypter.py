from cryptography.fernet import Fernet
import getpass
import sys

def generate_key():
    """
    * Generate a Fernet key named 'key'.
    * Prompt the user to enter a file name or path for storing the key.
    * Write the key in binary format to the specified file or path.
    """
    key = Fernet.generate_key()
    key_file = str(input("Enter file name or path for key storage: "))    
    with open(key_file, 'wb') as zoe:
        zoe.write(key)
    print("Key saved to file")

def handle_key_input():
    """
    * Prompt the user to choose between pasting key or selecting key file.
    * Handle user input and return the appropriate Fernet Key object.
    """
    while True:
        try:
            key_choice = int(input("Enter '1' to input key or '2' to select key file: "))
            if key_choice == 1:
                key = getpass.getpass(prompt="Enter your key: ")
                return Fernet(key)
            elif key_choice == 2:
                return input_key_file()
            else:
                print("Invalid option")
        except:
            print("Please enter '1' or '2'")

def input_key_file():
    """
    * Prompt the user to enter the file name or path containing the key.
    * Read the key from the specified file.
    * Return the key as a Fernet Key object.
    """
    while True:
        try:
            key_file = str(input("Enter file name or path to key file: "))
            with open(key_file, 'rb') as ray:
                key = ray.read()
            return Fernet(key)
        except:
            print(f"No Key detected at {key_file}")


def encrypt_data():
    """
    * Request path of file to encrypt.
    * Read file as binary and store in variable 'file_data'.
    * Call key handling.
    * Encrypt the data using the key.
    * Write encrypted data as binary back to the original file.
    """
    while True:
        print("Encrypting")
        file_path = str(input("Specify file path: "))
        try:
            with open(file_path, 'rb') as tom:
                file_data = tom.read()
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")
            continue
        fernet_key = handle_key_input()
        if fernet_key is not None:
            try:
                encrypted_data = fernet_key.encrypt(file_data)
            except Exception as e:
                print(f"Encryption failed: {e}")
                continue
            with open(file_path, 'wb') as kim:
                kim.write(encrypted_data)
            print("File encrypted successfully!") 
            break
    

def decrypt_data():
    """
    * Request path of file to decrypt.
    * Read file as binary and store in variable 'file_data'.
    * Call key handling.
    * Decrypt the data using the key.
    * Write decrypted data as binary back to the original file.
    """
    while True:
        print("Decrypting")
        file_path = str(input("Specify file path: "))
        try:
            with open(file_path, 'rb') as mia:
                file_data = mia.read()  
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")
            continue
        fernet_key = handle_key_input()
        if fernet_key is not None:
            try:
                decrypted_data = fernet_key.decrypt(file_data)
            except Exception as e:
                print(f"Encryption failed: {e}")
                continue
            with open(file_path, 'wb') as jay:
                jay.write(decrypted_data)
            print("File decrypted successfully!") 
            break

def manual():
    print(f"""
    This program allows you to perform cryptographic operations using a Fernet key:
    
    1. Generate Key:
       - Select option 1 to generate a Fernet key.
       - Enter a file name or path to store the key when prompted.
       - The program will generate a key and save it to the specified file.
          
          Note: Ensure you do not lose this key if you encrypt any data with it and store it securely.
    
    2. Encrypt File:
       - Select option 2 to encrypt a file using a Fernet key.
       - Enter the path of the file you want to encrypt when prompted.
       - Choose to input the key directly or select a key file.
         - If inputting the key, enter your key when prompted.
         - If selecting a key file, enter the file name or path containing the key.
       - The program will encrypt the file using the provided key and save the encrypted data back to the original file.
    
    3. Decrypt File:
       - Select option 3 to decrypt a file using a Fernet key.
       - Enter the path of the file you want to decrypt when prompted.
       - Choose to input the key directly or select a key file.
         - If inputting the key, enter your key when prompted.
         - If selecting a key file, enter the file name or path containing the key.
       - The program will decrypt the file using the provided key and save the decrypted data back to the original file.
    
    Note: Ensure you have the correct key for decryption to avoid data loss.
    
    4. Manual:
       - Select option 4 to display this manual, which provides detailed instructions on using the program.
    
    5. Exit:
       - Select option 5 to exit the program.
    
    Please select an option from the menu by entering the corresponding number (1-5).
    """)

def main():
    #MENU
    print(("\nWelcome to Blake's cryptography Python program\n\n"))
    print("Please select from the following options: \n1: Generate Key \n2: Encrypt File \n3: Decrypt File \n4: Manual \n5: Exit")
    while True:
            option = int(input(":"))

            if option == 1:
                #Call function to generate an encryption key
                generate_key()
            elif option ==2:
                #Call function to encrypt data
                encrypt_data()
            elif option == 3:
                #Call function to decrypt data
                decrypt_data()
            elif option == 4:
                #Call function to display manual / how to use program
                manual()
            elif option == 5:
                #Exit the program
                sys.exit()
            else:
                print("Invalid input, Please enter an integer from '1' to '5'")
        




if __name__ == "__main__":
    main()

""" Things I would like to add
* A form of key validation? to check that the correct key is being used for decryption?
* A Key encryption key to encrypt the key, should the KEK be stored hardcoded in the program?
* PBHKMDF whatever its called for password to key derivation for better security then .txt files
* remove storing or accessing keys from files
"""