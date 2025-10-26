import os
import shutil

directories = [
    r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\decrypted_files",
    r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\encryptet_files",
    r"C:\MAG\1_LETNIK\1_SEMESTER\IZBRANI_ALGORITMI\Naloga_1_prastevila_in_RSA\IR_Naloga_1_prastevila_in_RSA\keys"
]

def clear_directory(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"Directory {directory} does not exist.")

for dir_path in directories:
    clear_directory(dir_path)

print("Directories cleared successfully.")