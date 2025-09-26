import os
import shutil

def os_file_manager():
   
    while True:
        dir_path = input("Enter a directory path: ").strip()
        if os.path.isdir(dir_path):
            break
        print("Invalid directory.")

   
    backup_dir = os.path.join(dir_path, "backup")
    os.makedirs(backup_dir, exist_ok=True)

    
    copied_count = 0
    for filename in os.listdir(dir_path):
        source_path = os.path.join(dir_path, filename)
        if os.path.isfile(source_path) and filename.lower().endswith(".txt"):
            shutil.copy2(source_path, backup_dir)
            copied_count += 1

    # Print summary
    print("\nBackup complete!")
    print(f"Directory: {dir_path}")
    print(f"Backup folder: {backup_dir}")
    print(f"Total .txt files copied: {copied_count}")


if __name__ == "__main__":
    os_file_manager()
