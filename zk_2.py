from os import stat

#Function for loading a sequence from input txt file
def SequenceFromFile(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            if stat(file_name).st_size == 0:
                print("File is empty.")
                quit()
            data = f.read().split()
            return data
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except Exception as e:
        print(f"Unexpected error opening {file_name}: {e}")
        quit()

#Function for writing into output txt file
def WriteToFile(file_name, text):
    try:
        with open(file_name, mode="a", encoding="utf-8") as f:
            return f.write(str(text))
    except FileNotFoundError:
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except Exception as e:
        print(f"Unexpected error opening {file_name}: {e}")
        quit()

#Function for converting string elements into integers
def StrToInt(list):
    sequence = []
    index = -1
    for x in list:
        index += 1
        try:
            y = int(x)
            sequence.append(y)
        except ValueError:
            print(f"Element in position {index} in {list} is not a number and the program will skip this element")
            continue
    return sequence

#Loading sequences from files, converting to integers and deleting duplicate elements
sequence_1 = SequenceFromFile("input1.txt")
sequence_2 = SequenceFromFile("input2.txt")
s1 = list(set(StrToInt(sequence_1)))
s2 = list(set(StrToInt(sequence_2)))

#Loop for intersection of sequences
s_intersection = []
for element in s1:
    if element in s2:
        s_intersection.append(element)
        WriteToFile("output.txt", f"{element} ")