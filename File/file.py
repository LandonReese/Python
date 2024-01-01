def fileExtensionSeparator(fileName: str):
    """Takes an input file, and separates its contents into three new text files for each file extension
       This code assumes that each filename is on a newline in the input text

    Args:
        fileName (str): The filename of the input text
    """
    inputFile = open(fileName, "r")
    c_file = open("c_file.txt", "w")
    cs_file = open("cs_file.txt", "w")
    cpp_file = open("cpp_file.txt", "w")

    for line in inputFile:
        # Sets the prefix to the filename, and the suffix to the extension
        if line:
            # Strip the newline character off of the end
            line = line.strip()
            prefix, suffix = line.split(".")
        
            if suffix == "cpp":
                cpp_file.write(f"{prefix}.{suffix}\n")
            elif suffix == "cs":
                cs_file.write(f"{prefix}.{suffix}\n")
            elif suffix == "c":
                c_file.write(f"{prefix}.{suffix}\n")
            else:
                print(f"File {line} not found")
        else:
            print(f"File extension unknown")

    inputFile.close()
    c_file.close()
    cs_file.close()
    cpp_file.close()
    
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#
file = "input.txt"
fileExtensionSeparator(file)