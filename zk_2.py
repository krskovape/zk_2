#Function for loading a sequence from input txt file
def SequenceFromFile(file_name):
    try:
        with open(file_name, encoding="utf-8") as f:
            data = f.read().split()
            sequence = []
            index = -1
            for x in data:
                index += 1
                try:
                    y = int(x)
                    sequence.append(y)
                except ValueError:
                    print(f"Element in position {index} in {file_name} is not a number and the program will skip this element")
                    continue
                except:
                    print(f"Unexpected error occurred with element in position {index} in {file_name} and the program will skip it")
                    continue
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

def SequenceIntersection(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    s3 = []
    for element in s1:
        if element in s2:
            s3.append(element)
            WriteToFile("output.txt", f"{element} ")
    return s3

sequence_1 = SequenceFromFile("input1.txt")
sequence_2 = SequenceFromFile("input2.txt")

s_intersection = SequenceIntersection(sequence_1, sequence_2)