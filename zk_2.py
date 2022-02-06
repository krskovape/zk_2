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
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorect")
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
        print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorect")
        quit()
    except PermissionError:
        print(f"Program doesn't have permisson to acces file {file_name}.")
        quit()
    except Exception as e:
        print(f"Unexpected error opening {file_name}: {e}")
        quit()

#Function for deleting duplicate elements and converting string elements into integers
def StrToSetInt(sqnc):
    set_list = list(set(sqnc))
    sequence = []
    index = -1
    for x in set_list:
        index += 1
        try:
            y = int(x)
            sequence.append(y)
        except ValueError:
            print(f"Element in position {index} in {sqnc} is not a number and the program will skip this element")
            continue
    return sequence

#Function for intersection of two sequences
def SequenceIntersection(list1, list2):
    s1 = StrToSetInt(list1)
    s2 = StrToSetInt(list2)
    s3 = []
    for element in s1:
        if element in s2:
            s3.append(element)
            WriteToFile("output.txt", f"{element} ")
    return s3

#Loading sequences from input files and calling function for their intersection
sequence_1 = SequenceFromFile("input1.txt")
sequence_2 = SequenceFromFile("input2.txt")

s_intersection = SequenceIntersection(sequence_1, sequence_2)