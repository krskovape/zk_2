#Function for loading a sequence from input txt file
def SequenceFromFile(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            data = f.read().split()
            sequence = []
            for x in data:
                y = int(x)
                sequence.append(y)
            return sequence
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except EOFError:
        print(f"File {file_name} is empty.")
        quit()
    except:
        print(f"Unexpected error opening {file_name}")
        quit()

#Function for writing into output txt file
def WriteToFile(file_name, text):
    try:
        with open(file_name, mode="a", encoding="utf-8") as f:
            return f.write(str(text))
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except:
        print(f"Unexpected error opening {file_name}")
        quit()
